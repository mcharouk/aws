from aws_cdk import RemovalPolicy, Stack
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3  # Duration,
from constructs import Construct


class S3ReplicationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        base_bucket_name = "mcc-s3replicationdemo"
        primary_bucket_name = f"{base_bucket_name}-primary-65757847"
        secondary_bucket_name = f"{base_bucket_name}-secondary-86758837"

        # create bucket with versioning enabled
        primary_bucket = self.create_bucket(primary_bucket_name)
        secondary_bucket = self.create_bucket(secondary_bucket_name)

        # create a role for S3 replication
        replication_role = iam.Role(
            self,
            "ReplicationRole",
            role_name="s3-replication-role",
            assumed_by=iam.ServicePrincipal("s3.amazonaws.com"),
            description="Role for S3 replication",
        )

        # add a policy for S3 replication
        replication_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:GetReplicationConfiguration",
                    "s3:ListBucket",
                ],
                resources=[primary_bucket.bucket_arn],
            )
        )
        replication_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:GetObjectVersionForReplication",
                    "s3:GetObjectVersionAcl",
                    "s3:GetObjectVersionTagging",
                ],
                resources=[primary_bucket.arn_for_objects("*")],
            )
        )

        replication_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:ReplicateObject",
                    "s3:ReplicateDelete",
                    "s3:ReplicateTags",
                ],
                resources=[secondary_bucket.arn_for_objects("*")],
            )
        )

    def create_bucket(self, bucket_name):
        return s3.Bucket(
            self,
            bucket_name,
            bucket_name=bucket_name,
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
