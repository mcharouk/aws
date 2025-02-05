from aws_cdk import CfnOutput, RemovalPolicy, Stack
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_s3 as s3  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct


class CloudFrontDistributionStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        cf_function: cloudfront.Function,
        **kwargs,
    ) -> None:
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

        # create an origin request policy with the following header allow list
        # no cookie should be forwarded
        # all query strings should be forwarded
        origin_request_policy_name = "S3-UserDeviceType"
        header_allow_list = [
            "Origin",
            "Access-Control-Request-Method",
            "CloudFront-Is-IOS-Viewer",
            "Access-Control-Request-Headers",
            "CloudFront-Is-Tablet-Viewer",
            "CloudFront-Is-Mobile-Viewer",
            "CloudFront-Is-SmartTV-Viewer",
            "CloudFront-Is-Android-Viewer",
            "CloudFront-Is-Desktop-Viewer",
        ]
        origin_request_policy = cloudfront.OriginRequestPolicy(
            self,
            origin_request_policy_name,
            origin_request_policy_name=origin_request_policy_name,
            header_behavior=cloudfront.OriginRequestHeaderBehavior.allow_list(
                *header_allow_list
            ),
            query_string_behavior=cloudfront.OriginRequestQueryStringBehavior.all(),
        )

        # create a cloudfront distribution
        # associate s3 bucket as origin, and create an OAC
        # associate cloud front function with distribution
        # allowed methods are GET, HEAD, and OPTIONS
        # Viewer Protocol Policy is Redirect to HTTPS
        # default root object is images/orange-cat.jpg
        # add allviewerAndcloudfrontheaders origin request policy

        distribution = cloudfront.Distribution(
            self,
            "MyDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(
                    bucket=cloudfront_functions_bucket,
                ),
                origin_request_policy=origin_request_policy,
                function_associations=[
                    cloudfront.FunctionAssociation(
                        function=cf_function,
                        event_type=cloudfront.FunctionEventType.VIEWER_REQUEST,
                    )
                ],
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="images/orange-cat.jpg",
        )

        images_url = "/images/orange-cat.jpg"

        CfnOutput(
            self,
            "DistributionDomainName",
            value=distribution.domain_name,
        )

        # output distribution url
        CfnOutput(
            self,
            "DistributionImageUrl",
            value=f"https://{distribution.domain_name}{images_url}",
        )

    def uploadObject(self, bucket, prefix, file_name):
        s3deploy.BucketDeployment(
            self,
            f"S3Deployment-{prefix}",
            sources=[s3deploy.Source.asset(file_name)],
            destination_bucket=bucket,
            destination_key_prefix=prefix,
        )
