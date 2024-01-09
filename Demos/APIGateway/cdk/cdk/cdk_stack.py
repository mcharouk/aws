from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _lambda.Function(
            self,
            "APIGateway_Lambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("Lambdas/API"),
            handler="lambda_function.lambda_handler",
        )
