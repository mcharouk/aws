from aws_cdk import Stack
from aws_cdk import aws_cloudfront as cloudfront
from constructs import Construct


class CloudFrontFunctionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cloudfront_function_code_location = "./function/rewriteUrl.js"
        # create a cloudfront function
        self.rewrite_function = cloudfront.Function(
            self,
            "MyRedirectFunction",
            function_name="UserAgentRedirectFunction",
            code=cloudfront.FunctionCode.from_file(
                file_path=cloudfront_function_code_location
            ),
            runtime=cloudfront.FunctionRuntime.JS_2_0,
        )
