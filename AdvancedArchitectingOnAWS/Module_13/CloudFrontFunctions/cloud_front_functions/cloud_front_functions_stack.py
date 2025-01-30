from aws_cdk import RemovalPolicy, Stack
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_s3 as s3  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct


class CloudFrontFunctionsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        cloudfront_functions_bucket_name = (
            "aws-training-marccharouk-cloudfrontfunctions"
        )

        cloudfront_functions_bucket = s3.Bucket(
            self,
            "cloudfront_functions_bucket",
            bucket_name=cloudfront_functions_bucket_name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        self.uploadObject(cloudfront_functions_bucket, "images", "./images")

        cloudfront_function_code_location = "./function/rewriteUrl.js"
        # create a cloudfront function
        rewrite_function = cloudfront.Function(
            self,
            "MyFunction",
            code=cloudfront.FunctionCode.from_file(
                file_path=cloudfront_function_code_location
            ),
        )

        # create a cloudfront distribution
        # associate s3 bucket as origin, and create an OAC
        # associate cloud front function with distribution
        # allowed methods are GET, HEAD, and OPTIONS
        # Viewer Protocol Policy is Redirect to HTTPS
        # default root object is images/orange-cat.jpg

        cloudfront.Distribution(
            self,
            "MyDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(
                    bucket=cloudfront_functions_bucket,
                ),
                function_associations=[
                    cloudfront.FunctionAssociation(
                        function=rewrite_function,
                        event_type=cloudfront.FunctionEventType.VIEWER_REQUEST,
                    )
                ],
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="images/orange-cat.jpg",
        )

    def uploadObject(self, bucket, prefix, file_name):
        s3deploy.BucketDeployment(
            self,
            f"S3Deployment-{prefix}",
            sources=[s3deploy.Source.asset(file_name)],
            destination_bucket=bucket,
            destination_key_prefix=prefix,
        )
