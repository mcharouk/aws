from aws_cdk import RemovalPolicy, Size, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_efs as efs
from constructs import Construct


class BackupStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create an EBS volume in eu-west-3 region
        volume = ec2.Volume(
            self,
            "MyEBSVolume",
            availability_zone="eu-west-3a",
            size=Size.gibibytes(1),
            encrypted=False,
            volume_type=ec2.EbsDeviceVolumeType.GP3,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # create an EFS filesystem in eu-west-3 region
        filesystem = efs.FileSystem(
            self,
            "MyEFSFilesystem",
            vpc=ec2.Vpc.from_lookup(self, "VPC", is_default=True),
            encrypted=False,
            performance_mode=efs.PerformanceMode.GENERAL_PURPOSE,
            removal_policy=RemovalPolicy.DESTROY,
        )
