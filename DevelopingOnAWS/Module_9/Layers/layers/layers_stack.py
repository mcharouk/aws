from zipfile import ZipFile

from aws_cdk import CfnOutput, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3_assets as s3a
from constructs import Construct


class LayersStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.createRole(
            roleName="LayerLambdaRole",
            principal=iam.ServicePrincipal("lambda.amazonaws.com"),
            policies=[self.createLambdaCloudWatchPolicy()],
        )

        self.upload_lambda_code()

    def upload_lambda_code(self):
        lambda_code_rel_path = "main-function/Lambda-code.zip"
        with ZipFile(lambda_code_rel_path, "w") as zip_object:
            # Adding files that need to be zipped
            zip_object.write(
                filename="main-function/lambda_function.py",
                arcname="lambda_function.py",
            )

        asset = s3a.Asset(self, "MainLambdaFunctionCode", path=lambda_code_rel_path)

        CfnOutput(
            self,
            "s3_url_lambdacode",
            value=asset.s3_object_url,
        )

    def createLambdaCloudWatchPolicy(self):
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
            resources=["arn:aws:logs:eu-west-3:*:log-group:/aws/lambda/*:*"],
        )

        return self.createPolicy(
            "LambdaCloudWatchPolicy",
            [logGroupStatement, logStreamStatement],
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
