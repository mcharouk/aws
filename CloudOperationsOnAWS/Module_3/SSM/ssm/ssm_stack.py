from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import CfnOutput, RemovalPolicy
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_logs as logs
from aws_cdk import aws_s3 as s3
from constructs import Construct
from StackConfig import StackConfig


class SsmStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stackConfig = StackConfig()

        sessionLoggingBucketName = stackConfig.sessionLoggingBucketName
        sessionLoggingKeyPrefix = stackConfig.sessionLoggingKeyPrefix

        session_logging_bucket = s3.Bucket(
            self,
            sessionLoggingBucketName,
            bucket_name=sessionLoggingBucketName,
            encryption=s3.BucketEncryption.S3_MANAGED,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # create cloudwatch log group
        logs.LogGroup(
            self,
            "SSM-Session-Logging",
            log_group_name="ssm-session-logging",
            removal_policy=RemovalPolicy.DESTROY,
        )

        # get default VPC
        vpc = ec2.Vpc.from_lookup(
            self,
            "VPC",
            is_default=True,
        )
        # The code that defines your stack goes here

        securityGroup = ec2.SecurityGroup(
            self,
            "SSMRestricted",
            security_group_name="SSMRestricted",
            description="minimum rules to make work SSM",
            disable_inline_rules=True,
            vpc=vpc,
            allow_all_outbound=False,
        )
        securityGroup.add_egress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(443),
            description="Allow all outbound https traffic",
        )

        role = iam.Role(
            self,
            "SSMInstance",
            role_name="SSMInstance",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        policy = self.createSessionManagerPolicy(
            sessionLoggingBucketName, sessionLoggingKeyPrefix
        )

        policy.attach_to_role(role)

        instance_name = "SSM-Demo-Instance"
        amzn_windows = ec2.MachineImage.latest_windows(
            version=ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE
        )

        # create ec2 key pair
        key_pair = ec2.KeyPair(self, "ssm-windows", key_pair_name="ssm-windows")

        instance = ec2.Instance(
            self,
            instance_name,
            instance_name=instance_name,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            machine_image=amzn_windows,
            vpc=vpc,
            role=role,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=securityGroup,
            key_pair=key_pair,
        )

        local_port = "54321"
        ssm_pf_cmd = 'aws ssm start-session --target {0} --document-name AWS-StartPortForwardingSession --parameters "localPortNumber={1}, portNumber=3389" --region eu-west-3'.format(
            instance.instance_id, local_port
        )
        CfnOutput(self, "InstanceId", value=instance.instance_id)
        CfnOutput(self, "rdpHost", value="localhost:{0}".format(local_port))
        CfnOutput(self, "ssm-pf-cmd", value=ssm_pf_cmd)
        CfnOutput(
            self, "user-name", value="{0}\\Administrator".format(instance.instance_id)
        )
        CfnOutput(
            self,
            "session-logging-bucket-name",
            value=session_logging_bucket.bucket_name,
        )

    def createSessionManagerPolicy(self, bucketName, keyPrefix):
        s3loggingAccessStatement = iam.PolicyStatement(
            sid="s3SessionLoggingAccess",
            effect=iam.Effect.ALLOW,
            actions=["s3:PutObject"],
            resources=["arn:aws:s3:::{0}/{1}/*".format(bucketName, keyPrefix)],
        )

        s3AllResourcesStatement = iam.PolicyStatement(
            sid="s3AllAccess",
            effect=iam.Effect.ALLOW,
            actions=["s3:GetEncryptionConfiguration"],
            resources=["*"],
        )

        cloudwatchResourcesStatement = iam.PolicyStatement(
            sid="cloudWatchAllAccess",
            effect=iam.Effect.ALLOW,
            actions=[
                "logs:CreateLogStream",
                "logs:DescribeLogStreams",
                "logs:DescribeLogGroups",
                "logs:PutLogEvents",
            ],
            resources=["*"],
        )

        return self.createPolicy(
            "ssmCustomPolicy",
            [
                s3loggingAccessStatement,
                s3AllResourcesStatement,
                cloudwatchResourcesStatement,
            ],
        )

    def createPolicy(self, policyName, policyStatements):
        policy = iam.Policy(
            self,
            policyName,
            statements=policyStatements,
        )
        return policy
