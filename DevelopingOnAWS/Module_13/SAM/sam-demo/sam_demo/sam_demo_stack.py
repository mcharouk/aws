from aws_cdk import RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_s3 as s3
from constructs import Construct


class SamDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = "marc-charouk-samdemo-576758948"

        s3.Bucket(
            self,
            bucket_name,
            bucket_name=bucket_name,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
