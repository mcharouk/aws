from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as _lambda
from cdk.StackConfig import StackConfig
from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        stackConfig = StackConfig()

        lambdaFunction = _lambda.Function(
            self,
            "APIGateway_Lambda",
            function_name=stackConfig.lambda_name,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("Lambdas/API"),
            handler="lambda_function.lambda_handler",
        )

        if stackConfig.generate_api_gateway == True:
            self.generate_api_gateway(
                lambdaFunction, stackConfig.api_gateway_rest_api_name
            )

    def generate_api_gateway(self, lambdaFunction, api_gateway_rest_api_name):
        # Create a Rest API Gateway
        api = apigw.LambdaRestApi(
            self,
            "DemoAPIGateway",
            rest_api_name=api_gateway_rest_api_name,
            description="Demo API Gateway",
            deploy_options=apigw.StageOptions(
                stage_name="dev",
            ),
            proxy=False,
            handler=lambdaFunction,
            endpoint_export_name="DevStageEndpoint",
        )

        resources = api.root.add_resource("resource")
        resources.add_resource("{id}").add_method("GET")
