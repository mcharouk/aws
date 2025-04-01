from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import aws_elasticloadbalancingv2_targets as elbv2_targets
from aws_cdk import aws_iam as iam  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


# create a class called VpcConfig with member target_vpc, nlb_sg, alb_sg, lambda_sg, alb_listener_port
class VpcConfig:
    def __init__(
        self, target_vpc, client_vpc, nlb_sg, alb_sg, lambda_sg, alb_listener_port
    ):
        self.target_vpc = target_vpc
        self.client_vpc = client_vpc
        self.nlb_sg = nlb_sg
        self.alb_sg = alb_sg
        self.lambda_sg = lambda_sg
        self.alb_listener_port = alb_listener_port


class PrivateLinkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc_config = self.create_target_vpc_config()

        alb = self.create_producer_api(vpc_config=vpc_config)

        self.create_nlb(vpc_config=vpc_config, alb=alb)

        private_link_endpoint_sg = self.create_client_instance(
            vpc=vpc_config.client_vpc
        )

        CfnOutput(
            self,
            "ClientVPCId",
            value=vpc_config.client_vpc.vpc_id,
        )

        CfnOutput(
            self,
            "PrivateLinkEndpointSgId",
            value=private_link_endpoint_sg.security_group_id,
        )

        # write the region name to a local json file
        # overwrite the file if it exists
        # the file name is region.json
        # the file content is {"region": "region_name"}
        import json

        with open("region.json", "w") as f:
            f.write(json.dumps({"region": Stack.of(self).region}))

    def create_target_vpc_config(self):
        target_vpc = ec2.Vpc(
            self,
            "PrivateLinkTargetVPC",
            vpc_name="PrivateLinkTargetVPC",
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PrivateSubnet",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=24,
                )
            ],
            enable_dns_hostnames=True,
            enable_dns_support=True,
        )

        client_vpc = ec2.Vpc(
            self,
            "PrivateLinkClientVPC",
            vpc_name="PrivateLinkClientVPC",
            ip_addresses=ec2.IpAddresses.cidr("10.0.1.0/16"),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PrivateSubnet",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=24,
                )
            ],
            enable_dns_hostnames=True,
            enable_dns_support=True,
        )

        # create a security group for network load balancer that allow inbound connections on HTTP port
        nlb_sg = ec2.SecurityGroup(
            self,
            "NLBSecurityGroup",
            vpc=target_vpc,
            allow_all_outbound=True,
            security_group_name="NLBSecurityGroup",
        )
        nlb_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.HTTP,
            description="Allow HTTP from anywhere",
        )

        # create a security group for application load balancer that allow inbound connections on HTTP port
        alb_sg = ec2.SecurityGroup(
            self,
            "ALBSecurityGroup",
            vpc=target_vpc,
            allow_all_outbound=True,
            security_group_name="ALBSecurityGroup",
        )
        alb_sg.add_ingress_rule(
            peer=ec2.Peer.security_group_id(nlb_sg.security_group_id),
            connection=ec2.Port.HTTP,
            description="Allow HTTP from NLB Security Group",
        )

        lambda_sg = ec2.SecurityGroup(
            self,
            "LambdaSecurityGroup",
            vpc=target_vpc,
            allow_all_outbound=False,
            security_group_name="LambdaSecurityGroup",
        )
        lambda_sg.add_ingress_rule(
            peer=ec2.Peer.security_group_id(alb_sg.security_group_id),
            connection=ec2.Port.HTTP,
            description="Allow HTTP from ALB Security Group",
        )
        return VpcConfig(
            target_vpc=target_vpc,
            client_vpc=client_vpc,
            nlb_sg=nlb_sg,
            alb_sg=alb_sg,
            lambda_sg=lambda_sg,
            alb_listener_port=80,
        )

    def create_producer_api(self, vpc_config: VpcConfig):
        helloForPrivateLink_lambda_role = self.createRole(
            "HelloForPrivateLinkLambdaRole",
            iam.ServicePrincipal("lambda.amazonaws.com"),
            [],
        )

        self.addManagedPolicy(
            helloForPrivateLink_lambda_role,
            "service-role/AWSLambdaVPCAccessExecutionRole",
        )

        hello_lambda = _lambda.Function(
            self,
            id="HelloForPrivateLink",
            function_name="HelloForPrivateLink",
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("lambda"),
            handler="lambda_function.lambda_handler",
            role=helloForPrivateLink_lambda_role,
            vpc=vpc_config.target_vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            security_groups=[vpc_config.lambda_sg],
        )

        # create a private application load balancer that has lambda as a target

        alb = elbv2.ApplicationLoadBalancer(
            self,
            "PrivateLinkALB",
            load_balancer_name="PrivateLinkALB",
            vpc=vpc_config.target_vpc,
            internet_facing=False,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            security_group=vpc_config.alb_sg,
        )
        alb_listener = alb.add_listener(
            "PrivateLinkALBListener",
            port=vpc_config.alb_listener_port,
            protocol=elbv2.ApplicationProtocol.HTTP,
            default_action=elbv2.ListenerAction.fixed_response(
                status_code=200,
                content_type="application/json",
                message_body='{"status": "OK"}',
            ),
        )

        lambda_target_group = elbv2.ApplicationTargetGroup(
            self,
            "LambdaTargetGroup",
            target_type=elbv2.TargetType.LAMBDA,
            targets=[elbv2_targets.LambdaTarget(hello_lambda)],
        )

        # add rule to listener for path hello, target lambda function
        alb_listener.add_action(
            "PrivateLinkALBHelloAction",
            action=elbv2.ListenerAction.forward(target_groups=[lambda_target_group]),
            conditions=[elbv2.ListenerCondition.path_patterns(["/hello"])],
            priority=1,
        )

        return alb

    def create_client_instance(self, vpc: ec2.Vpc):

        # create interface endpoint for session manager
        vpc.add_interface_endpoint(
            "SSMEndpoint_targetVPC", service=ec2.InterfaceVpcEndpointAwsService.SSM
        )
        vpc.add_interface_endpoint(
            "SSMMessagesEndpoint_targetVPC",
            service=ec2.InterfaceVpcEndpointAwsService.SSM_MESSAGES,
        )
        vpc.add_interface_endpoint(
            "EC2MessagesEndpoint_targetVPC",
            service=ec2.InterfaceVpcEndpointAwsService.EC2_MESSAGES,
        )

        # create a role for an ec2 instance that has systems manager default policy
        privatelink_ec2_target_vpc_role = self.createRole(
            "PrivateLinkEC2TargetVPCRole",
            iam.ServicePrincipal("ec2.amazonaws.com"),
            [],
        )
        self.addManagedPolicy(
            privatelink_ec2_target_vpc_role, "AmazonSSMManagedInstanceCore"
        )

        # create a security group
        ec2_security_group = ec2.SecurityGroup(
            self,
            "PrivateLinkClientInstanceSG",
            vpc=vpc,
            description="Security Group of client instance",
            allow_all_outbound=True,
            security_group_name="PrivateLinkClientInstanceSG",
        )

        # create a security group
        private_link_endpoint_sg = ec2.SecurityGroup(
            self,
            "PrivateLinkEndpointSG",
            vpc=vpc,
            description="Security Group of private link interface endpoint",
            allow_all_outbound=True,
            security_group_name="PrivateLinkEndpointSG",
        )

        # add inbound rule to authorize HTTP calls from ec2 security group
        private_link_endpoint_sg.add_ingress_rule(
            peer=ec2.Peer.security_group_id(ec2_security_group.security_group_id),
            connection=ec2.Port.HTTP,
            description="Allow HTTP from ec2 Security Group",
        )

        # create an EC2 instance with t2.micro as instance type
        ec2.Instance(
            self,
            "PrivateLinkTargetVPCInstance",
            instance_name="PrivateLinkTargetVPCInstance",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            role=privatelink_ec2_target_vpc_role,
            security_group=ec2_security_group,
        )

        return private_link_endpoint_sg

    def create_nlb(self, vpc_config: VpcConfig, alb: elbv2.ApplicationLoadBalancer):

        # create a target group that points load balancer arn
        target_group = elbv2.NetworkTargetGroup(
            self,
            "PrivateLinkTargetGroup",
            target_group_name="PrivateLinkTargetGroup",
            vpc=vpc_config.target_vpc,
            port=vpc_config.alb_listener_port,
            protocol=elbv2.Protocol.TCP,
            target_type=elbv2.TargetType.ALB,
        )

        target_group.add_target(
            elbv2_targets.AlbListenerTarget(
                alb_listener=alb.listeners[0],  # Reference to the ALB listener
            )
        )

        # create a network load balancer that points to the target group
        nlb = elbv2.NetworkLoadBalancer(
            self,
            "PrivateLinkNLB",
            load_balancer_name="PrivateLinkNLB",
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            vpc=vpc_config.target_vpc,
            internet_facing=False,
            cross_zone_enabled=True,
            enforce_security_group_inbound_rules_on_private_link_traffic=True,
            security_groups=[vpc_config.nlb_sg],
        )
        nlb.add_listener(
            "PrivateLinkNLBListener",
            port=vpc_config.alb_listener_port,
            protocol=elbv2.Protocol.TCP,
            default_target_groups=[target_group],
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
