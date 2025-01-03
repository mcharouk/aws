from aws_cdk import (  # Duration,; aws_sqs as sqs,
    CfnOutput,
    Duration,
    RemovalPolicy,
    Stack,
)
from aws_cdk import aws_autoscaling as autoscaling
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import aws_iam as iam
from constructs import Construct


class EcsCapacityProvidersStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a VPC with a public subnet and a private subnet
        vpc = ec2.Vpc(
            self,
            "VPC",
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            vpc_name="ECS-VPC",
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

        ecs_instance_role = self.createRole(
            "ECSInstanceRole",
            iam.ServicePrincipal("ec2.amazonaws.com"),
            [],
        )

        self.addManagedPolicy(
            ecs_instance_role,
            "service-role/AmazonEC2ContainerServiceforEC2Role",
        )

        ecs_task_execution_role = self.createRole(
            "ECSTaskExecutionRoleDemo",
            iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            [],
        )

        self.addManagedPolicy(
            ecs_task_execution_role,
            "service-role/AmazonECSTaskExecutionRolePolicy",
        )

        # create a security group for ecs instances
        alb_sg = ec2.SecurityGroup(
            self,
            "ECSAlbSG",
            vpc=vpc,
            description="Allow http access for alb",
            allow_all_outbound=True,
            security_group_name="ECSAlbSG",
        )

        # allow http inbound from anywhere
        alb_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow http access from anywhere",
        )

        # create a security group for ecs service
        ecs_service_sg = ec2.SecurityGroup(
            self,
            "ECSServiceSG",
            vpc=vpc,
            description="Allow http access for ecs service",
            allow_all_outbound=True,
            security_group_name="ECSServiceSG",
        )

        # allow http inbound from alb sg
        ecs_service_sg.connections.allow_from(
            alb_sg,
            ec2.Port.tcp(5000),
            "Allow inbound connections on port 5000",
        )

        # create a security group for ecs instances
        ecs_instances_sg = ec2.SecurityGroup(
            self,
            "ECSInstancesSG",
            vpc=vpc,
            description="Allow http access to ec2 instances",
            allow_all_outbound=True,
            security_group_name="ECSInstancesSG",
        )

        ecs_cluster_name = "sample-app-cluster"
        user_data = ec2.UserData.for_linux()
        user_data.add_commands(
            "#!/bin/bash",
            f'echo "ECS_CLUSTER={ecs_cluster_name}" >> /etc/ecs/ecs.config',
            'echo "ECS_ENABLE_CONTAINER_METADATA=true" >> /etc/ecs/ecs.config',
        )

        # create an EC2 auto scaling group with an ECS optimized AMI
        asg = autoscaling.AutoScalingGroup(
            self,
            "ECSAutoScalingGroup",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO
            ),
            machine_image=ecs.EcsOptimizedImage.amazon_linux2(),  # Use ECS-optimized AMI
            min_capacity=1,
            max_capacity=1,
            desired_capacity=1,
            # Configure user data for ECS cluster integration
            user_data=user_data,
            block_devices=[
                autoscaling.BlockDevice(
                    device_name="/dev/xvda",
                    volume=autoscaling.BlockDeviceVolume.ebs(
                        volume_size=30,
                        volume_type=autoscaling.EbsDeviceVolumeType.GP3,
                        delete_on_termination=True,
                    ),
                )
            ],
            health_check=autoscaling.HealthCheck.ec2(grace=Duration.seconds(60)),
            security_group=ecs_instances_sg,
            role=ecs_instance_role,
            auto_scaling_group_name="ECSAutoScalingGroup",
        )

        # create a new capacity provider
        """ecs.AsgCapacityProvider(
            self,
            "AsgCapacityProvider",
            auto_scaling_group=asg,
            capacity_provider_name="AsgCapacityProvider",
        )"""

        # create an ECR repository
        repository_name = "capacity-provider-app"
        ecr.Repository(
            self,
            "ECRRepository",
            repository_name=repository_name,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # create an application load balancer
        alb = elbv2.ApplicationLoadBalancer(
            self,
            "ApplicationLoadBalancer",
            vpc=vpc,
            internet_facing=True,
            security_group=alb_sg,
            load_balancer_name="ECS-ALB",
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

        alb_listener = alb.add_listener(
            "ECSCapaProviderALBListener",
            port=80,
            protocol=elbv2.ApplicationProtocol.HTTP,
            default_action=elbv2.ListenerAction.fixed_response(
                status_code=200,
                content_type="application/json",
                message_body='{"status": "OK"}',
            ),
        )

        ecs_service_target_group = elbv2.ApplicationTargetGroup(
            self,
            "ECSServiceTargetGroup",
            vpc=vpc,
            port=5000,
            protocol=elbv2.ApplicationProtocol.HTTP,
            target_type=elbv2.TargetType.IP,
            target_group_name="ECSServiceTargetGroup",
        )

        # add rule to listener for path hello, target lambda function
        alb_listener.add_action(
            "ECSServiceHelloAction",
            action=elbv2.ListenerAction.forward(
                target_groups=[ecs_service_target_group]
            ),
            conditions=[elbv2.ListenerCondition.path_patterns(["/hello"])],
            priority=1,
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
