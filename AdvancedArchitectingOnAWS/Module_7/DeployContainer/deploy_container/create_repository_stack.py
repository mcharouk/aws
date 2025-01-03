from aws_cdk import RemovalPolicy, Stack
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from constructs import Construct


class CreateRepositoryStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repository_name = "cicd-sample-app"
        repository = ecr.Repository(
            self,
            "cicd-sample-app-repository",
            repository_name=repository_name,
            removal_policy=RemovalPolicy.DESTROY,
        )

        artifact_bucket_name = "aws-training-marccharouk-cicd-artifacts"
        artifact_bucket = s3.Bucket(
            self,
            "cicd-sample-app-artifact-bucket",
            bucket_name=artifact_bucket_name,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        codebuild_policy = self.createPolicy(
            "ECS-CICD-CodeBuildPolicy",
            policyStatements=[
                iam.PolicyStatement(
                    sid="UploadToECR",
                    effect=iam.Effect.ALLOW,
                    actions=[
                        "ecr:CompleteLayerUpload",
                        "ecr:UploadLayerPart",
                        "ecr:InitiateLayerUpload",
                        "ecr:BatchCheckLayerAvailability",
                        "ecr:PutImage",
                        "ecr:GetAuthorizationToken",
                    ],
                    resources=[repository.repository_arn],
                ),
                iam.PolicyStatement(
                    sid="GetAuthorizationToken",
                    effect=iam.Effect.ALLOW,
                    actions=["ecr:GetAuthorizationToken"],
                    resources=["*"],
                ),
                iam.PolicyStatement(
                    sid="AccessToCloudWatchLogs",
                    effect=iam.Effect.ALLOW,
                    actions=[
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents",
                    ],
                    resources=["*"],
                ),
                iam.PolicyStatement(
                    sid="AccessToS3Artifacts",
                    effect=iam.Effect.ALLOW,
                    actions=[
                        "s3:PutObject",
                        "s3:GetObject",
                        "s3:GetObjectVersion",
                        "s3:GetBucketAcl",
                        "s3:GetBucketLocation",
                    ],
                    resources=[
                        artifact_bucket.bucket_arn,
                        f"{artifact_bucket.bucket_arn}/*",
                    ],
                ),
            ],
        )

        self.createRole(
            "ECS-CICD-CodeBuildServiceRole",
            iam.ServicePrincipal("codebuild.amazonaws.com"),
            [codebuild_policy],
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
