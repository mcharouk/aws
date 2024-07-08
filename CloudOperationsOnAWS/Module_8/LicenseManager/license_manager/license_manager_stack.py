import LicenseConfigurationFactory
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_licensemanager as lim
from constructs import Construct


class LicenseManagerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        license_arn = LicenseConfigurationFactory.get_license_configuration_arn()

        vpc = ec2.Vpc.from_lookup(
            self,
            "VPC",
            is_default=True,
        )

        # get default security group
        securityGroup = ec2.SecurityGroup(
            self,
            "LicenseManagerSG",
            security_group_name="LicenseManagerSG",
            description="security group for EC2 license manager demo",
            disable_inline_rules=True,
            vpc=vpc,
            allow_all_outbound=True,
        )
        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux2023()

        # create an ec2 instance

        ec2.CfnLaunchTemplate(
            self,
            "LicenseDemo",
            launch_template_name="LicenseDemo",
            version_description="1.0.0",
            launch_template_data=ec2.CfnLaunchTemplate.LaunchTemplateDataProperty(
                instance_type="t2.micro",
                image_id=amzn_linux.get_image(self).image_id,
                security_group_ids=[securityGroup.security_group_id],
                license_specifications=[
                    ec2.CfnLaunchTemplate.LicenseSpecificationProperty(
                        license_configuration_arn=license_arn
                    )
                ],
            ),
        )
