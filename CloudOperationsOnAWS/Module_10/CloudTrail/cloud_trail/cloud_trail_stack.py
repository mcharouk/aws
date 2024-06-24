from aws_cdk import RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_athena as athena
from aws_cdk import aws_glue as glue
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct


class CloudTrailStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        bucket_name = "cloudtrail-demo-marccharouk-847856739"
        # The code that defines your stack goes here

        # create an s3 bucket named accesspointdemo-marccharouk-548675486
        cloudtrail_bucket = s3.Bucket(
            self,
            "cloudTrailDataBucket",
            bucket_name=bucket_name,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        bucket_name = "athena-querylocation-marccharouk-847856739"
        # The code that defines your stack goes here

        # create an s3 bucket named accesspointdemo-marccharouk-548675486
        athena_querylocation_bucket = s3.Bucket(
            self,
            "athenaQueryLocationBucket",
            bucket_name=bucket_name,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        root_folder_cloudtrail = "AWSLogs/637423642269/CloudTrail/eu-west-3/2024/06/24/"
        self.uploadObject(cloudtrail_bucket, root_folder_cloudtrail, "./resources/data")

        database_name = "cloudtrail-demo"
        # create a glue database
        glue.CfnDatabase(
            self,
            "glueDatabase",
            catalog_id=self.account,  # type: ignore
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                name=database_name, description="Database for cloudtrail data"
            ),
        )

        # create an athena workgroup
        athena.CfnWorkGroup(
            self,
            "CloudtrailWorkgroup",
            name="cloudtrail-workgroup",
            description="Athena Workgroup for CloudTrail",
            recursive_delete_option=True,
            state="ENABLED",
            work_group_configuration=athena.CfnWorkGroup.WorkGroupConfigurationProperty(
                enforce_work_group_configuration=True,
                result_configuration=athena.CfnWorkGroup.ResultConfigurationProperty(
                    output_location=f"s3://{athena_querylocation_bucket.bucket_name}/queryResults"
                ),
            ),
        )

    def uploadObject(self, bucket, prefix, file_name):
        s3deploy.BucketDeployment(
            self,
            f"S3Deployment-{prefix}",
            sources=[s3deploy.Source.asset(file_name)],
            destination_bucket=bucket,
            destination_key_prefix=prefix,
        )
