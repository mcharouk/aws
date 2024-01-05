import os

import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk.aws_s3_assets import Asset
from constructs import Construct

dirname = os.path.dirname(__file__)


class VpcSecurityStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        subnet = ec2.SubnetConfiguration(
            name="PublicSubnet",
            subnet_type=ec2.SubnetType.PUBLIC,
        )

        vpc = ec2.Vpc(
            self,
            "VpcSecurityStack",
            vpc_name="VpcSecurityDemo",
            enable_dns_hostnames=True,
            enable_dns_support=True,
            cidr="192.168.0.0/28",
            max_azs=1,
            create_internet_gateway=True,
            subnet_configuration=[subnet],
            nat_gateways=0,
        )

        networkAcl = ec2.NetworkAcl(
            self,
            "PublicNetworkAcl",
            network_acl_name="PublicNetworkAcl",
            vpc=vpc,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

        ec2.NetworkAclEntry(
            self,
            "NetworkAclEntryIngress",
            network_acl=networkAcl,
            rule_number=100,
            direction=ec2.TrafficDirection.INGRESS,
            network_acl_entry_name="Allow HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(80),
            rule_action=ec2.Action.ALLOW,
        )

        ec2.NetworkAclEntry(
            self,
            "NetworkAclEntryEgress",
            network_acl=networkAcl,
            rule_number=100,
            direction=ec2.TrafficDirection.EGRESS,
            network_acl_entry_name="Allow HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port_range(32768, 61000),
            rule_action=ec2.Action.ALLOW,
        )

        securityGroup = ec2.SecurityGroup(
            self,
            "SecurityGroup",
            vpc=vpc,
            allow_all_outbound=False,
            security_group_name="SecurityGroup",
            description="Demo SecurityGroup",
            disable_inline_rules=True,
        )

        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023,
            edition=ec2.AmazonLinuxEdition.STANDARD,
        )

        role = iam.Role(
            self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        instance = ec2.Instance(
            self,
            "InstanceDemo",
            instance_name="InstanceDemo",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            associate_public_ip_address=True,
            vpc=vpc,
            machine_image=amzn_linux,
            role=role,
            security_group=securityGroup,
        )

        asset = Asset(self, "Asset", path=os.path.join(dirname, "configure.sh"))
        local_path = instance.user_data.add_s3_download_command(
            bucket=asset.bucket, bucket_key=asset.s3_object_key
        )

        instance.user_data.add_execute_file_command(file_path=local_path)
        asset.grant_read(instance.role)
