from aws_cdk import RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct


class AccessPointsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = "accesspointdemo-marccharouk-548675486"
        # The code that defines your stack goes here

        # create an s3 bucket named accesspointdemo-marccharouk-548675486
        bucket = s3.Bucket(
            self,
            "AccessPointDemoBucket",
            bucket_name=bucket_name,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        bucket.add_to_resource_policy(self.createBucketPolicy(bucket=bucket))

        self.uploadObject(bucket, "folder1", "./resources/folder1")
        self.uploadObject(bucket, "folder2", "./resources/folder2")

        accesspoint_folder1_name = "accesspoint-folder1"
        accesspoint_folder2_name = "accesspoint-folder2"
        # create an access point for bucket created above

        role = self.createRole(
            "AccessPointDemoRole",
            iam.AccountPrincipal(self.account),
            [self.createAccessRoleDemoPolicy(accesspoint_folder1_name)],
        )

        self.createAccessPointFolder1(bucket_name, role, accesspoint_folder1_name)
        self.createAccessPointFolder2(bucket_name, role, accesspoint_folder2_name)

    def createAccessPointFolder1(
        self,
        bucket_name,
        human_role,
        accesspoint_folder_name,
    ):
        s3.CfnAccessPoint(
            self,
            f"{accesspoint_folder_name}Demo",
            bucket=bucket_name,
            name=accesspoint_folder_name,
            policy={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": f"arn:aws:iam::{self.account}:role/{human_role.role_name}"
                        },
                        "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
                        "Resource": [
                            f"arn:aws:s3:{self.region}:{self.account}:accesspoint/{accesspoint_folder_name}/object/folder1/*"
                        ],
                    }
                ],
            },
        )

    def createAccessPointFolder2(
        self,
        bucket_name,
        human_role,
        accesspoint_folder_name,
    ):
        s3.CfnAccessPoint(
            self,
            f"{accesspoint_folder_name}Demo",
            bucket=bucket_name,
            name=accesspoint_folder_name,
            policy={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Deny",
                        "Principal": {
                            "AWS": f"arn:aws:iam::{self.account}:role/{human_role.role_name}"
                        },
                        "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
                        "Resource": [
                            f"arn:aws:s3:{self.region}:{self.account}:accesspoint/{accesspoint_folder_name}/object/*"
                        ],
                    }
                ],
            },
        )

    # upload resources/object1.txt to bucket in prefix folder1
    def uploadObject(self, bucket, prefix, file_name):
        s3deploy.BucketDeployment(
            self,
            f"S3Deployment-{prefix}",
            sources=[s3deploy.Source.asset(file_name)],
            destination_bucket=bucket,
            destination_key_prefix=prefix,
        )

    def createBucketPolicy(self, bucket):
        return iam.PolicyStatement(
            sid="ListAccesspoints",
            effect=iam.Effect.ALLOW,
            principals=[iam.AnyPrincipal()],
            actions=[
                "*",
            ],
            resources=[f"{bucket.bucket_arn}", f"{bucket.bucket_arn}/*"],
            conditions={"StringEquals": {"s3:DataAccessPointAccount": self.account}},
        )

    def createAccessRoleDemoPolicy(self, accesspoint_folder1_name):
        listAccessPointsStatement = iam.PolicyStatement(
            sid="ListAccesspoints",
            effect=iam.Effect.ALLOW,
            actions=[
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:ListAccessPoints",
                "s3:ListMultiRegionAccessPoints",
                "s3:GetAccessPoint",
            ],
            resources=["*"],
        )

        """
        getAccessPointsStatement = iam.PolicyStatement(
            sid="GetAccessPoints",
            effect=iam.Effect.ALLOW,
            actions=["s3:GetAccessPoint"],
            resources=["*"],
            conditions={
                "StringLike": {
                    "s3:DataAccessPointArn": f"arn:aws:s3:{self.region}:{self.account}:accesspoint/{accesspoint_folder1_name}"
                }
            },
        )
        """

        return self.createPolicy(
            "AccessPointDemoPolicy",
            [listAccessPointsStatement],
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
