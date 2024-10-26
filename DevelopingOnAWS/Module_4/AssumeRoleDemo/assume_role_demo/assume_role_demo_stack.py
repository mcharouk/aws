from aws_cdk import CfnOutput, SecretValue, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from aws_cdk.aws_secretsmanager import Secret, SecretStringGenerator
from constructs import Construct


class AssumeRoleDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        s3_role_name = "S3access"

        contractor_policy_cloudshell = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["cloudshell:*"],
            resources=["*"],
        )

        contractor_policy_assume_role = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["sts:AssumeRole"],
            resources=[f"arn:aws:iam::{self.account}:role/{s3_role_name}"],
        )

        # create a group named contractor
        contractor_group = iam.Group(
            self,
            "contractor_group",
            group_name="contractor",
        )
        contractor_group.add_to_principal_policy(contractor_policy_cloudshell)
        contractor_group.add_to_principal_policy(contractor_policy_assume_role)

        # generate a random password for the user contractor aith at least one uppercase letter, at least one number, at least one symbol and at least 8 characters
        contractor_password = Secret(
            self,
            "contractor_password",
            secret_name="contractor_password",
            generate_secret_string=SecretStringGenerator(
                exclude_characters="'\"@/\\",
                include_space=False,
                require_each_included_type=True,
                password_length=8,
            ),
        )

        # create a user contractor
        user_name = "contractor"
        contractor = iam.User(
            self,
            "contractor",
            user_name=user_name,
            password=contractor_password.secret_value,
            groups=[contractor_group],
        )

        # create a role for S3_access and add S3 full access managed policy
        s3_role = iam.Role(
            self,
            "s3_role",
            role_name=s3_role_name,
            assumed_by=iam.AccountPrincipal(self.account),
        )
        s3_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
        )

        # display password as output
        CfnOutput(
            self,
            "contractor_pwd",
            value=contractor_password.secret_value.unsafe_unwrap(),
        )
