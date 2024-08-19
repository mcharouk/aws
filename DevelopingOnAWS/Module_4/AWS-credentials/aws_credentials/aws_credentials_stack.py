from aws_cdk import CfnOutput, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from aws_cdk import aws_secretsmanager as secretsmanager
from constructs import Construct


class AwsCredentialsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create an iam role that has dynamodb full access managed policy
        dynamodbFullAccessRole = iam.Role(
            self,
            "DynamodbFullAccessRole",
            assumed_by=iam.AccountRootPrincipal(),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonDynamoDBFullAccess"
                )
            ],
            role_name="DynamodbFullAccessRole",
            description="Role with DynamoDB full access",
        )

        # create an iam user who has sqs full access managed policy
        sqsFullAccessUser = iam.User(
            self,
            "SqsAdmin",
            user_name="SqsAdmin",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSQSFullAccess")
            ],
        )

        sqsFullAccessUser.attach_inline_policy(
            iam.Policy(
                self,
                "StsAssumeRoleDDB",
                statements=[
                    iam.PolicyStatement(
                        effect=iam.Effect.ALLOW,
                        actions=["sts:AssumeRole"],
                        resources=[dynamodbFullAccessRole.role_arn],
                    )
                ],
            )
        )

        # create an access key for user sqsFullAccessUser
        accessKeyForSqsFullAccessUser = iam.AccessKey(
            self,
            "AccessKeyForSqsFullAccessUser",
            user=sqsFullAccessUser,
        )

        snsFullAccessUser = iam.User(
            self,
            "Sns",
            user_name="SnsAdmin",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSNSFullAccess")
            ],
        )

        accessKeyForSnsFullAccessUser = iam.AccessKey(
            self,
            "AccessKeyForSnsFullAccessUser",
            user=snsFullAccessUser,
        )

        # create a secret and put secret access key in it
        secretsmanager.Secret(
            self,
            "SecretAccessKeyForSqsFullAccessUser",
            secret_name="SqsAdmin-SecretAccessKey",
            secret_string_value=accessKeyForSqsFullAccessUser.secret_access_key,
        )

        secretsmanager.Secret(
            self,
            "SecretAccessKeyForSnsFullAccessUser",
            secret_name="SnsAdmin-SecretAccessKey",
            secret_string_value=accessKeyForSnsFullAccessUser.secret_access_key,
        )

        CfnOutput(self, "DynamoDBRoleARN", value=dynamodbFullAccessRole.role_arn)
        CfnOutput(
            self,
            "sqsAdmin-AccessKeyId",
            value=accessKeyForSqsFullAccessUser.access_key_id,
        )
        CfnOutput(
            self,
            "snsAdmin-AccessKeyId",
            value=accessKeyForSnsFullAccessUser.access_key_id,
        )
