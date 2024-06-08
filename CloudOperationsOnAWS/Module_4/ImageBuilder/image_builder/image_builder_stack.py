import aws_cdk.aws_iam as iam
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from constructs import Construct


class ImageBuilderStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        role = iam.Role(
            self,
            "ApacheImageBuilderRole",
            role_name="ApacheImageBuilderRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "EC2InstanceProfileForImageBuilder"
            )
        )

        # create an instance profile to attach the role
        iam.CfnInstanceProfile(
            self,
            "ApacheImageBuilderRoleInstanceProfile",
            instance_profile_name="ApacheImageBuilderRoleInstanceProfile",
            roles=[role.role_name],
        )
