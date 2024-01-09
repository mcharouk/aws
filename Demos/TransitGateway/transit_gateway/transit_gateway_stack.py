from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_ec2 as ec2  # Duration,; aws_sqs as sqs,
from constructs import Construct


class TransitGatewayStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a VPC with only one private subnet
        from aws_cdk import aws_ec2 as ec2
        from aws_cdk import aws_iam as iam

        # create a transit gateway with no tags and attach it to the VPC
        tgw = ec2.CfnTransitGateway(
            self,
            "TransitGateway",
            amazon_side_asn=64512,
            auto_accept_shared_attachments="enable",
            default_route_table_association="enable",
            default_route_table_propagation="enable",
            dns_support="enable",
            vpn_ecmp_support="enable",
        )

        # create a transit gateway route table and associate it with the VPC
        """ tgw_route_table = ec2.CfnTransitGatewayRouteTable(
            self,
            "TransitGatewayRouteTable",
            transit_gateway_id=tgw.ref
            # tags=[CfnTag(key="Name", value="TransitGatewayRouteTable")]
        ) """

        class VPCProperties:
            def __init__(self, name, cidr):
                self.name = name
                self.cidr = cidr

        vpcProperties = [
            VPCProperties("VPC-A", "10.0.0.0/24"),
            VPCProperties("VPC-B", "10.1.0.0/24"),
            VPCProperties("VPC-C", "10.2.0.0/24"),
        ]

        for vpcProperty in vpcProperties:
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

            # add a route to the vpc route table that targets transit gateway
            ec2.CfnRoute(
                self,
                "VPCRouteToTransitGateway-" + vpcProperty.name,
                route_table_id=vpc.isolated_subnets[0].route_table.route_table_id,
                destination_cidr_block="10.0.0.0/16",
                transit_gateway_id=tgw.ref,
            )

            ec2.CfnTransitGatewayAttachment(
                self,
                "TransitGatewayAttachment-" + vpcProperty.name,
                transit_gateway_id=tgw.ref,
                vpc_id=vpc.vpc_id,
                subnet_ids=[subnet.subnet_id for subnet in vpc.isolated_subnets],
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

            # create a security group for the instance with icmp allowed in inbound and outbound
            securityGroup = ec2.SecurityGroup(
                self,
                "SecurityGroup-" + vpcProperty.name,
                security_group_name="SecurityGroup-" + vpcProperty.name,
                description="Demo SecurityGroup",
                disable_inline_rules=True,
                vpc=vpc,
            )
            securityGroup.add_ingress_rule(
                peer=ec2.Peer.ipv4("0.0.0.0/0"),
                connection=ec2.Port.tcp(80),
                description="Allow all inbound http traffic",
            )

            securityGroup.add_ingress_rule(
                peer=ec2.Peer.ipv4("0.0.0.0/0"),
                connection=ec2.Port.tcp(443),
                description="Allow all inbound https traffic (for System Manager)",
            )

            securityGroup.add_ingress_rule(
                peer=ec2.Peer.ipv4("0.0.0.0/0"),
                connection=ec2.Port.all_icmp(),
                description="Allow all inbound icmp traffic",
            )

            # create an instance in vpc with session manager enabled
            instance_name = "TransitGatewayTestInstance-" + vpcProperty.name
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

            # create a security group for VPC Endpoints
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
                subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                ),
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
                subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                ),
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
                subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                ),
                private_dns_enabled=True,
                security_groups=[vpcEndpointSecurityGroup],
                open=True,
                lookup_supported_azs=False,
            )

            CfnOutput(
                self,
                instance_name + "-PrivateIp",
                value=instance.instance_private_ip,
            )
