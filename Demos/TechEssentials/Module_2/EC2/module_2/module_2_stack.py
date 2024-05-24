import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from constructs import Construct


class Module2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a vpc with only one private subnet
        from aws_cdk import aws_ec2 as ec2

        vpc_name = "ComputeDemo"
        private_subnet = ec2.SubnetConfiguration(
            name="Private", subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
        )
        vpc = ec2.Vpc(
            self,
            "ComputeDemo",
            vpc_name=vpc_name,
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            nat_gateways=0,
            max_azs=1,
            create_internet_gateway=False,
            subnet_configuration=[private_subnet],
            enable_dns_hostnames=True,
            enable_dns_support=True,
        )

        self.create_ec2_security_group(vpc)
        self.create_ssm_vpc_endpoint(vpc, vpc_name, subnet=private_subnet)

        # create a security group for an EC2 instance that can connect to the VPC interface endpoint

        # an EC2 instance role that has systems manager access permissions
        role = self.create_ec2_role_instance()

    def create_ec2_security_group(self, vpc):
        securityGroup = ec2.SecurityGroup(
            self,
            "SecurityGroupEC2Instance",
            security_group_name="SecurityGroupEC2Instance",
            description="Demo EC2 Instance SecurityGroup",
            vpc=vpc,
        )
        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )

    def create_ec2_role_instance(self):
        role = iam.Role(
            self,
            "RoleEC2Instance",
            role_name="RoleEC2Instance",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        instance_profile = iam.CfnInstanceProfile(
            self, "EC2InstanceProfile", roles=[role.role_name]
        )

        return role

    def create_ssm_vpc_endpoint(self, vpc, vpc_name, subnet):

        vpcEndpointSecurityGroup = ec2.SecurityGroup(
            self,
            "SecurityGroupVpcEndpoint-" + vpc_name,
            security_group_name="SecurityGroupVpcEndpoint-" + vpc_name,
            description="Demo VPC Endpoint SecurityGroup",
            disable_inline_rules=True,
            allow_all_outbound=True,
            vpc=vpc,
        )
        vpcEndpointSecurityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )

        ec2.InterfaceVpcEndpoint(
            self,
            "VpcEndpointSsm-" + vpc_name,
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
            "VpcEndpointSsmMessages-" + vpc_name,
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
            "VpcEndpointEc2-" + vpc_name,
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.EC2_MESSAGES,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            private_dns_enabled=True,
            security_groups=[vpcEndpointSecurityGroup],
            open=True,
            lookup_supported_azs=False,
        )
