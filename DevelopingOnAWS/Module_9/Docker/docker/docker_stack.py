from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from constructs import Construct


class DockerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.createRole(
            roleName="LambdaOnDockerRole",
            principal=iam.ServicePrincipal("lambda.amazonaws.com"),
            policies=[self.createLambdaCloudWatchPolicy()],
        )

    def createLambdaCloudWatchPolicy(self):
        logGroupStatement = iam.PolicyStatement(
            sid="logGroupStatement",
            effect=iam.Effect.ALLOW,
            actions=["logs:CreateLogGroup"],
            resources=[f"arn:aws:logs:{self.region}:*:*"],
        )

        logStreamStatement = iam.PolicyStatement(
            sid="logStreamStatement",
            effect=iam.Effect.ALLOW,
            actions=["logs:CreateLogStream", "logs:PutLogEvents"],
            resources=[f"arn:aws:logs:{self.region}:*:log-group:/aws/lambda/*:*"],
        )

        return self.createPolicy(
            "LambdaCloudWatchPolicy",
            [logGroupStatement, logStreamStatement],
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
