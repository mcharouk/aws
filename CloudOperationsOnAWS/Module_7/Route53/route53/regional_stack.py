import aws_cdk.aws_elasticloadbalancingv2_targets as targets
from aws_cdk import CfnOutput, Stack, Tags  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_ssm as ssm
from constructs import Construct


class RegionalStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc_cidr_range: str,
        createHelloGeneratorLambda: bool,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # create a vpc with one private subnet

        helloFromRegion_lambda_role = iam.Role.from_role_name(
            self,
            "HelloFromRegionLambdaRole",
            "HelloFromRegionLambdaRole",
        )

        helloGenerator_lambda_role = iam.Role.from_role_name(
            self,
            "HelloGeneratorLambdaRole",
            "HelloGeneratorLambdaRole",
        )

        self.vpc = ec2.Vpc(
            self,
            "VPC",
            vpc_name="Route53DemoVPC",
            ip_addresses=ec2.IpAddresses.cidr(vpc_cidr_range),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=25,
                )
            ],
            enable_dns_support=True,
            enable_dns_hostnames=True,
        )

        albSecGroup = ec2.SecurityGroup(
            self,
            "AlbSG",
            security_group_name="AlbSG",
            description="open ports to contact ALB",
            disable_inline_rules=True,
            vpc=self.vpc,
        )
        albSecGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow all inbound http traffic",
        )

        helloFromRegion_lambda = _lambda.Function(
            self,
            id="HelloFromRegion",
            function_name="HelloFromRegion",
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("HelloFromRegion"),
            handler="lambda_function.lambda_handler",
            role=helloFromRegion_lambda_role,
        )

        alb = elbv2.ApplicationLoadBalancer(
            self,
            id="Route53ALBDemo",
            load_balancer_name="Route53ALBDemo",
            vpc=self.vpc,
            security_group=albSecGroup,
            internet_facing=False,
        )

        listener = alb.add_listener(id="HttpListener", port=80, open=True)
        listener.add_targets(
            id="HelloFromRegionTG",
            targets=[targets.LambdaTarget(helloFromRegion_lambda)],
        )

        if createHelloGeneratorLambda is True:

            lambdaSecGroup = ec2.SecurityGroup(
                self,
                "lambdaSG",
                security_group_name="lambdaSG",
                description="lambda caller SG",
                disable_inline_rules=True,
                vpc=self.vpc,
            )

            dnsKeySsm = "/helloFromRegion/DNSName"

            ssm.StringParameter(
                self,
                "DnsParameter",
                parameter_name=dnsKeySsm,
                string_value=alb.load_balancer_dns_name,
            )

            _lambda.Function(
                self,
                id="HelloGenerator",
                function_name="HelloGenerator",
                runtime=_lambda.Runtime.PYTHON_3_12,
                code=_lambda.Code.from_asset("HelloGeneratorLambda"),
                handler="lambda_function.lambda_handler",
                role=helloGenerator_lambda_role,
                environment={"DNS_NAME_KEY_SSM": dnsKeySsm},
                vpc=self.vpc,
                security_groups=[lambdaSecGroup],
            )

            ssmEndpointSecurityGroup = ec2.SecurityGroup(
                self,
                "SsmVpcEndpointSG",
                security_group_name="SsmVpcEndpointSG",
                description="SecurityGroup For SSM VPC Endpoint",
                disable_inline_rules=True,
                vpc=self.vpc,
            )

            ssmEndpointSecurityGroup.add_ingress_rule(
                peer=ec2.Peer.security_group_id(lambdaSecGroup.security_group_id),
                connection=ec2.Port.tcp(443),
                description="Allow all inbound https traffic from lambda SG",
            )

            # create VPC Endpoint for SSM
            ec2.InterfaceVpcEndpoint(
                self,
                "SsmVpcEndpoint",
                vpc=self.vpc,
                service=ec2.InterfaceVpcEndpointAwsService.SSM,
                subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                ),
                private_dns_enabled=True,
                security_groups=[ssmEndpointSecurityGroup],
                open=True,
                lookup_supported_azs=False,
            )

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
