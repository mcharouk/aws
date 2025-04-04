#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags
from route53.global_stack import GlobalStack
from route53.regional_stack import RegionalStack

app = cdk.App()
globalStack = GlobalStack(
    app,
    "GlobalStack",
    env=cdk.Environment(region="eu-west-3", account=os.getenv("CDK_DEFAULT_ACCOUNT")),
)
parisStack = RegionalStack(
    app,
    "ParisRegionStack",
    env=cdk.Environment(region="eu-west-3", account=os.getenv("CDK_DEFAULT_ACCOUNT")),
    vpc_cidr_range="10.0.1.0/20",
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
irelandStack = RegionalStack(
    app,
    "IrelandRegionStack",
    env=cdk.Environment(region="eu-west-1", account=os.getenv("CDK_DEFAULT_ACCOUNT")),
    vpc_cidr_range="192.168.1.0/20",
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

parisStack.add_dependency(globalStack)
irelandStack.add_dependency(globalStack)

Tags.of(globalStack).add("DemoName", "Route53")
Tags.of(parisStack).add("DemoName", "Route53")
Tags.of(irelandStack).add("DemoName", "Route53")

app.synth()
