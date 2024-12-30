import boto3
from aws_cdk import CfnOutput, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_certificatemanager as acm
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


class ClientVpnStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create vpc with a public subnet and a private subnet
        # create an internet gateway and attach it

        vpc = ec2.Vpc(
            self,
            "VPC",
            max_azs=1,
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            create_internet_gateway=True,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            vpc_name="client_vpn_demo",
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="private",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=24,
                ),
            ],
        )

        # create security group that allows all outbound traffic
        clientVpn_sg = ec2.SecurityGroup(
            self,
            "ClientVPNSecurityGroup",
            vpc=vpc,
            security_group_name="client_vpn_sg",
            description="Allow all outbound traffic",
            allow_all_outbound=True,
        )

        ec2_sg = ec2.SecurityGroup(
            self,
            "EC2SecurityGroup",
            vpc=vpc,
            security_group_name="ec2_sg",
            description="Allow all outbound traffic",
            allow_all_outbound=True,
        )

        # allow all icmp, http and https traffic from client vpn sg to ec2 sg
        ec2_sg.add_ingress_rule(
            peer=clientVpn_sg,
            connection=ec2.Port.all_icmp(),
            description="Allow all traffic from client vpn sg",
        )

        ec2_sg.add_ingress_rule(
            peer=clientVpn_sg,
            connection=ec2.Port.HTTP,
            description="Allow all traffic from client vpn sg",
        )

        ec2_sg.add_ingress_rule(
            peer=clientVpn_sg,
            connection=ec2.Port.HTTPS,
            description="Allow all traffic from client vpn sg",
        )

        # create an ec2 instance in a private subnet, t2.micro type
        # and associate it with the security group

        ec2_instance = ec2.Instance(
            self,
            "EC2Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            security_group=ec2_sg,
        )

        # Output ec2 private ip address
        CfnOutput(self, "EC2PrivateIP", value=ec2_instance.instance_private_ip)
