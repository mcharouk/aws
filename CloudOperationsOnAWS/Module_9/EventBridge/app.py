#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags
from event_bridge.event_bridge_stack import EventBridgeStack
from event_bridge.event_bridge_stack_us_east_1 import EventBridgeStackUsEast1


app = cdk.App()

eventBridgeStackUsEast1 = EventBridgeStackUsEast1(
    app,
    "EventBridgeStackUsEast1",
    env=cdk.Environment(region="us-east-1", account=os.getenv("CDK_DEFAULT_ACCOUNT")),
)


eventBridgeStack = EventBridgeStack(
    app,
    "EventBridgeStack",
    env=cdk.Environment(region="eu-west-3", account=os.getenv("CDK_DEFAULT_ACCOUNT")),
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

Tags.of(eventBridgeStack).add("DemoName", "EventBridge")
Tags.of(eventBridgeStackUsEast1).add("DemoName", "EventBridge")

app.synth()
