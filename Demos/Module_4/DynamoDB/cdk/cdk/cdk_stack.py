from aws_cdk import Stack
from aws_cdk import aws_iam as iam  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_event_sources as _lambda_es
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_notifications as s3n
from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        accountId = "270188911144"
        region = "eu-west-3"
        dynamoDBTableName = "demo_employee"
        bucketName = "eventnotification-demo-457663"
        inputObjectPrefix = "files"
        generate_lambda = False

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
                    region=region, accountId=accountId, tableName=dynamoDBTableName
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
                    region=region, accountId=accountId
                )
            ],
        )

        cloudwatchPolicyLogStreamStatement = iam.PolicyStatement(
            sid="CloudWatchLogStreamForLambdaPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=["logs:CreateLogStream", "logs:PutLogEvents"],
            resources=[
                "arn:aws:logs:{region}:{accountId}:log-group:/aws/lambda/*:*".format(
                    accountId=accountId, region=region
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
                    bucketName=bucketName, inputObjectPrefix=inputObjectPrefix
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

        if generate_lambda == True:
            self.generate_lambda(role, bucketName)

    def generate_lambda(self, role, bucketName):
        lambdaFunction = _lambda.Function(
            self,
            "DynamoDB_Lambda",
            function_name="DynamoDB-S3Feeder",
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
