from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from constructs import Construct
from pass_role.StackConfig import StackConfig


class PassRoleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stackConfig = StackConfig()
        self.createRole(
            "Admin-NetworkFirewallPolicyEditorRole",
            iam.ServicePrincipal("lambda.amazonaws.com"),
            [self.createNetworkAdminPolicy()],
        )
        self.createRole(
            "Dev-UpdateProductRole",
            iam.ServicePrincipal("lambda.amazonaws.com"),
            [self.createDeveloperPolicy()],
        )
        self.createRole(
            "DevLambdaAdminRole",
            iam.AccountRootPrincipal(),
            [self.createLambdaFullAccessPolicy(), self.createDevLambdaIamPolicy()],
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

    def createNetworkAdminPolicy(self):
        networkAdminPolicyStatement = iam.PolicyStatement(
            sid="networkAdminPolicy",
            effect=iam.Effect.ALLOW,
            actions=[
                "network-firewall:UpdateFirewallPolicyChangeProtection",
                "network-firewall:AssociateFirewallPolicy",
                "network-firewall:UpdateFirewallPolicy",
                "network-firewall:DeleteFirewallPolicy",
                "network-firewall:CreateFirewallPolicy",
            ],
            resources=["*"],
        )

        return self.createPolicy("networkAdminPolicy", [networkAdminPolicyStatement])

    def createDeveloperPolicy(self):
        updateProductPolicyStatement = iam.PolicyStatement(
            sid="updateProductPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=[
                "sqs:DeleteMessage",
                "dynamodb:PutItem",
                "sqs:ReceiveMessage",
                "sqs:SendMessage",
            ],
            resources=["*"],
        )

        # create an identity based policy that allows read and write from dynamodb

        return self.createPolicy("developerPolicy", [updateProductPolicyStatement])

    def createLambdaFullAccessPolicy(self):
        lambdaFullAccessPolicyStatement = iam.PolicyStatement(
            sid="lambdaFullAccessPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=[
                "lambda:*",
            ],
            resources=["*"],
        )

        return self.createPolicy(
            "lambdaFullAccessPolicy", [lambdaFullAccessPolicyStatement]
        )

    def createDevLambdaIamPolicy(self):
        iamAccessOnAllResourcesStatement = iam.PolicyStatement(
            sid="iamAccessOnAllResources",
            effect=iam.Effect.ALLOW,
            actions=[
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListRolePolicies",
                "iam:ListRoles",
            ],
            resources=["*"],
        )

        iamAccessOnDevResourcesStatement = iam.PolicyStatement(
            sid="iamAccessOnDevResources",
            effect=iam.Effect.ALLOW,
            actions=["iam:PassRole"],
            resources=["*"],
            conditions={
                "StringEquals": {"iam:PassedToService": "lambda.amazonaws.com"}
            },
        )

        return self.createPolicy(
            "devLambdaIamPolicy",
            [iamAccessOnAllResourcesStatement, iamAccessOnDevResourcesStatement],
        )

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy
