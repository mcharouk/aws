#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags
from lake_formation.lake_formation_admin_stack import LakeFormationAdminStack
from lake_formation.lake_formation_glue_crawler_stack import (
    LakeFormationGlueCrawlerStack,
)
from lake_formation.lake_formation_stack import LakeFormationStack

app = cdk.App()
lakeFormation_admin_stack = LakeFormationAdminStack(
    app,
    "LakeFormationAdminStack",
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

lakeFormation_stack = LakeFormationStack(
    app,
    "LakeFormationStack",
    admin_roles=lakeFormation_admin_stack.admin_roles,
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

lakeFormation_glue_crawler_stack = LakeFormationGlueCrawlerStack(
    app,
    "LakeFormationGlueCrawlerStack",
    crawler_role=lakeFormation_stack.crawler_role,
    database_name=lakeFormation_stack.database_name,
    datalake_bucket=lakeFormation_stack.datalake_bucket,
    target_root_folder_datalake=lakeFormation_stack.target_root_folder_datalake,
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

lakeFormation_stack.add_dependency(lakeFormation_admin_stack)
lakeFormation_glue_crawler_stack.add_dependency(lakeFormation_stack)
Tags.of(lakeFormation_stack).add("DemoName", "LakeFormation")
Tags.of(lakeFormation_admin_stack).add("DemoName", "LakeFormation")
Tags.of(lakeFormation_glue_crawler_stack).add("DemoName", "LakeFormation")

app.synth()
