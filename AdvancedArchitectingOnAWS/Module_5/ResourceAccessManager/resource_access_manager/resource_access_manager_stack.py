from aws_cdk import Stack  # Duration,
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


class ResourceAccessManagerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a new VPC with Two subnets, one private and one public

        vpc = ec2.Vpc(
            self,
            "SharedVPC",
            vpc_name="SharedVPC",
            max_azs=1,
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC, name="PublicSubnet", cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    name="SharedPrivateSubnet",
                    cidr_mask=24,
                ),
            ],
            enable_dns_hostnames=True,
            enable_dns_support=True,
        )

        # create a security group for the VPC that allows all traffic from the VPC
        sg = ec2.SecurityGroup(
            self,
            "SharedSecurityGroup",
            vpc=vpc,
            allow_all_outbound=True,
            security_group_name="SharedSecurityGroup",
        )

        # add inbound rules to authorize http and https traffic
        sg.add_ingress_rule(
            peer=ec2.Peer.ipv4(vpc.vpc_cidr_block), connection=ec2.Port.tcp(80)
        )
        sg.add_ingress_rule(
            peer=ec2.Peer.ipv4(vpc.vpc_cidr_block), connection=ec2.Port.tcp(443)
        )
