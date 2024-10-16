from aws_cdk import CfnOutput, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from aws_cdk import aws_secretsmanager as secretsmanager
from constructs import Construct


class CredentialsPriorityStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        john_foo_user_name = "john.foo"
        johnFooUser = iam.User(
            self,
            john_foo_user_name,
            user_name=john_foo_user_name,
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSQSFullAccess")
            ],
        )

        accessKeyForJohnFooUser = iam.AccessKey(
            self,
            "AccessKeyForJohnFooUser",
            user=johnFooUser,
        )

        secretsmanager.Secret(
            self,
            "SecretAccessKeyForJohnFooUser",
            secret_name="JohnFoo-SecretAccessKey",
            secret_string_value=accessKeyForJohnFooUser.secret_access_key,
        )

        s3_admin_role_name = "S3AdminRole"
        # create role with S3 Full access
        s3FullAccessRole = iam.Role(
            self,
            "S3FullAccessRole",
            assumed_by=iam.AccountRootPrincipal(),
            role_name=s3_admin_role_name,
            description="Role with S3 full access",
        )

        CfnOutput(
            self,
            "JohnFooAccessKeyId",
            value=accessKeyForJohnFooUser.access_key_id,
        )

        CfnOutput(
            self,
            "S3AdminRoleArn",
            value=s3FullAccessRole.role_arn,
        )
