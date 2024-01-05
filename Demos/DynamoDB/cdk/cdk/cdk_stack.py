from aws_cdk import Stack
from aws_cdk import aws_iam as iam  # Duration,; aws_sqs as sqs,
from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamoDBTableName = "demo_employee"
        accountId = "270188911144"
        region = "eu-west-3"
        dynamoDBTableName = "demo_employee"
        bucketName = "eventnotification-demo-457663"
        inputObjectPrefix = "files"

        # create an iam role assumed by lambda and attach the policy
        role = iam.Role(
            self,
            "LambdaRole",
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
