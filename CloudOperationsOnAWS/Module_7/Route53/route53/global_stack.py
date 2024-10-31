from aws_cdk import CfnOutput, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from constructs import Construct


class GlobalStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # create a vpc with one private subnet

        helloFromRegion_lambda_role = self.createRole(
            "HelloFromRegionLambdaRole",
            iam.ServicePrincipal("lambda.amazonaws.com"),
            [],
        )

        self.addManagedPolicy(
            helloFromRegion_lambda_role, "service-role/AWSLambdaBasicExecutionRole"
        )

    def addManagedPolicy(self, role, policyName):
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(policyName)
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

        return role

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy
