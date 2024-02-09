import os

import aws_cdk.aws_ec2 as ec2
from aws_cdk import CfnOutput, Stack  # Duration,; aws_sqs as sqs,
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
            network_acl_entry_name="Allow http port for webapp",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(80),
            rule_action=ec2.Action.ALLOW,
        )

        ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryIngressEphemeralPorts",
            network_acl=networkAcl,
            rule_number=101,
            direction=ec2.TrafficDirection.INGRESS,
            network_acl_entry_name="Allow all traffic on ephemeral ports for yum update response",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            rule_action=ec2.Action.ALLOW,
        )

        # add network acl entry that allow all outbound traffic
        ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryEgressEphemeralPorts",
            network_acl=networkAcl,
            rule_number=101,
            direction=ec2.TrafficDirection.EGRESS,
            network_acl_entry_name="Allow all traffic on ephemeral ports for webapp response",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            rule_action=ec2.Action.ALLOW,
        )

        ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryEgressFTP",
            network_acl=networkAcl,
            rule_number=102,
            direction=ec2.TrafficDirection.EGRESS,
            network_acl_entry_name="Allow ftp traffic for yum update",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port_range(20, 21),
            rule_action=ec2.Action.ALLOW,
        )

        ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryEgressHTTP",
            network_acl=networkAcl,
            rule_number=103,
            direction=ec2.TrafficDirection.EGRESS,
            network_acl_entry_name="Allow http traffic for yum update",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(80),
            rule_action=ec2.Action.ALLOW,
        )

        ec2.NetworkAclEntry(
            self,
            "VPCSecurityDemo-NetworkAclEntryEgressHTTPS",
            network_acl=networkAcl,
            rule_number=104,
            direction=ec2.TrafficDirection.EGRESS,
            network_acl_entry_name="Allow https traffic for yum update",
            cidr=ec2.AclCidr.any_ipv4(),
            traffic=ec2.AclTraffic.tcp_port(443),
            rule_action=ec2.Action.ALLOW,
        )

        securityGroup = ec2.SecurityGroup(
            self,
            "VPCSecurityDemo-SecurityGroup",
            vpc=vpc,
            allow_all_outbound=False,
            security_group_name="VPCSecurityDemo-SecurityGroup",
            description="VPCSecurityDemo SecurityGroup",
            disable_inline_rules=True,
        )

        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )

        securityGroup.add_egress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all outbound http traffic for yum update",
        )

        securityGroup.add_egress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(443),
            description="Allow all outbound https traffic for yum update",
        )

        securityGroup.add_egress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp_range(20, 21),
            description="Allow all outbound ftp traffic for yum update",
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux2023()

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
            security_group=securityGroup,
            user_data=ec2.UserData.custom(user_data),
        )

        # add public DNS of instance as cfn output
        CfnOutput(
            self,
            "InstancePublicDNS",
            value="http://" + instance.instance_public_dns_name,
        )
