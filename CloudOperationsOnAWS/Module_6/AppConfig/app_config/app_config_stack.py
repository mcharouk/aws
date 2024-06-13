from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import Duration
from aws_cdk import aws_appconfig as appconfig
from aws_cdk import aws_cloudwatch as cloudwatch
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class AppConfigStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_name = "AppConfigLambda"

        lambda_role = iam.Role(
            self,
            "appConfigLambdaRole",
            role_name="appConfigLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        ssmCloudWatchAlarmDiscoveryRole = iam.Role(
            self,
            "ssmCloudWatchAlarmDiscoveryRole",
            role_name="ssmCloudWatchAlarmDiscoveryRole",
            assumed_by=iam.ServicePrincipal("appconfig.amazonaws.com"),
        )

        self.createLambdaAppConfigPolicy().attach_to_role(role=lambda_role)
        self.createLambdaCloudWatchPolicy(lambda_name).attach_to_role(role=lambda_role)

        self.createAppConfigAlarmRole().attach_to_role(
            role=ssmCloudWatchAlarmDiscoveryRole
        )

        appConfigLayer = _lambda.LayerVersion.from_layer_version_arn(
            self,
            id="appConfigLayer",
            layer_version_arn="arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:111",
        )

        _lambda.Function(
            self,
            id="AppConfig_Lambda",
            function_name=lambda_name,
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("Lambda"),
            handler="lambda_function.lambda_handler",
            role=lambda_role,
            layers=[appConfigLayer],
            environment={"AWS_APPCONFIG_EXTENSION_POLL_INTERVAL_SECONDS": "15"},
        )

        metric = cloudwatch.Metric(
            namespace="AWS/Lambda",
            metric_name="Duration",
            dimensions_map={"FunctionName": lambda_name},
            period=Duration.seconds(300),
            statistic="Average",
        )

        cloudwatch.Alarm(
            self,
            "AppConfigAlarm",
            alarm_name="AppConfigAlarm",
            comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
            threshold=10000,
            evaluation_periods=1,
            datapoints_to_alarm=1,
            metric=metric,
            treat_missing_data=cloudwatch.TreatMissingData.MISSING,
        )

        # create app config deployment strategy
        appconfig.CfnDeploymentStrategy(
            self,
            id="DemoDeploymentStrategy",
            name="DemoDeploymentStrategy",
            description="Strategy to use for quick deployment in demo",
            final_bake_time_in_minutes=1,
            deployment_duration_in_minutes=0,
            growth_factor=100,
            replicate_to="NONE",
        )

    def createLambdaAppConfigPolicy(self):
        appConfigStatement = iam.PolicyStatement(
            sid="iamRoleStatement",
            effect=iam.Effect.ALLOW,
            actions=[
                "appconfig:GetLatestConfiguration",
                "appconfig:StartConfigurationSession",
            ],
            resources=["*"],
        )

        return self.createPolicy(
            "LambdaAppConfigPolicy",
            [appConfigStatement],
        )

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

    def createAppConfigAlarmRole(self):
        ssmCloudWatchAlarmDiscoveryStatement = iam.PolicyStatement(
            sid="SSMCloudWatchAlarmDiscoveryStatement",
            effect=iam.Effect.ALLOW,
            actions=["cloudwatch:DescribeAlarms"],
            resources=["*"],
        )

        return self.createPolicy(
            "SSMCloudWatchAlarmDiscoveryPolicy",
            [ssmCloudWatchAlarmDiscoveryStatement],
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
