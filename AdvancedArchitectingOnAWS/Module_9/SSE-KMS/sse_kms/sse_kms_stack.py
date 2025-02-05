from aws_cdk import Stack
from aws_cdk import aws_iam as iam  # Duration,; aws_sqs as sqs,
from constructs import Construct


class SseKmsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        role_name = "S3Administrator"
        # create a role that can be assumed that any principal of account
        # attach the managed policy that give admin access to s3

        iam.Role(
            self,
            "s3_admin_role",
            assumed_by=iam.AccountPrincipal(self.account),
            role_name=role_name,
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
            ],
        )
