from aws_cdk import Stack, CfnOutput
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class PermissionBoundaryStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a policy that allow role creation but only if attached to a permission boundary
        permission_boundary_policy = _iam.ManagedPolicy(
            self,
            "PermissionBoundaryPolicy",
            managed_policy_name="PermissionBoundaryPolicy",
            statements=[
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=["s3:*"],
                    resources=["*"],
                ),
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=["sns:*"],
                    resources=["*"],
                ),
            ],
        )

        forcePermissionBoundaryAttachment = _iam.PolicyStatement(
            effect=_iam.Effect.DENY,            
            actions=[
                "iam:AttachRolePolicy",
                "iam:CreateRole",
                "iam:DetachRolePolicy",
                "iam:PutRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:PutRolePermissionsBoundary",
            ],
            resources=["*"],
        )
        forcePermissionBoundaryAttachment.add_condition(
            "StringNotLike",
            {
                "iam:PermissionsBoundary": "arn:aws:iam::*:policy/PermissionBoundaryPolicy"
            },
        )

        allowIAMReadPolicies = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW,
            actions=[
                "iam:GetPolicyVersion",
                "iam:ListPolicyTags",
                "iam:GetPolicy",
                "iam:ListEntitiesForPolicy",
                "iam:ListPolicyVersions",
            ],
            resources=[
                "arn:aws:iam::*:policy/TechLeadLambda*",
                "arn:aws:iam::*:policy/PermissionBoundaryPolicy",
            ],
        )

        allowIAMPolicies = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW,
            actions=[
                "iam:UpdateAssumeRolePolicy",
                "iam:ListRoleTags",
                "iam:PutRolePermissionsBoundary",
                "iam:TagRole",
                "iam:DeletePolicy",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy",
                "iam:PassRole",
                "iam:DetachRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListRolePolicies",
                "iam:CreatePolicyVersion",
                "iam:GetRole",
                "iam:DeleteRole",
                "iam:UpdateRoleDescription",
                "iam:TagPolicy",
                "iam:CreatePolicy",
                "iam:UpdateRole",
                "iam:GetRolePolicy",
                "iam:ListInstanceProfilesForRole",
            ],
            resources=[                
                "arn:aws:iam::*:role/LambdaRole*",
                "arn:aws:iam::*:policy/TechLeadLambda*",
            ],
        )

        allowIAMList = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW,
            actions=["iam:ListPolicies", "iam:ListRoles"],
            resources=[
                "*",
            ],
        )

        denyPermissionBoundaryEdition = _iam.PolicyStatement(
            effect=_iam.Effect.DENY,
            actions=[
                "iam:DeletePolicy",
                "iam:CreatePolicyVersion",
                "iam:CreatePolicy",
                "iam:DeletePolicyVersion",
                "iam:SetDefaultPolicyVersion",
            ],
            resources=["arn:aws:iam::*:policy/PermissionBoundaryPolicy"],
        )

        techLeadPolicy = _iam.Policy(
            self,
            "TechLeadPolicy",
            policy_name="TechLeadPolicy",
            statements=[
                forcePermissionBoundaryAttachment,
                allowIAMPolicies,
                allowIAMList,
                allowIAMReadPolicies,
                denyPermissionBoundaryEdition,
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=["lambda:*"],
                    resources=["*"],
                ),
            ],
        )

        role = _iam.Role(
            self,
            "TechLeadRole",
            assumed_by=_iam.AccountPrincipal(account_id=self.account),
            inline_policies={
                "TechLeadInlinePolicy": _iam.PolicyDocument(
                    statements=[
                        forcePermissionBoundaryAttachment,
                        allowIAMPolicies,
                        allowIAMList,
                        allowIAMReadPolicies,
                        denyPermissionBoundaryEdition,
                        _iam.PolicyStatement(
                            effect=_iam.Effect.ALLOW,
                            actions=["lambda:*"],
                            resources=["*"],
                        ),
                    ]
                )
            },
            role_name="TechLeadRole",
        )

        techleadLambdaPolicy = _iam.ManagedPolicy(
            self,
            "TechLeadLambda",
            managed_policy_name="TechLeadLambdaPolicy",
            statements=[
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=["sqs:*"],
                    resources=["*"],
                ),
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=["s3:*"],
                    resources=["*"],
                ),
            ],
        )

        # create a lambda function
        _lambda.Function(
            self,
            "PermissionBoundaryHandler",
            function_name="PermissionBoundary",
            description="Permission Boundary Handler",
            runtime=_lambda.Runtime.PYTHON_3_13,
            code=_lambda.Code.from_asset("lambda"),
            handler="permissionBoundary.lambda_handler",
        )

        CfnOutput(
            self,
            "PermissionBoundaryPolicyArn",
            value=permission_boundary_policy.managed_policy_arn,
            description="Permission Boundary Policy ARN",
        )

        CfnOutput(
            self,
            "TechLeadLambdaPolicyArn",
            value=techleadLambdaPolicy.managed_policy_arn,
            description="Techlead Lambda Policy ARN",
        )
