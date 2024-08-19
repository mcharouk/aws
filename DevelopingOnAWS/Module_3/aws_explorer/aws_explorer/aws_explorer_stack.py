from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_sqs as sqs
from constructs import Construct


class AwsExplorerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_name = "HelloWorldLambda"
        lambda_role = self.createRole(
            roleName="HelloWorldLambdaRole",
            principal=iam.ServicePrincipal("lambda.amazonaws.com"),
            policies=[self.createLambdaCloudWatchPolicy(lambda_name)],
        )

        _lambda.Function(
            self,
            id="HelloWorld_Lambda",
            function_name=lambda_name,
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset("Lambda"),
            handler="lambda_function.lambda_handler",
            role=lambda_role,
        )
        # The code that defines your stack goes here

    def createLambdaCloudWatchPolicy(self, lambda_name):
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

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy
