from aws_cdk import CfnOutput, CfnTag, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_networkfirewall as nf
from constructs import Construct


class NetworkFirewallStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc_ip_addresses_range = "10.0.0.0/16"
        vpc = ec2.Vpc(
            self,
            "VPC",
            ip_addresses=ec2.IpAddresses.cidr(vpc_ip_addresses_range),
            vpc_name="Network-firewall-VPC",
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Firewall",
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=24,
                ),
            ],
        )

        # create a stateful rule that block all traffic that does not come from France
        block_youtube_https = nf.CfnRuleGroup.StatefulRuleProperty(
            action="DROP",
            header=nf.CfnRuleGroup.HeaderProperty(
                destination="ANY",
                destination_port="443",
                direction="FORWARD",
                protocol="TCP",
                source=vpc_ip_addresses_range,
                source_port="ANY",
            ),
            rule_options=[
                nf.CfnRuleGroup.RuleOptionProperty(keyword="sid:3"),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="rev:1"),
                nf.CfnRuleGroup.RuleOptionProperty(
                    keyword='msg:"Block youtube.com HTTPS"'
                ),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="flow:to_server"),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="tls.sni"),
                nf.CfnRuleGroup.RuleOptionProperty(keyword='content:"youtube.com"'),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="startswith"),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="nocase"),
            ],
        )

        block_youtube_http = nf.CfnRuleGroup.StatefulRuleProperty(
            action="DROP",
            header=nf.CfnRuleGroup.HeaderProperty(
                destination="ANY",
                destination_port="80",
                direction="FORWARD",
                protocol="TCP",
                source=vpc_ip_addresses_range,
                source_port="ANY",
            ),
            rule_options=[
                nf.CfnRuleGroup.RuleOptionProperty(keyword="sid:4"),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="rev:1"),
                nf.CfnRuleGroup.RuleOptionProperty(
                    keyword='msg:"Block youtube.com HTTP"'
                ),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="flow:to_server"),
                nf.CfnRuleGroup.RuleOptionProperty(keyword='content:"youtube.com"'),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="http_host"),
            ],
        )

        block_non_fr_inbound = nf.CfnRuleGroup.StatefulRuleProperty(
            action="DROP",
            header=nf.CfnRuleGroup.HeaderProperty(
                destination="ANY",
                destination_port="ANY",
                source="ANY",
                source_port="ANY",
                protocol="IP",
                direction="FORWARD",
            ),
            rule_options=[
                nf.CfnRuleGroup.RuleOptionProperty(keyword="sid:6"),
                nf.CfnRuleGroup.RuleOptionProperty(keyword="rev:1"),
                nf.CfnRuleGroup.RuleOptionProperty(
                    keyword='msg:"Block non-FR inbound"'
                ),
                nf.CfnRuleGroup.RuleOptionProperty(
                    keyword="flow:to_server"  # Only match new connections
                ),
                nf.CfnRuleGroup.RuleOptionProperty(
                    keyword="geoip:src,!FR"  # Block sources not from France
                ),
            ],
        )

        rule_group_demo = nf.CfnRuleGroup(
            self,
            "RuleGroupDemo",
            capacity=100,
            rule_group_name="rule-group-demo",
            type="STATEFUL",
            rule_group=nf.CfnRuleGroup.RuleGroupProperty(
                rules_source=nf.CfnRuleGroup.RulesSourceProperty(
                    stateful_rules=[
                        block_youtube_https,
                        block_youtube_http,
                        block_non_fr_inbound,
                    ],
                )
            ),
        )

        # create a network firewall policy
        firewall_policy = nf.CfnFirewallPolicy(
            self,
            "NetworkFirewallPolicy",
            firewall_policy_name="network-firewall-policy-demo",
            firewall_policy=nf.CfnFirewallPolicy.FirewallPolicyProperty(
                stateless_default_actions=["aws:forward_to_sfe"],
                stateless_fragment_default_actions=["aws:forward_to_sfe"],
                stateful_rule_group_references=[
                    nf.CfnFirewallPolicy.StatefulRuleGroupReferenceProperty(
                        resource_arn=rule_group_demo.attr_rule_group_arn
                    )
                ],
                stateful_engine_options=nf.CfnFirewallPolicy.StatefulEngineOptionsProperty(
                    rule_order="DEFAULT_ACTION_ORDER"
                ),
            ),
        )

        # create a network firewall
        # associate it with subnet whose name is Firewall

        subnets = vpc.select_subnets(subnet_group_name="Firewall")

        nf.CfnFirewall(
            self,
            "NetworkFirewall",
            firewall_name="NetworkFirewall",
            firewall_policy_arn=firewall_policy.attr_firewall_policy_arn,
            subnet_mappings=[
                nf.CfnFirewall.SubnetMappingProperty(
                    subnet_id=subnets.subnets[0].subnet_id
                )
            ],
            vpc_id=vpc.vpc_id,
        )

        securityGroup = self.create_ec2_security_group(vpc)

        with open("./ec2_contents/configure.sh") as f:
            user_data = f.read()

        # create a role for ec2 instance that gives permissions to session manager
        ec2_instance_role = self.createRole(
            "ec2DemoRole", iam.ServicePrincipal("ec2.amazonaws.com"), []
        )

        # attach a managed policy to the role
        ec2_instance_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        # create an EC2 instance
        instance = ec2.Instance(
            self,
            "NFInstanceDemo",
            instance_name="NFInstanceDemo",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            associate_public_ip_address=True,
            vpc=vpc,
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            security_group=securityGroup,
            user_data=ec2.UserData.custom(user_data),
            role=ec2_instance_role,
            vpc_subnets=ec2.SubnetSelection(subnet_group_name="Public"),
        )

        # create default routing table for internet gateway
        # provide tag with name internet-gateway
        ec2.CfnRouteTable(
            self,
            "InternetGatewayRouteTable",
            vpc_id=vpc.vpc_id,
            tags=[CfnTag(key="Name", value="NetworkFirewallStack/VPC/IGW")],
        )

        # Or specifically for your named subnets
        firewall_subnets = vpc.select_subnets(subnet_group_name="Firewall").subnets
        public_subnets = vpc.select_subnets(subnet_group_name="Public").subnets

        # Output Firewall subnet CIDR
        for i, subnet in enumerate(firewall_subnets):
            CfnOutput(
                self,
                f"FirewallSubnet{i}CIDR",
                value=subnet.ipv4_cidr_block,
                description=f"Firewall Subnet {i} CIDR block",
            )

        # Output Public subnet CIDR
        for i, subnet in enumerate(public_subnets):
            CfnOutput(
                self,
                f"PublicSubnet{i}CIDR",
                value=subnet.ipv4_cidr_block,
                description=f"Public Subnet {i} CIDR block",
            )

        # Output VPC CIDR
        CfnOutput(self, "VPC CIDR Block", value=vpc_ip_addresses_range)

        CfnOutput(
            self,
            "InstancePublicDNS",
            value="http://" + instance.instance_public_dns_name,
        )

    def create_ec2_security_group(self, vpc):
        securityGroup = ec2.SecurityGroup(
            self,
            "SecurityGroupEC2Instance",
            security_group_name="SecurityGroupEC2Instance",
            description="EC2 instance SG",
            allow_all_outbound=True,
            vpc=vpc,
        )
        securityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )
        return securityGroup

    def addManagedPolicy(self, role, policyName):
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(policyName)
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
