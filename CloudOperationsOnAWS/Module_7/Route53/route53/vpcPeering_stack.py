from aws_cdk import CfnOutput, Fn, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


class VpcPeeringStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        parisVpc: ec2.Vpc,
        irelandVpc: ec2.Vpc,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create peering connection
        self.peeringConnection = ec2.CfnVPCPeeringConnection(
            self,
            "VPCPeering",
            peer_vpc_id=irelandVpc.vpc_id,
            vpc_id=parisVpc.vpc_id,
            peer_region=irelandVpc.env.region,
        )
