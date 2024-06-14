from aws_cdk import CfnOutput, Fn, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


class VpcPeeringRouteStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        sourceVpc: ec2.Vpc,
        targetVpc: ec2.Vpc,
        peeringConnection: ec2.CfnVPCPeeringConnection,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        index = 0
        for isolated_subnet in sourceVpc.isolated_subnets:
            routeTableId = isolated_subnet.route_table.route_table_id
            ec2.CfnRoute(
                self,
                f"VPCPeeringRoute-{index}",
                route_table_id=routeTableId,
                destination_cidr_block=targetVpc.vpc_cidr_block,
                vpc_peering_connection_id=peeringConnection.attr_id,
            )
            index += 1
