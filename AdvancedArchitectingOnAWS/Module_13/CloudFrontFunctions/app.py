#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags
from cloud_front_functions.cloudfront_distribution_stack import (
    CloudFrontDistributionStack,
)
from cloud_front_functions.cloudfront_function_stack import CloudFrontFunctionStack

app = cdk.App()
function_stack = CloudFrontFunctionStack(
    app,
    "CloudFrontFunctionsStack",
    env=cdk.Environment(region="us-east-1", account=os.getenv("CDK_DEFAULT_ACCOUNT")),
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.
    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.
    # env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */
    # env=cdk.Environment(account='123456789012', region='us-east-1'),
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
)
distribution_stack = CloudFrontDistributionStack(
    app,
    "CloudFrontDistributionStack",
    env=cdk.Environment(region="eu-west-3", account=os.getenv("CDK_DEFAULT_ACCOUNT")),
    cf_function=function_stack.rewrite_function,
    cross_region_references=True,
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.
    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.
    # env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */
    # env=cdk.Environment(account='123456789012', region='us-east-1'),
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
)

distribution_stack.add_dependency(function_stack)

Tags.of(function_stack).add("DemoName", "CloudFrontFunctions")
Tags.of(distribution_stack).add("DemoName", "CloudFrontFunctions")

app.synth()
