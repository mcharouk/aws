import os

import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import CfnOutput
from aws_cdk.aws_s3_assets import Asset
from constructs import Construct

dirname = os.path.dirname(__file__)


class VpcSecurityStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self,
            "VpcSecurityStack",
            vpc_name="VpcSecurityDemo",
            enable_dns_hostnames=True,
            enable_dns_support=True,
            ip_addresses=ec2.IpAddresses.cidr("192.168.0.0/28"),
            max_azs=1,
            create_internet_gateway=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PublicSubnet", subnet_type=ec2.SubnetType.PUBLIC
                )
            ],
            nat_gateways=0,
        )

        networkAcl = ec2.NetworkAcl(
            self,
            "PublicNetworkAcl",
            network_acl_name="VPCSecurityDemo-PublicNetworkAcl",
            vpc=vpc,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

        ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryIngressHTTP",
            network_acl=networkAcl,
            rule_number=100,
            direction=ec2.TrafficDirection.INGRESS,
            network_acl_entry_name="Allow All Traffic",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.all_traffic(),
            rule_action=ec2.Action.ALLOW,
        )

        """ ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryIngressHTTP",
            network_acl=networkAcl,
            rule_number=101,
            direction=ec2.TrafficDirection.INGRESS,
            network_acl_entry_name="Allow HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(80),
            rule_action=ec2.Action.ALLOW,
        )

        ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryEgressEphemeralPorts",
            network_acl=networkAcl,
            rule_number=100,
            direction=ec2.TrafficDirection.EGRESS,
            network_acl_entry_name="Allow HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port_range(32768, 61000),
            rule_action=ec2.Action.ALLOW,
        ) """

        # add network acl entry that allow all outbound traffic
        ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryEgressHTTP",
            network_acl=networkAcl,
            rule_number=101,
            direction=ec2.TrafficDirection.EGRESS,
            network_acl_entry_name="Allow All Traffic",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.all_traffic(),
            rule_action=ec2.Action.ALLOW,
        )

        securityGroup = ec2.SecurityGroup(
            self,
            "VPCSecurityDemo-SecurityGroup",
            vpc=vpc,
            allow_all_outbound=True,
            security_group_name="VPCSecurityDemo-SecurityGroup",
            description="VPCSecurityDemo SecurityGroup",
            disable_inline_rules=True,
        )

        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )

        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(443),
            description="Allow all inbound https traffic (SystemManager)",
        )

        # create a security group for VPC Endpoints
        vpcEndpointSecurityGroup = ec2.SecurityGroup(
            self,
            "SecurityGroupVpcEndpoint-VPCSecurity",
            security_group_name="SecurityGroupVpcEndpoint-VPCSecurity",
            description="Demo SecurityGroup For VPC Endpoints",
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
            "VpcEndpointSsm-VPCSecurity",
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.SSM,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            private_dns_enabled=True,
            security_groups=[vpcEndpointSecurityGroup],
            open=True,
            lookup_supported_azs=False,
        )

        ec2.InterfaceVpcEndpoint(
            self,
            "VpcEndpointSsmMessages--VPCSecurity",
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.SSM_MESSAGES,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            private_dns_enabled=True,
            security_groups=[vpcEndpointSecurityGroup],
            open=True,
            lookup_supported_azs=False,
        )

        # create VPC Endpoint for EC2
        ec2.InterfaceVpcEndpoint(
            self,
            "VpcEndpointEc2--VPCSecurity",
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.EC2_MESSAGES,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            private_dns_enabled=True,
            security_groups=[vpcEndpointSecurityGroup],
            open=True,
            lookup_supported_azs=False,
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux2023()

        role = iam.Role(
            self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        with open("./vpc_security/configure.sh") as f:
            user_data = f.read()

        instance = ec2.Instance(
            self,
            "VPCSecurityInstanceDemo",
            instance_name="VPCSecurityInstanceDemo",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            associate_public_ip_address=True,
            vpc=vpc,
            machine_image=amzn_linux,
            role=role,
            security_group=securityGroup,
            user_data=ec2.UserData.custom(user_data),
        )

        # add public DNS of instance as cfn output
        CfnOutput(
            self,
            "InstancePublicDNS",
            value="http://" + instance.instance_public_dns_name,
        )
