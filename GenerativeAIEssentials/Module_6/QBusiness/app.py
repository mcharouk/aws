#!/usr/bin/env python3
import os
import aws_cdk as cdk
from q_business.qbusiness_stack import QBusinessStack
from aws_cdk import Tags

app = cdk.App()

# Create the Q Business stack (Account 637423642269, Region eu-west-1)
# Q Business will automatically create the Identity Center application
q_business_stack=QBusinessStack(
    app, 
    "QBusinessDemoStack",
    env=cdk.Environment(
        account='637423642269',  # Q Business account
        region='eu-west-1'       # Ireland region for Q Business
    )
)

Tags.of(q_business_stack).add("DemoName", "QBusiness")

app.synth()