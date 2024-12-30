from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_ec2 as ec2  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_networkmanager as nm
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

        class VPCProperties:
            def __init__(self, name, cidr):
                self.name = name
                self.cidr = cidr

        vpcProperties = [
            VPCProperties("VPC-A", "10.0.0.0/24"),
            VPCProperties("VPC-B", "10.1.0.0/24"),
            VPCProperties("VPC-C", "10.2.0.0/24"),
        ]

        def createVPC(vpcProperty):
            return ec2.Vpc(
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

        def generate_outputs(vpcProperty, vpc):
            CfnOutput(
                self,
                "VPC-Id-" + vpcProperty.name,
                value=vpc.vpc_id,
            )

            CfnOutput(
                self,
                "VPC-CidrBlock-" + vpcProperty.name,
                value=vpc.vpc_cidr_block,
            )

        tgw_attachements = []
        for vpcProperty in vpcProperties:
            vpc = createVPC(vpcProperty=vpcProperty)

            tgw_attachment = ec2.CfnTransitGatewayAttachment(
                self,
                "TransitGatewayAttachment-" + vpcProperty.name,
                transit_gateway_id=tgw.ref,
                vpc_id=vpc.vpc_id,
                subnet_ids=[subnet.subnet_id for subnet in vpc.isolated_subnets],
            )
            tgw_attachements.append(tgw_attachment)

            # add a route to the vpc route table that targets transit gateway
            route = ec2.CfnRoute(
                self,
                "VPCRouteToTransitGateway-" + vpcProperty.name,
                route_table_id=vpc.isolated_subnets[0].route_table.route_table_id,
                destination_cidr_block="10.0.0.0/8",
                transit_gateway_id=tgw.ref,
            )

            route.node.add_dependency(tgw_attachment)

            generate_outputs(vpcProperty, vpc)

        # create a global network in network manager
        global_network = nm.CfnGlobalNetwork(
            self,
            "GlobalNetwork",
            description="My Global Network",
        )

        # register transit gateway
        tgwRegistration = nm.CfnTransitGatewayRegistration(
            self,
            "TransitGatewayRegistration",
            global_network_id=global_network.attr_id,
            transit_gateway_arn=tgw.attr_transit_gateway_arn,
        )
        for tgw_attachment in tgw_attachements:
            tgwRegistration.node.add_dependency(tgw_attachment)
