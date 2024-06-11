from aws_cdk import CfnOutput, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3_assets as s3a
from aws_cdk import aws_servicecatalog as sc
from constructs import Construct


class ServiceCatalogStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.createRole(
            "EC2ProductPolicyForServiceCatalogRole",
            iam.ServicePrincipal("servicecatalog.amazonaws.com"),
            [self.createServiceCatalogPolicy()],
        )

        cloudFormationTemplatePath = "resources/ec2-linux-apache.json"
        asset = s3a.Asset(
            self, "cloudFormationTemplatePath", path=cloudFormationTemplatePath
        )

        sc.TagOptions(
            self,
            "ProjectTagOptions",
            allowed_values_for_tags={"Project": ["ProjectA", "ProjectB", "ProjectC"]},
        )

        CfnOutput(
            self,
            "CloudFormationTemplateS3Url",
            value="https://{0}.s3.eu-west-3.amazonaws.com/{1}".format(
                asset.s3_bucket_name, asset.s3_object_key
            ),
        )

    def createServiceCatalogPolicy(self):
        iamRoleStatement = iam.PolicyStatement(
            sid="iamRoleStatement",
            effect=iam.Effect.ALLOW,
            actions=[
                "iam:GetRole",
                "iam:PassRole",
                "iam:DetachRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy",
                "iam:GetRolePolicy",
            ],
            resources=["arn:aws:iam::*:role/*"],
        )

        s3Statement = iam.PolicyStatement(
            sid="s3Statement",
            effect=iam.Effect.ALLOW,
            actions=["s3:GetObject"],
            resources=["*"],
            conditions={
                "StringEquals": {
                    "s3:ExistingObjectTag/servicecatalog:provisioning": "true"
                }
            },
        )

        allResourcesStatement = iam.PolicyStatement(
            sid="allResourcesStatement",
            effect=iam.Effect.ALLOW,
            actions=[
                "cloudformation:SetStackPolicy",
                "iam:CreateInstanceProfile",
                "iam:DeleteInstanceProfile",
                "sns:*",
                "iam:GetInstanceProfile",
                "iam:RemoveRoleFromInstanceProfile",
                "iam:ListInstanceProfileTags",
                "iam:ListInstanceProfiles",
                "cloudformation:GetTemplateSummary",
                "iam:AddRoleToInstanceProfile",
                "cloudformation:DescribeStacks",
                "iam:ListInstanceProfilesForRole",
                "cloudformation:DescribeStackEvents",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "ssm:*",
                "cloudformation:UpdateStack",
                "ec2:*",
                "servicecatalog:*",
                "iam:UntagInstanceProfile",
                "cloudformation:ValidateTemplate",
                "iam:TagInstanceProfile",
            ],
            resources=["*"],
        )

        return self.createPolicy(
            "EC2ProductPolicyForServiceCatalog",
            [iamRoleStatement, s3Statement, allResourcesStatement],
        )

    def createRole(self, roleName, principal, policies):
        role = iam.Role(
            self,
            roleName,
            role_name=roleName,
            assumed_by=principal,
        )
        for policy in policies:
            policy.attach_to_role(role=role)

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy
