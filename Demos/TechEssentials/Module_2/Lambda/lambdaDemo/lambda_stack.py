from zipfile import ZipFile

import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_iam as iam
import aws_cdk.aws_sqs as sqs
from aws_cdk import (  # Duration,; aws_sqs as sqs,
    CfnOutput,
    Duration,
    RemovalPolicy,
    Stack,
)
from aws_cdk import aws_s3_assets as s3a
from constructs import Construct
from lambdaDemo.StackConfig import StackConfig


class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stackConfig = StackConfig()

        # create a sqs standard queue
        sqs.Queue(
            self,
            "LambdaDemoQueue",
            visibility_timeout=Duration.seconds(300),
            queue_name=stackConfig.sqsQueueName,
        )

        # create a dynamodb table named Organizations with partition key named index as type Number
        dynamodb.Table(
            self,
            "OrganizationsTable",
            partition_key=dynamodb.Attribute(
                name=stackConfig.dynamoDBPartitionKey,
                type=dynamodb.AttributeType.NUMBER,
            ),
            table_name=stackConfig.dynamoDBTableName,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # create an iam role for lambda function that can read from an sqs queue and write in dynamoDB
        role = iam.Role(
            self,
            "LambdaRole",
            role_name="LambdaDemoRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        dynamodbPolicy = self.createDynamoDBPolicy(stackConfig=stackConfig)
        dynamodbPolicy.attach_to_role(role=role)

        # attach AWSLambdaSQSQueueExecutionRole managed policy to role
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "service-role/AWSLambdaSQSQueueExecutionRole"
            )
        )

        self.upload_lambda_code()

    def createDynamoDBPolicy(self, stackConfig):
        dynamoDBPolicyStatement = iam.PolicyStatement(
            sid="DynamoDBPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=[
                "dynamodb:BatchWriteItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
            ],
            resources=[
                "arn:aws:dynamodb:{region}:{accountId}:table/{tableName}".format(
                    region=stackConfig.region,
                    accountId=stackConfig.accountId,
                    tableName=stackConfig.dynamoDBTableName,
                )
            ],
        )

        dynamodbPolicy = iam.Policy(
            self,
            "DynamoDBIdentityBasedPolicy",
            statements=[dynamoDBPolicyStatement],
        )
        return dynamodbPolicy

    def upload_lambda_code(self):
        lambda_code_rel_path = "lambda_function/techEssentials-module2-lambda-code.zip"
        with ZipFile(lambda_code_rel_path, "w") as zip_object:
            # Adding files that need to be zipped
            zip_object.write(
                filename="lambda_function/lambda_function.py",
                arcname="lambda_function.py",
            )

        asset = s3a.Asset(
            self, "TechEssentialsModule2LambdaCode", path=lambda_code_rel_path
        )

        CfnOutput(
            self,
            "s3_url_lambdacode",
            value=asset.s3_object_url,
        )
