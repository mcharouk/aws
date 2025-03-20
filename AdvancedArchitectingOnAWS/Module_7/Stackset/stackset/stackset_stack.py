from aws_cdk import CfnOutput, RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct


class StacksetStack(Stack):

    def uploadObject(self, bucket, prefix, file_name):
        s3deploy.BucketDeployment(
            self,
            f"S3Deployment-{prefix}",
            sources=[s3deploy.Source.asset(file_name)],
            destination_bucket=bucket,
            destination_key_prefix=prefix,
        )

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stackset_bucket_name = "aws-training-marccharouk-stackset"

        stackset_bucket = s3.Bucket(
            self,
            "stackset_bucket",
            bucket_name=stackset_bucket_name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        target_root_folder_template = "template"

        self.uploadObject(stackset_bucket, target_root_folder_template, "./template")

        CfnOutput(
            self,
            "template_url",
            value=f"https://{stackset_bucket.bucket_name}.s3.{self.region}.amazonaws.com/{target_root_folder_template}/sqs.yaml",
        )
