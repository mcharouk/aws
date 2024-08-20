from aws_cdk import RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct


class BatchOperationsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = "demo-marccharouk-batchoperations-678474-files"

        bucket = s3.Bucket(
            self,
            bucket_name,
            bucket_name=bucket_name,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        s3deploy.BucketDeployment(
            self,
            "DeployAssets",
            sources=[s3deploy.Source.asset("input_files")],
            destination_bucket=bucket,
        )

        lambda_name = "batchoperations-update-tags"

        lambda_role = self.createRole(
            roleName="LambdaForBatchOperationsRole",
            principal=iam.ServicePrincipal("lambda.amazonaws.com"),
            policies=[self.createLambdaBatchOperationsPolicy(lambda_name, bucket)],
        )

        lambda_function = _lambda.Function(
            self,
            id=lambda_name,
            function_name=lambda_name,
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset("lambda"),
            handler="lambda_function.lambda_handler",
            role=lambda_role,
        )

        self.createRole(
            roleName="BatchOperationsRole",
            principal=iam.ServicePrincipal("batchoperations.s3.amazonaws.com"),
            policies=[self.createBatchOperationsPolicy(lambda_function, bucket)],
        )

    def createBatchOperationsPolicy(self, lambda_function, s3_bucket):
        lambdaInvokeStatement = iam.PolicyStatement(
            sid="lambdaInvoke",
            effect=iam.Effect.ALLOW,
            actions=["lambda:InvokeFunction"],
            resources=[lambda_function.function_arn],
        )

        s3Statement = iam.PolicyStatement(
            sid="s3Statement",
            effect=iam.Effect.ALLOW,
            actions=["s3:GetObject", "s3:GetObjectVersion", "s3:PutObject"],
            resources=[s3_bucket.bucket_arn + "/*"],
        )

        return self.createPolicy(
            "BatchOperationsPolicy",
            [lambdaInvokeStatement, s3Statement],
        )

    def createLambdaBatchOperationsPolicy(self, lambda_name, s3_bucket):
        logGroupStatement = iam.PolicyStatement(
            sid="logGroupStatement",
            effect=iam.Effect.ALLOW,
            actions=["logs:CreateLogGroup"],
            resources=["arn:aws:logs:eu-west-3:*:*"],
        )

        logStreamStatement = iam.PolicyStatement(
            sid="logStreamStatement",
            effect=iam.Effect.ALLOW,
            actions=["logs:CreateLogStream", "logs:PutLogEvents"],
            resources=[
                "arn:aws:logs:eu-west-3:*:log-group:/aws/lambda/{0}:*".format(
                    lambda_name
                )
            ],
        )

        s3ObjectStatement = iam.PolicyStatement(
            sid="s3ObjectStatement",
            effect=iam.Effect.ALLOW,
            actions=["s3:GetObject", "s3:PutObjectTagging"],
            resources=[s3_bucket.bucket_arn + "/*"],
        )

        return self.createPolicy(
            "LambdaBatchOperationsPolicy",
            [logGroupStatement, logStreamStatement, s3ObjectStatement],
        )

    def createRole(self, roleName, principal, policies):
        role = iam.Role(
            self,
            roleName,
            role_name=roleName,
            assumed_by=principal,
        )
        for policy in policies:
            policy.attach_to_role(role=role)

        return role

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy
