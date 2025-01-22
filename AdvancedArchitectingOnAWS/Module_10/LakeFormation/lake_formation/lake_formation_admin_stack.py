import boto3
from aws_cdk import Stack
from aws_cdk import aws_lakeformation as lf
from constructs import Construct
from lake_formation.lake_formation_admins import LfAdmin


class LakeFormationAdminStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        admin_role_pattern = "AWSAdministratorAccess"
        iam_client = boto3.client("iam")
        roles = iam_client.list_roles(
            PathPrefix="/aws-reserved/sso.amazonaws.com/eu-west-3"
        )["Roles"]
        for role in roles:
            if admin_role_pattern in role["RoleName"]:
                role_arn = role["Arn"]
                break

        iam_client.close()

        # set current role as a Lake formation administrator
        cfn_execution_role_name = self.node.try_get_context("cfn_execution_role_name")
        if not cfn_execution_role_name:
            cfn_execution_role_name = (
                f"cdk-hnb659fds-cfn-exec-role-{self.account}-{self.region}"
            )
        cfn_execution_role_arn = (
            f"arn:aws:iam::{self.account}:role/{cfn_execution_role_name}"
        )

        lf.CfnDataLakeSettings(
            self,
            "MyCfnDataLakeSettings",
            admins=[
                lf.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier=role_arn
                ),
                lf.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier=cfn_execution_role_arn
                ),
            ],
            create_database_default_permissions=[],  # Empty list removes IAMAllowedPrincipals
            create_table_default_permissions=[],
        )

        self.admin_roles = [
            LfAdmin("CfnExecutionRole", cfn_execution_role_arn),
            LfAdmin("AWSAdminRole", role_arn),
        ]
