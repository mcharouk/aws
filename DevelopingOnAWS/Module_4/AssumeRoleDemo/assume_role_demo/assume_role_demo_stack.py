from aws_cdk import SecretValue, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from constructs import Construct


class AssumeRoleDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3_contractor_role_name = "ContractorS3Role"
        contractor_user_name = "contractor"
        contractor_group_name = "contractorGroup"

        # create a role with full s3 access
        s3ContractorRole = iam.Role(
            self,
            s3_contractor_role_name,
            assumed_by=iam.AccountRootPrincipal(),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
            ],
            role_name=s3_contractor_role_name,
            description="Role with S3 full access",
        )

        # create a group with s3 full access policy
        contractorGroup = iam.Group(
            self,
            contractor_group_name,
            group_name=contractor_group_name,
        )

        # Attach policy with cloudshell full access managed policy and assume s3 contractor role to group
        contractorGroup.attach_inline_policy(
            iam.Policy(
                self,
                "AssumeS3ContractorRolePolicy",
                statements=[
                    iam.PolicyStatement(
                        effect=iam.Effect.ALLOW,
                        actions=["sts:AssumeRole"],
                        resources=[s3ContractorRole.role_arn],
                    )
                ],
            )
        )
        contractorGroup.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AWSCloudShellFullAccess")
        )

        # attach user contractor to group contractorGroup
        contractorUser = iam.User(
            self,
            contractor_user_name,
            user_name=contractor_user_name,
            groups=[contractorGroup],
            password=SecretValue.unsafe_plain_text("Contractor2024!"),
            password_reset_required=False,
        )
