from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_ssm as ssm  # Duration,
from constructs import Construct


class CommandDocumentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        with open("resources/cloudwatchConfigApache.json", "r") as f:
            content = f.read()
        # The code that defines your stack goes here
        cloudWatchConfigParameter = ssm.StringParameter(
            self,
            "CloudWatchConfigParameter",
            parameter_name="/cloudwatch/agent/config/apache",
            string_value=content,
        )

        vpc = ec2.Vpc.from_lookup(
            self,
            "VPC",
            is_default=True,
        )

        securityGroup = ec2.SecurityGroup(
            self,
            "ApacheServerSecGroup",
            security_group_name="ApacheServerSecGroup",
            description="open ports to contact apache server",
            disable_inline_rules=True,
            vpc=vpc,
        )
        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )

        role = self.createRole(
            "ApacheServerInstanceRole",
            iam.ServicePrincipal("ec2.amazonaws.com"),
            [self.createFleetManagerReadonlyPolicy()],
        )

        self.addManagedPolicy(role, "AmazonSSMManagedInstanceCore")
        self.addManagedPolicy(role, "AmazonSSMPatchAssociation")
        self.addManagedPolicy(role, "CloudWatchAgentServerPolicy")

        amzn_linux = ec2.MachineImage.latest_amazon_linux2023()

        with open("./resources/apacheServerInstallScript.sh") as f:
            user_data = f.read()

        instance = ec2.Instance(
            self,
            "ApacheServer",
            instance_name="ApacheServer",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            role=role,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            vpc=vpc,
            machine_image=amzn_linux,
            security_group=securityGroup,
            user_data=ec2.UserData.custom(user_data),
        )

        CfnOutput(
            self,
            "InstancePublicDNS",
            value="http://" + instance.instance_public_dns_name,
        )

        CfnOutput(
            self,
            "CloudWatchConfigParameterName",
            value=cloudWatchConfigParameter.parameter_name,
        )

    def addManagedPolicy(self, role, policyName):
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(policyName)
        )

    def createFleetManagerReadonlyPolicy(self):
        ec2Statement = iam.PolicyStatement(
            sid="ec2Statement",
            effect=iam.Effect.ALLOW,
            actions=["ec2:DescribeInstances", "ec2:DescribeTags"],
            resources=["*"],
        )

        ssmStatement = iam.PolicyStatement(
            sid="ssmStatement",
            effect=iam.Effect.ALLOW,
            actions=[
                "ssm:DescribeInstanceAssociationsStatus",
                "ssm:DescribeInstancePatches",
                "ssm:DescribeInstancePatchStates",
                "ssm:DescribeInstanceProperties",
                "ssm:GetCommandInvocation",
                "ssm:GetServiceSetting",
                "ssm:GetInventorySchema",
                "ssm:ListComplianceItems",
                "ssm:ListInventoryEntries",
                "ssm:ListTagsForResource",
                "ssm:ListCommandInvocations",
                "ssm:ListAssociations",
            ],
            resources=["*"],
        )

        ssmDocumentStatement = iam.PolicyStatement(
            sid="ssmDocumentStatement",
            effect=iam.Effect.ALLOW,
            actions=["ssm:GetDocument", "ssm:SendCommand", "ssm:StartSession"],
            resources=[
                "arn:aws:ec2:*:*:instance/*",
                "arn:aws:ssm:*:*:managed-instance/*",
                "arn:aws:ssm:*:*:document/SSM-SessionManagerRunShell",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetDiskInformation",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetFileContent",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetFileSystemContent",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetGroups",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetPerformanceCounters",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetProcessDetails",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetUsers",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetWindowsEvents",
                "arn:aws:ssm:*:*:document/AWSFleetManager-GetWindowsRegistryContent",
            ],
            conditions={"BoolIfExists": {"ssm:SessionDocumentAccessCheck": "true"}},
        )

        terminateSessionStatement = iam.PolicyStatement(
            sid="terminateSessionStatement",
            effect=iam.Effect.ALLOW,
            actions=["ssm:TerminateSession"],
            resources=["*"],
            conditions={
                "StringLike": {
                    "ssm:resourceTag/aws:ssmmessages:session-id": ["${aws:userid}"]
                }
            },
        )

        return self.createPolicy(
            "FleetManagerReadonlyPolicy",
            [
                ec2Statement,
                ssmStatement,
                ssmDocumentStatement,
                terminateSessionStatement,
            ],
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
