from aws_cdk import CfnOutput, Fn, Stack  # Duration,; aws_sqs as sqs,
from constructs import Construct


class VpcEndpointsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        class VPCProperties:
            def __init__(self, name, cidr):
                self.name = name
                self.cidr = cidr

        vpcProperty = VPCProperties("VPC-Endpoints", "10.3.0.0/24")

        # The code that defines your stack goes here
        from aws_cdk import aws_ec2 as ec2
        from aws_cdk import aws_iam as iam

        vpc = ec2.Vpc(
            self,
            vpcProperty.name,
            ip_addresses=ec2.IpAddresses.cidr(vpcProperty.cidr),
            max_azs=1,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=28,
                    name="PrivateSubnet",
                )
            ],
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux2023()

        role = iam.Role(
            self,
            "InstanceSSM" + vpcProperty.name,
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSQSFullAccess")
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
        )

        securityGroup = ec2.SecurityGroup(
            self,
            "EC2-" + vpcProperty.name,
            security_group_name="EC2-" + vpcProperty.name,
            description="EC2 SecurityGroup",
            disable_inline_rules=True,
            vpc=vpc,
        )

        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(443),
            description="Allow all inbound https traffic (for System Manager)",
        )

        instance_name = "VPCEndpointTestInstance-" + vpcProperty.name
        instance = ec2.Instance(
            self,
            instance_name,
            instance_name=instance_name,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            machine_image=amzn_linux,
            vpc=vpc,
            role=role,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            security_group=securityGroup,
        )

        vpcEndpointSecurityGroup = ec2.SecurityGroup(
            self,
            "SecurityGroupVpcEndpoint-" + vpcProperty.name,
            security_group_name="SecurityGroupVpcEndpoint-" + vpcProperty.name,
            description="Demo SecurityGroup",
            disable_inline_rules=True,
            vpc=vpc,
        )
        vpcEndpointSecurityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(443),
            description="Allow all inbound https traffic",
        )

        # create VPC Endpoint for SSM
        ec2.InterfaceVpcEndpoint(
            self,
            "VpcEndpointSsm-" + vpcProperty.name,
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.SSM,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            private_dns_enabled=True,
            security_groups=[vpcEndpointSecurityGroup],
            open=True,
            lookup_supported_azs=False,
        )

        ec2.InterfaceVpcEndpoint(
            self,
            "VpcEndpointSsmMessages-" + vpcProperty.name,
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.SSM_MESSAGES,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            private_dns_enabled=True,
            security_groups=[vpcEndpointSecurityGroup],
            open=True,
            lookup_supported_azs=False,
        )

        # create VPC Endpoint for EC2
        ec2.InterfaceVpcEndpoint(
            self,
            "VpcEndpointEc2-" + vpcProperty.name,
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.EC2_MESSAGES,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            private_dns_enabled=True,
            security_groups=[vpcEndpointSecurityGroup],
            open=True,
            lookup_supported_azs=False,
        )

        # create VPC Endpoint for SQS
        sqsInterfaceEndpoint = ec2.InterfaceVpcEndpoint(
            self,
            "VpcEndpointSqs-" + vpcProperty.name,
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.SQS,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            private_dns_enabled=False,
            security_groups=[vpcEndpointSecurityGroup],
            open=True,
            lookup_supported_azs=False,
        )

        vpc.add_gateway_endpoint(
            "s3GatewayEndpoint", service=ec2.GatewayVpcEndpointAwsService.S3
        )

        i = 0
        nb_dns_entries = len(sqsInterfaceEndpoint.vpc_endpoint_dns_entries)
        print(
            "creating {nb_dns_entries} dns entries".format(
                nb_dns_entries=nb_dns_entries
            )
        )
        while i < nb_dns_entries:
            CfnOutput(
                self,
                "sqsInterfaceEndpointDnsName-" + str(i),
                value=Fn.select(i, sqsInterfaceEndpoint.vpc_endpoint_dns_entries),
            )
            i += 1
