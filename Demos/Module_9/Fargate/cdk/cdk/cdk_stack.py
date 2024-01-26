import aws_cdk.aws_ec2 as ec2
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a security group in the default vpc
        sg = ec2.SecurityGroup(
            self,
            "SecurityGroup",
            vpc=ec2.Vpc.from_lookup(self, "VPC", is_default=True),
            allow_all_outbound=True,
            description="Fargate Demo Security Group",
        )
        sg.add_ingress_rule(
            ec2.Peer.ipv4("0.0.0.0/0"), ec2.Port.tcp(5000), "Allow only port 5000"
        )
