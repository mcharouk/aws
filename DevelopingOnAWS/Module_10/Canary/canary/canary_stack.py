from aws_cdk import CfnOutput, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class CanaryStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_name = "CanaryDemo"

        # lambda_role = self.createRole(
        #     roleName="HelloWorldLambdaRole",
        #     principal=iam.ServicePrincipal("lambda.amazonaws.com"),
        #     policies=[self.createLambdaCloudWatchPolicy(lambda_name)],
        # )

        lambdaFunction = _lambda.Function(
            self,
            "APIGateway_Lambda",
            function_name=lambda_name,
            runtime=_lambda.Runtime.PYTHON_3_13,
            code=_lambda.Code.from_asset("lambda"),
            handler="lambda_function.lambda_handler",
        )

        version = lambdaFunction.current_version
        alias_name = "Blue"

        alias = _lambda.Alias(self, "Blue", alias_name=alias_name, version=version)

        api_gateway_rest_api_name = "CanaryDemoRestAPI"
        stage_name = "Prod"
        rest_api = apigw.LambdaRestApi(
            self,
            api_gateway_rest_api_name,
            rest_api_name=api_gateway_rest_api_name,
            description="Demo API Gateway Canary",
            deploy_options=apigw.StageOptions(
                stage_name=stage_name,
                variables={"lambdaAlias": alias_name},
            ),
            proxy=False,
            handler=alias,
            endpoint_export_name="DevStageEndpoint",
        )

        method = rest_api.root.add_method("GET")

        lambdaFunction.add_permission(
            "lambdaPermission",
            action="lambda:InvokeFunction",
            principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
            source_arn=method.method_arn.replace(
                rest_api.deployment_stage.stage_name, "*"
            ),
        )

        CfnOutput(
            self,
            "SourceARN",
            value=f"arn:aws:execute-api:{self.region}:{self.account}:{rest_api.rest_api_id}/*/GET/",
        )
