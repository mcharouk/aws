from aws_cdk import RemovalPolicy, Stack
from aws_cdk import aws_glue as glue
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from constructs import Construct


class LakeFormationGlueCrawlerStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        crawler_role: iam.Role,
        database_name: str,
        target_root_folder_datalake: str,
        datalake_bucket: s3.Bucket,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        crawler = glue.CfnCrawler(
            self,
            "training-data-crawler",
            name="training-data-crawler",
            role=crawler_role.role_arn,
            database_name=database_name,
            targets=glue.CfnCrawler.TargetsProperty(
                s3_targets=[
                    glue.CfnCrawler.S3TargetProperty(
                        path=f"s3://{datalake_bucket.bucket_name}/{target_root_folder_datalake}/"
                    )
                ]
            ),
            lake_formation_configuration=glue.CfnCrawler.LakeFormationConfigurationProperty(
                account_id=self.account, use_lake_formation_credentials=True
            ),
        )
