from zipfile import ZipFile

import boto3
import yaml
from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_dynamodb as ddb
from aws_cdk import aws_iam as iam  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_event_sources as _lambda_es
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_assets as s3a
from aws_cdk import aws_s3_notifications as s3n
from cdk.StackConfig import StackConfig
from constructs import Construct


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stackConfig = StackConfig()

        # create an iam role assumed by lambda and attach the policy
        role = iam.Role(
            self,
            "LambdaRole",
            role_name="DynamoDBLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        dynamoDBPolicyStatement = iam.PolicyStatement(
            sid="DynamoDBPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=[
                "dynamodb:BatchGetItem",
                "dynamodb:GetItem",
                "dynamodb:Query",
                "dynamodb:Scan",
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

        # create an identity based policy that allows read and write from dynamodb
        dynamodbPolicy = iam.Policy(
            self,
            "DynamoDBIdentityBasedPolicy",
            statements=[dynamoDBPolicyStatement],
        )

        dynamodbPolicy.attach_to_role(role=role)

        cloudwatchPolicyLogGroupStatement = iam.PolicyStatement(
            sid="CloudWatchLogGroupForLambdaPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=["logs:CreateLogGroup"],
            resources=[
                "arn:aws:logs:{region}:{accountId}:*".format(
                    region=stackConfig.region, accountId=stackConfig.accountId
                )
            ],
        )

        cloudwatchPolicyLogStreamStatement = iam.PolicyStatement(
            sid="CloudWatchLogStreamForLambdaPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=["logs:CreateLogStream", "logs:PutLogEvents"],
            resources=[
                "arn:aws:logs:{region}:{accountId}:log-group:/aws/lambda/*:*".format(
                    accountId=stackConfig.accountId, region=stackConfig.region
                )
            ],
        )

        cloudwatchForLambdaPolicy = iam.Policy(
            self,
            "CloudwatchForLambdaPolicy",
            statements=[
                cloudwatchPolicyLogGroupStatement,
                cloudwatchPolicyLogStreamStatement,
            ],
        )

        cloudwatchForLambdaPolicy.attach_to_role(role=role)

        s3ForLambdaPolicyStatement = iam.PolicyStatement(
            sid="S3ForLambdaPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=["s3:GetObject", "s3:ListBucket"],
            resources=[
                "arn:aws:s3:::{bucketName}/{inputObjectPrefix}/*".format(
                    bucketName=stackConfig.bucketName,
                    inputObjectPrefix=stackConfig.inputObjectPrefix,
                ),
                "arn:aws:s3:::{bucketName}",
            ],
        )

        s3ForLambdaPolicy = iam.Policy(
            self,
            "s3ForLambdaPolicy",
            statements=[s3ForLambdaPolicyStatement],
        )

        s3ForLambdaPolicy.attach_to_role(role=role)

        if stackConfig.generate_lambda == True:
            self.generate_lambda(role, stackConfig.bucketName, stackConfig.lambdaName)
            self.create_dynamodb_table(stackConfig)
        else:
            self.upload_lambda_code()

    def generate_lambda(self, role, bucketName, lambdaName):
        lambdaFunction = _lambda.Function(
            self,
            "DynamoDB_Lambda",
            function_name=lambdaName,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("Lambda"),
            handler="lambda_function.lambda_handler",
            role=role,
        )

        bucket = s3.Bucket.from_bucket_name(
            self, "S3EventNotificationsBucket", bucket_name=bucketName
        )

        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(lambdaFunction),
            s3.NotificationKeyFilter(prefix="files/"),
        )

    def create_dynamodb_table(self, stackConfig):
        # create a dynamodb table
        ddb.CfnGlobalTable(
            self,
            "DynamoDBTable",
            attribute_definitions=[
                ddb.CfnGlobalTable.AttributeDefinitionProperty(
                    attribute_name=stackConfig.dynamoDBPartitionKey,
                    attribute_type="S",
                ),
                ddb.CfnGlobalTable.AttributeDefinitionProperty(
                    attribute_name=stackConfig.dynamoDBSortKey,
                    attribute_type="S",
                ),
            ],
            key_schema=[
                ddb.CfnGlobalTable.KeySchemaProperty(
                    attribute_name=stackConfig.dynamoDBPartitionKey, key_type="HASH"
                ),
                ddb.CfnGlobalTable.KeySchemaProperty(
                    attribute_name=stackConfig.dynamoDBSortKey, key_type="RANGE"
                ),
            ],
            replicas=[
                ddb.CfnGlobalTable.ReplicaSpecificationProperty(
                    region=stackConfig.region
                ),
                ddb.CfnGlobalTable.ReplicaSpecificationProperty(
                    region=stackConfig.dynamoDBSecondaryRegion
                ),
            ],
            billing_mode="PAY_PER_REQUEST",
            table_name=stackConfig.dynamoDBTableName,
            stream_specification=ddb.CfnGlobalTable.StreamSpecificationProperty(
                stream_view_type="NEW_AND_OLD_IMAGES"
            ),
        )

    def upload_lambda_code(self):
        lambda_code_rel_path = "Lambda-noDynamo/Lambda-code.zip"
        with ZipFile(lambda_code_rel_path, "w") as zip_object:
            # Adding files that need to be zipped
            zip_object.write(
                filename="Lambda-noDynamo/lambda_function.py",
                arcname="lambda_function.py",
            )

        asset = s3a.Asset(self, "LambdaNoDynamoCode", path=lambda_code_rel_path)

        CfnOutput(
            self,
            "s3_url_lambdacode",
            value=asset.s3_object_url,
        )
