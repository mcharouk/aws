from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class StepFunctionStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        class LambdaProperties:
            def __init__(self, name, assetName):
                self.name = name
                self.assetName = assetName

        generateOrderLambda = LambdaProperties(
            "GenerateOrderLambda", "Lambdas/GenerateOrder"
        )
        buyLambda = LambdaProperties("BuyerLambda", "Lambdas/Buy")
        sellLambda = LambdaProperties("SellerLambda", "Lambdas/Sell")

        for lambdaObject in [generateOrderLambda, buyLambda, sellLambda]:
            # create a lambda function
            _lambda.Function(
                self,
                lambdaObject.name,
                runtime=_lambda.Runtime.PYTHON_3_12,
                code=_lambda.Code.from_asset(lambdaObject.assetName),
                handler="lambda_function.lambda_handler",
            )
