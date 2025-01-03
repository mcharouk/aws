from aws_cdk import CfnOutput, RemovalPolicy, Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import aws_iam as iam  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_s3 as s3
from constructs import Construct


class DeployContainerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repository_name = "cicd-sample-app"
        # get ecr repository
        repository = ecr.Repository.from_repository_name(
            self, "ECS-CICD-Repository", repository_name
        )

        vpc = ec2.Vpc(
            self,
            "VPC",
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            vpc_name="ECS-CICD-VPC",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name="Private",
                    cidr_mask=24,
                ),
            ],
            nat_gateways=1,
        )

        # create an ecs cluster with fargate capacity providers

        cluster = ecs.Cluster(
            self,
            "ECSCluster",
            cluster_name="ECS-Cluster",
            enable_fargate_capacity_providers=True,
            vpc=vpc,
        )

        ecs_task_execution_role = self.createRole(
            "ECS-CICD-TaskExecutionRoleDemo",
            iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            [],
        )

        self.addManagedPolicy(
            ecs_task_execution_role,
            "service-role/AmazonECSTaskExecutionRolePolicy",
        )

        # create a task definition
        task_definition = ecs.FargateTaskDefinition(
            self,
            "ECS-CICD-TaskDefinition",
            cpu=256,
            memory_limit_mib=512,
            family="ECS-CICD-TaskDefinition",
            task_role=ecs_task_execution_role,
        )

        task_definition.add_container(
            id="ECS-CICD-Container",
            container_name="cicd-sample-app",
            image=ecs.ContainerImage.from_ecr_repository(repository=repository),
            port_mappings=[
                ecs.PortMapping(
                    container_port=5000,
                )
            ],
        )

        alb_sg = ec2.SecurityGroup(
            self,
            "ECS-CICD-AlbSG",
            vpc=vpc,
            description="Allow http access for alb",
            allow_all_outbound=True,
            security_group_name="ECS-CICD-AlbSG",
        )

        alb_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow http access from anywhere",
        )

        # create a security group for ecs service
        ecs_service_sg = ec2.SecurityGroup(
            self,
            "ECS-cicd-ServiceSG",
            vpc=vpc,
            description="Allow http access for ecs service",
            allow_all_outbound=True,
            security_group_name="ECS-cicd-ServiceSG",
        )

        # allow http inbound from alb sg
        ecs_service_sg.connections.allow_from(
            alb_sg,
            ec2.Port.tcp(5000),
            "Allow inbound connections on port 5000",
        )

        alb = elbv2.ApplicationLoadBalancer(
            self,
            "ApplicationLoadBalancer",
            vpc=vpc,
            internet_facing=True,
            security_group=alb_sg,
            load_balancer_name="ECS-CICD-ALB",
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

        alb_listener = alb.add_listener(
            "ECS-CICD-CapaProviderALBListener",
            port=80,
            protocol=elbv2.ApplicationProtocol.HTTP,
            default_action=elbv2.ListenerAction.fixed_response(
                status_code=200,
                content_type="application/json",
                message_body='{"status": "OK"}',
            ),
        )

        # create ecs service
        ecs_service = ecs.FargateService(
            self,
            "ECS-CICD-Service",
            task_definition=task_definition,
            cluster=cluster,
            service_name="ecs-cicd-Service",
            desired_count=1,
            security_groups=[ecs_service_sg],
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            assign_public_ip=False,
            deployment_controller=ecs.DeploymentController(
                type=ecs.DeploymentControllerType.CODE_DEPLOY
            ),
        )

        elbv2.ApplicationTargetGroup(
            self,
            "ECSServiceGreenTargetGroup",
            vpc=vpc,
            port=5000,
            protocol=elbv2.ApplicationProtocol.HTTP,
            target_type=elbv2.TargetType.IP,
            target_group_name="ECSServiceGreenTargetGroup",
        )

        alb_listener.add_targets(
            "ECS-CICD-ServiceBlueTargetGroup",
            port=5000,
            protocol=elbv2.ApplicationProtocol.HTTP,
            targets=[ecs_service],
            conditions=[elbv2.ListenerCondition.path_patterns(["/hello"])],
            priority=1,
        )

        codedeploy_service_role = self.createRole(
            "ECS-CICD-CodeDeployServiceRole",
            iam.ServicePrincipal("codedeploy.amazonaws.com"),
            [],
        )

        self.addManagedPolicy(
            codedeploy_service_role,
            "AWSCodeDeployRoleForECS",
        )

        # create an output with alb dns name
        CfnOutput(
            self,
            "ApplicationLoadBalancerDNSName",
            value=f"http://{alb.load_balancer_dns_name}",
        )

    def addManagedPolicy(self, role, policyName):
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(policyName)
        )

    def createRole(self, roleName, principal, policies):
        role = iam.Role(
            self,
            roleName,
            role_name=roleName,
            assumed_by=principal,
        )
        for policy in policies:
            policy.attach_to_role(role=role)

        return role

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy
