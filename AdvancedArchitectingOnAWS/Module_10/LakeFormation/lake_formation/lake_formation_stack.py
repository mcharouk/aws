from typing import List

from aws_cdk import RemovalPolicy, Stack
from aws_cdk import aws_athena as athena
from aws_cdk import aws_glue as glue
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lakeformation as lf  # Duration,
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct
from lake_formation.lake_formation_admins import LfAdmin


class LakeFormationStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        admin_roles: List[LfAdmin],
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        datalake_bucket_name = "aws-training-marccharouk-datalake"
        athena_results_bucket_name = "aws-training-marccharouk-athena-results"
        self.database_name = "training-data"

        # create datalake s3 bucket
        self.datalake_bucket = s3.Bucket(
            self,
            "datalake_bucket",
            bucket_name=datalake_bucket_name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        athena_results_bucket = s3.Bucket(
            self,
            "athena_results_bucket",
            bucket_name=athena_results_bucket_name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        # register datalake bucket as lakeformation data location

        data_location_policy_statements = [
            iam.PolicyStatement(
                actions=["lakeformation:RegisterResource"],
                resources=[
                    self.datalake_bucket.bucket_arn,
                ],
            ),
            iam.PolicyStatement(
                actions=["s3:PutObject", "s3:GetObject", "s3:DeleteObject"],
                resources=[
                    f"{self.datalake_bucket.bucket_arn}/*",
                ],  # You may want to restrict this to specific role ARNs
            ),
            iam.PolicyStatement(
                actions=["s3:ListBucket"],
                resources=[
                    self.datalake_bucket.bucket_arn
                ],  # You may want to restrict this to specific role ARNs
            ),
        ]

        # Create the policy using your existing helper method
        data_location_policy = self.createPolicy(
            "Lf-datalocation-policy", data_location_policy_statements
        )

        # Create the role using your existing helper method
        data_location_role = self.createRole(
            "DataLocationRole",
            iam.CompositePrincipal(
                iam.ServicePrincipal("lakeformation.amazonaws.com"),
                iam.ServicePrincipal("glue.amazonaws.com"),
            ),
            [data_location_policy],
        )

        s3_data_location_resource = lf.CfnResource(
            self,
            "MyS3DataLocation",
            resource_arn=self.datalake_bucket.bucket_arn,
            use_service_linked_role=False,
            role_arn=data_location_role.role_arn,
        )

        self.target_root_folder_datalake = "cities"
        self.uploadObject(
            self.datalake_bucket, self.target_root_folder_datalake, "./data"
        )

        # create a glue database
        database = glue.CfnDatabase(
            self,
            "training-data",
            catalog_id=self.account,
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                name=self.database_name,
                location_uri=f"s3://{datalake_bucket_name}/{self.target_root_folder_datalake}/",
                create_table_default_permissions=[],
            ),
        )
        # create a glue crawler
        crawler_policy_statements = [
            iam.PolicyStatement(
                actions=["s3:GetBucket*", "s3:GetObject*", "s3:List*"],
                resources=[
                    self.datalake_bucket.bucket_arn,
                    f"{self.datalake_bucket.bucket_arn}/*",
                ],
            ),
            iam.PolicyStatement(
                actions=["iam:PassRole"],
                resources=["*"],  # You may want to restrict this to specific role ARNs
            ),
            iam.PolicyStatement(
                actions=["lakeformation:GetDataAccess"],
                resources=["*"],  # You may want to restrict this to specific role ARNs
            ),
        ]

        # Create the policy using your existing helper method
        crawler_policy = self.createPolicy(
            "GlueCrawlerPolicy", crawler_policy_statements
        )

        # Create the role using your existing helper method
        self.crawler_role = self.createRole(
            "GlueCrawlerRole",
            iam.CompositePrincipal(
                iam.ServicePrincipal("lakeformation.amazonaws.com"),
                iam.ServicePrincipal("glue.amazonaws.com"),
            ),
            [crawler_policy],
        )
        self.addManagedPolicy(self.crawler_role, "service-role/AWSGlueServiceRole")

        # add lakeformation permissions to crawler
        lf.CfnPermissions(
            self,
            "CrawlerPermissions",
            data_lake_principal=lf.CfnPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier=self.crawler_role.role_arn
            ),
            resource=lf.CfnPermissions.ResourceProperty(
                database_resource=lf.CfnPermissions.DatabaseResourceProperty(
                    name=database.ref
                )
            ),
            permissions=["ALL"],
        )

        for admin in admin_roles:
            # give permissions to drop all tables in database
            lf.CfnPermissions(
                self,
                f"DropTablePermissions-{admin.logical_id}",
                data_lake_principal=lf.CfnPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier=admin.role_arn
                ),
                resource=lf.CfnPermissions.ResourceProperty(
                    table_resource=lf.CfnPermissions.TableResourceProperty(
                        database_name=database.ref, table_wildcard={}
                    )
                ),
                permissions=["DROP", "DESCRIBE"],
            )

            lf.CfnPermissions(
                self,
                f"SelectTablePermissions-{admin.logical_id}",
                data_lake_principal=lf.CfnPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier=admin.role_arn
                ),
                resource=lf.CfnPermissions.ResourceProperty(
                    table_resource=lf.CfnPermissions.TableResourceProperty(
                        database_name=database.ref, table_wildcard={}
                    )
                ),
                permissions=["SELECT"],
            )

        data_location_resource_property = (
            lf.CfnPermissions.DataLocationResourceProperty(
                s3_resource=f"{self.datalake_bucket.bucket_arn}/*",
            )
        )
        principal_permissions = lf.CfnPermissions(
            self,
            "DatalakePrincipalPermissions",
            permissions=["DATA_LOCATION_ACCESS"],
            permissions_with_grant_option=[],
            data_lake_principal=lf.CfnPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier=self.crawler_role.role_arn
            ),
            resource=lf.CfnPermissions.ResourceProperty(
                data_location_resource=data_location_resource_property
            ),
        )
        principal_permissions.node.add_dependency(s3_data_location_resource)

        workgroup = athena.CfnWorkGroup(
            self,
            "DatalakeAdminsWorkgroup",
            name="datalake-admins-workgroup",
            description="Athena Workgroup for Datalake Admins",
            recursive_delete_option=True,
            state="ENABLED",
            work_group_configuration=athena.CfnWorkGroup.WorkGroupConfigurationProperty(
                enforce_work_group_configuration=True,
                result_configuration=athena.CfnWorkGroup.ResultConfigurationProperty(
                    output_location=f"s3://{athena_results_bucket.bucket_name}/queryResults"
                ),
            ),
        )
        ba_role_name = "businessAnalystRole"

        ba_policy_statements = [
            iam.PolicyStatement(
                actions=[
                    "s3:GetBucketLocation",
                    "s3:GetObject",
                    "s3:ListBucket",
                    "s3:PutObject",
                ],
                resources=[
                    athena_results_bucket.bucket_arn,
                    f"{athena_results_bucket.bucket_arn}/*",
                ],
            ),
            iam.PolicyStatement(
                actions=[
                    "athena:StartQueryExecution",
                    "athena:GetQueryExecution",
                    "athena:GetQueryResults",
                    "athena:GetWorkGroup",
                    "athena:StopQueryExecution",
                    "athena:ListWorkGroups",
                    "athena:GetQueryResultsStream",
                    "athena:ListNamedQueries",
                    "athena:BatchGetNamedQuery",
                    "athena:ListQueryExecutions",
                    "athena:CreateNamedQuery",
                    "athena:GetNamedQuery",
                ],
                resources=[
                    f"arn:aws:athena:{self.region}:{self.account}:workgroup/{workgroup.name}"
                ],  # You may want to restrict this to specific role ARNs
            ),
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "glue:GetTable",
                    "glue:GetTables",
                    "glue:GetDatabase",
                    "glue:GetDatabases",
                    "glue:GetPartitions",
                    "glue:BatchGetPartition",
                    "glue:GetUserDefinedFunction",
                ],
                resources=[
                    f"arn:aws:glue:{self.region}:{self.account}:catalog",
                    f"arn:aws:glue:{self.region}:{self.account}:database/{self.database_name}",
                    f"arn:aws:glue:{self.region}:{self.account}:table/{self.database_name}/*",
                ],
            ),
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["lakeformation:GetDataAccess"],
                resources=["*"],
            ),
        ]

        ba_policy = self.createPolicy("BusinessAnalystPolicy", ba_policy_statements)

        # create a role that can query tables with lake formation
        business_analyst_role = self.createRole(
            ba_role_name,
            iam.AccountPrincipal(account_id=self.account),
            [ba_policy],
        )

        business_analyst_permission = lf.CfnPermissions(
            self,
            "BusinessAnalystDatabasePermissions",
            data_lake_principal=lf.CfnPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier=business_analyst_role.role_arn
            ),
            resource=lf.CfnPermissions.ResourceProperty(
                table_resource=lf.CfnPermissions.TableResourceProperty(
                    database_name=database.ref, table_wildcard={}
                )
            ),
            permissions=["DESCRIBE"],
        )

        business_analyst_permission.node.add_dependency(database)

    def addManagedPolicy(self, role, policyName):
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(policyName)
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

        return role

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy

    def uploadObject(self, bucket, prefix, file_name):
        s3deploy.BucketDeployment(
            self,
            f"S3Deployment-{prefix}",
            sources=[s3deploy.Source.asset(file_name)],
            destination_bucket=bucket,
            destination_key_prefix=prefix,
        )
