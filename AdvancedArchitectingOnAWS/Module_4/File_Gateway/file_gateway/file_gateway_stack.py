from aws_cdk import CfnOutput, RemovalPolicy, Stack
from aws_cdk import aws_ec2 as ec2  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_iam as iam  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_s3 as s3
from constructs import Construct


class FileGatewayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        default_vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)
        # create an EC2 instance used as a file gateway in defaault VPC
        # create a new security group that allows NFS access
        file_gateway_sg = ec2.SecurityGroup(
            self,
            "FileGatewaySG",
            security_group_name="FileGatewayApplianceSG",
            vpc=default_vpc,
            description="Allow NFS access to the file gateway",
            allow_all_outbound=True,
        )
        # NFS required ports
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(2049), "Allow NFS access"
        )
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(111), "Allow NFS portmapper"
        )
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(20048), "Allow NFS mount"
        )

        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.udp(2049), "Allow NFS access"
        )
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.udp(111), "Allow NFS portmapper"
        )
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.udp(20048), "Allow NFS mount"
        )

        # Management console access
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow HTTP access to management console",
        )
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(8080),
            "Allow HTTP access to management console",
        )
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "Allow HTTPS access to management console",
        )

        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.DNS_TCP,
            "Allow DNS TCP communication",
        )
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.DNS_UDP,
            "Allow DNS UDP communication",
        )

        # SSH access for management (optional, restrict to specific IP ranges in production)
        file_gateway_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH access"
        )

        file_gateway_ami = ec2.MachineImage.from_ssm_parameter(
            "/aws/service/storagegateway/ami/FILE_S3/latest"
        )

        bucket_name = "training-charouk-filegateway-databucket"

        # create a bucket for file gateway
        bucket = s3.Bucket(
            self,
            "Bucket",
            bucket_name=bucket_name,
            versioned=False,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        # Create the EC2 instance for File Gateway with a secondary EBS storage of 150 Gb
        ec2ApplianceRole = iam.Role(
            self,
            "FileGatewayApplianceRole",
            role_name="FileGatewayApplianceRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSSMManagedInstanceCore"
                )
            ],
        )

        ec2ApplianceRole.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:GetBucketLocation",
                    "s3:ListBucket",
                    "s3:ListBucketMultipartUploads",
                    "s3:AbortMultipartUpload",
                    "s3:DeleteObject",
                    "s3:GetObject",
                    "s3:ListMultipartUploadParts",
                    "s3:PutObject",
                    "s3:GetBucketPolicy",
                ],
                resources=[
                    bucket.bucket_arn,  # For bucket-level permissions
                    bucket.arn_for_objects("*"),  # For object-level permissions
                ],
            )
        )

        ec2ApplianceRole.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW, actions=["storagegateway:*"], resources=["*"]
            )
        )

        ec2ApplianceRole.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "ec2:DescribeNetworkInterfaces",
                    "ec2:DeleteNetworkInterface",
                    "ec2:CreateNetworkInterface",
                ],
                resources=["*"],
            )
        )

        file_gateway = ec2.Instance(
            self,
            "FileGatewayAppliance",
            instance_name="FileGatewayAppliance",
            instance_type=ec2.InstanceType("m5.xlarge"),
            machine_image=file_gateway_ami,
            vpc=default_vpc,
            security_group=file_gateway_sg,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(150, encrypted=False),
                )
            ],
            role=ec2ApplianceRole,
        )

        file_share_role = iam.Role(
            self,
            "FileShareRole",
            role_name="FileShareRole",
            assumed_by=iam.ServicePrincipal("storagegateway.amazonaws.com"),
        )

        file_share_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:GetAccelerateConfiguration",
                    "s3:GetBucketLocation",
                    "s3:GetBucketVersioning",
                    "s3:ListBucket",
                    "s3:ListBucketVersions",
                    "s3:ListBucketMultipartUploads",
                ],
                resources=[
                    bucket.bucket_arn,  # For bucket-level permissions
                ],
            )
        )

        file_share_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:AbortMultipartUpload",
                    "s3:DeleteObject",
                    "s3:DeleteObjectVersion",
                    "s3:GetObject",
                    "s3:GetObjectAcl",
                    "s3:GetObjectVersion",
                    "s3:ListMultipartUploadParts",
                    "s3:PutObject",
                    "s3:PutObjectAcl",
                ],
                resources=[
                    bucket.arn_for_objects("*"),  # For object-level permissions
                ],
            )
        )

        # create a new security group that allows NFS access
        client_sg = ec2.SecurityGroup(
            self,
            "ClientSG",
            vpc=default_vpc,
            description="Allow NFS access to the client",
            allow_all_outbound=True,
            security_group_name="FileGatewayClientSG",
        )

        # create a t2.micro instance that will mount an nfs share from the file gateway
        # attach a role that allows connection with session manager
        client = ec2.Instance(
            self,
            "FileGatewayClient",
            instance_name="FileGatewayClient",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=default_vpc,
            security_group=client_sg,
            role=iam.Role(
                self,
                "FileGatewayClientRole",
                role_name="FileGatewayClientRole",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                managed_policies=[
                    iam.ManagedPolicy.from_aws_managed_policy_name(
                        "AmazonSSMManagedInstanceCore"
                    )
                ],
            ),
        )

        # create an output with ec2 file gateway instance public ip
        CfnOutput(self, "FileGatewayPublicIP", value=file_gateway.instance_public_ip)
