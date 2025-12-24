from aws_cdk import RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from aws_cdk import aws_ssm as ssm
from constructs import Construct


class XRayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = "marc-charouk-dynamodb-imports3-7564787"
        bucket = s3.Bucket(
            self,
            bucket_name,
            bucket_name=bucket_name,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        bucket_deployment = s3deploy.BucketDeployment(
            self,
            "DeployAssets",
            sources=[s3deploy.Source.asset("input_files")],
            destination_bucket=bucket,
        )

        # create a dynamodb table from S3 import
        table = dynamodb.Table(
            self,
            "CitiesTable",
            table_name="cities",
            partition_key=dynamodb.Attribute(
                name="city_ascii", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="iso2", type=dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY,
            import_source=dynamodb.ImportSourceSpecification(
                compression_type=dynamodb.InputCompressionType.GZIP,
                input_format=dynamodb.InputFormat.csv(),
                bucket=bucket,
            ),
        )
        table.node.add_dependency(bucket_deployment)

        # create a lambda layer called xrayDemoLayer
        # zip package is in layer-package/layer-package.zip
        # compatible runtimes are python3.12 and python3.11
        # compatible architecture is x86_64

        layerVersion = _lambda.LayerVersion(
            self,
            "xrayDemoLayer",
            code=_lambda.Code.from_asset("layer-package/layer-package.zip"),
            compatible_runtimes=[
                _lambda.Runtime.PYTHON_3_13                
            ],
            compatible_architectures=[_lambda.Architecture.X86_64],
        )

        powertool_layer = _lambda.LayerVersion.from_layer_version_arn(
            self,
            "PowerToolsLayer",
            layer_version_arn=f"arn:aws:lambda:{self.region}:017000801446:layer:AWSLambdaPowertoolsPythonV2:18",
        )

        # create an iam role that have basic lambda policies, permission to read a dynamodb table, permission to read an ssm parameter
        cityIamRole = iam.Role(
            self,
            "CityLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSXRayDaemonWriteAccess"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonDynamoDBReadOnlyAccess"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSSMReadOnlyAccess"
                ),
            ],
        )

        weatherIamRole = iam.Role(
            self,
            "WeatherLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSXRayDaemonWriteAccess"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                ),
            ],
        )

        weather_lambda_name = "WeatherFunction"
        weatherLambdaFunction = _lambda.Function(
            self,
            weather_lambda_name,
            function_name=weather_lambda_name,
            runtime=_lambda.Runtime.PYTHON_3_13,
            code=_lambda.Code.from_asset("lambda_weather"),
            handler="lambda_function.lambda_handler",
            tracing=_lambda.Tracing.ACTIVE,
            role=weatherIamRole,
            layers=[layerVersion, powertool_layer],
        )

        lambda_name_city = "CityFunction"
        cityLambdaFunction = _lambda.Function(
            self,
            lambda_name_city,
            function_name=lambda_name_city,
            runtime=_lambda.Runtime.PYTHON_3_13,
            code=_lambda.Code.from_asset("lambda_city"),
            handler="lambda_function.lambda_handler",
            tracing=_lambda.Tracing.ACTIVE,
            role=cityIamRole,
            layers=[layerVersion, powertool_layer],
        )
        # create a Rest API names DemoX-Ray
        # add and endpoint weather connected to lambda function with proxy integration v2
        # add two query parameters : latitude and longitude
        # add a stage called dev

        rest_api = apigw.RestApi(
            self,
            "DemoX-Ray",
            rest_api_name="DemoX-Ray",
            deploy_options=apigw.StageOptions(stage_name="dev", tracing_enabled=True),
        )

        rest_api.root.add_resource("weather").add_method(
            "GET",
            apigw.LambdaIntegration(weatherLambdaFunction),
            request_parameters={
                "method.request.querystring.latitude": True,
                "method.request.querystring.longitude": True,
            },
        )

        rest_api.root.add_resource("city").add_method(
            "GET",
            apigw.LambdaIntegration(cityLambdaFunction),
            request_parameters={
                "method.request.querystring.city": True,
                "method.request.querystring.country": True,
            },
        )

        # put stage url in parameter store key named /xraydemo/weather-url
        ssm.StringParameter(
            self,
            "WeatherURL",
            parameter_name="/xraydemo/weather-url",
            string_value=rest_api.url_for_path("/weather"),
        )

        ssm.StringParameter(
            self,
            "CityUrl",
            parameter_name="/xraydemo/city-url",
            string_value=rest_api.url_for_path("/city"),
        )
