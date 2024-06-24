from aws_cdk import RemovalPolicy, Stack
from aws_cdk import aws_ec2 as ec2  # Duration,
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from constructs import Construct


class MountPointsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        # create security group for an instance that allows efs access
        instanceSG = ec2.SecurityGroup(
            self,
            id="InstanceSecurityGroup",
            vpc=vpc,
            security_group_name="InstanceSecurityGroup",
            allow_all_outbound=True,
        )

        # create a security group for efs mount points
        mountPointsSG = ec2.SecurityGroup(
            self,
            id="EFSMountPointsSecurityGroup",
            vpc=vpc,
            security_group_name="EFSMountPointsSecurityGroup",
            allow_all_outbound=False,
        )

        mountPointsSG.add_ingress_rule(
            peer=ec2.Peer.security_group_id(instanceSG.security_group_id),
            connection=ec2.Port.tcp(2049),
            description="Allow incoming NFS traffic from EC2 instances",
        )

        mountPointsSG.add_egress_rule(
            peer=ec2.Peer.ipv4(vpc.vpc_cidr_block),
            connection=ec2.Port.tcp(2049),
            description="Allow outgoing NFS traffic to EC2 instances",
        )

        bucket_name = "mountpoint-marccharouk-86758493"
        # The code that defines your stack goes here

        # create an s3 bucket named accesspointdemo-marccharouk-548675486
        bucket = s3.Bucket(
            self,
            "mountPointDemo",
            bucket_name=bucket_name,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        role = self.createRole(
            "EFSInstanceRole",
            iam.ServicePrincipal("ec2.amazonaws.com"),
            [self.createS3MountPointPolicy(bucket.bucket_name)],
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux2023()

        with open("./resources/install-mount-points.sh") as f:
            user_data = f.read()

        ec2.Instance(
            self,
            "MountStorageInstance1",
            instance_name="MountStorageInstance1",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            associate_public_ip_address=True,
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                one_per_az=True,
                subnet_type=ec2.SubnetType.PUBLIC,
                availability_zones=["eu-west-3a"],
            ),
            machine_image=amzn_linux,
            security_group=instanceSG,
            role=role,
            user_data=ec2.UserData.custom(user_data),
        )

        ec2.Instance(
            self,
            "MountStorageInstance2",
            instance_name="MountStorageInstance2",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            associate_public_ip_address=True,
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                one_per_az=True,
                subnet_type=ec2.SubnetType.PUBLIC,
                availability_zones=["eu-west-3b"],
            ),
            machine_image=amzn_linux,
            security_group=instanceSG,
            role=role,
            user_data=ec2.UserData.custom(user_data),
        )

    def createS3MountPointPolicy(self, bucket_name):
        mountpointFullBucketAccess = iam.PolicyStatement(
            sid="MountpointFullBucketAccess",
            effect=iam.Effect.ALLOW,
            actions=["s3:ListBucket"],
            resources=[f"arn:aws:s3:::{bucket_name}"],
        )

        mountpointFullObjectAccess = iam.PolicyStatement(
            sid="MountpointFullObjectAccess",
            effect=iam.Effect.ALLOW,
            actions=[
                "s3:GetObject",
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:DeleteObject",
            ],
            resources=[f"arn:aws:s3:::{bucket_name}/*"],
        )

        return self.createPolicy(
            "S3MountPointPolicy",
            [mountpointFullBucketAccess, mountpointFullObjectAccess],
        )

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy

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
