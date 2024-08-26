from aws_cdk import RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_cognito as cognito
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from aws_cdk import custom_resources as cr
from constructs import Construct


class CognitoIdentityPoolStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create cognito user pool
        user_pool = cognito.UserPool(
            self,
            "UserPoolForIdentityPoolDemo",
            user_pool_name="UserPoolForIdentityPoolDemo",
            removal_policy=RemovalPolicy.DESTROY,
            self_sign_up_enabled=False,
            password_policy=cognito.PasswordPolicy(
                min_length=6,
                require_lowercase=False,
                require_uppercase=False,
                require_digits=False,
                require_symbols=False,
            ),
            sign_in_aliases=cognito.SignInAliases(
                username=True, email=False, phone=False, preferred_username=False
            ),
            standard_attributes=cognito.StandardAttributes(
                preferred_username=cognito.StandardAttribute(
                    required=True,
                    mutable=True,
                )
            ),
            account_recovery=cognito.AccountRecovery.NONE,
            deletion_protection=False,
        )

        # create a user pool client
        user_pool_client = cognito.UserPoolClient(
            self,
            "MyAppClient",
            user_pool=user_pool,
            generate_secret=True,
            supported_identity_providers=[
                cognito.UserPoolClientIdentityProvider.COGNITO
            ],
            auth_flows=cognito.AuthFlow(
                user_password=True,
            ),
            user_pool_client_name="MyAppClient",
        )

        self.create_user(
            user_pool=user_pool,
            user_id="JohnFooUser",
            user_name="john.foo",
            user_password="john.foo",
            department="finance",
        )

        self.create_user(
            user_pool=user_pool,
            user_id="DaveBarUser",
            user_name="dave.bar",
            user_password="dave.bar",
            department="rh",
        )

        bucket_name = "marc-charouk-identitypool-demo"

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

        """role = iam.Role(
            self,
            "LambdaRole",
            role_name="DynamoDBLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )"""

        policy = iam.ManagedPolicy(
            self, "IdentityPoolTestPolicy", managed_policy_name="IdentityPoolTestPolicy"
        )
        policy.add_statements(
            iam.PolicyStatement(
                sid="allowListBucket",
                effect=iam.Effect.ALLOW,
                actions=["s3:List*"],
                resources=[bucket.bucket_arn],
            ),
            iam.PolicyStatement(
                sid="allowGetObjectBucket",
                effect=iam.Effect.ALLOW,
                actions=["s3:GetObject*"],
                resources=[
                    "{0}/${{aws:PrincipalTag/department}}/*".format(bucket.bucket_arn)
                ],
            ),
        )

        # policy.attach_to_role(role)

    def create_user(self, user_pool, user_id, user_name, user_password, department):
        user = cognito.CfnUserPoolUser(
            self,
            user_id,
            user_pool_id=user_pool.user_pool_id,
            username=user_name,
            user_attributes=[
                cognito.CfnUserPoolUser.AttributeTypeProperty(
                    name="department",
                    value=department,
                )
            ],
        )

        user_password_id = f"{user_id}Password"
        cr.AwsCustomResource(
            self,
            user_password_id,
            on_create=cr.AwsSdkCall(
                service="CognitoIdentityServiceProvider",
                action="adminSetUserPassword",
                parameters={
                    "UserPoolId": user_pool.user_pool_id,
                    "Username": user.username,
                    "Password": user_password,
                    "Permanent": True,
                },
                physical_resource_id=cr.PhysicalResourceId.of(f"Set{user_password_id}"),
            ),
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE,
            ),
        )
        return user
