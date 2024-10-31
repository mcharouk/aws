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
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # create a vpc with one private subnet

        helloFromRegion_lambda_role = iam.Role.from_role_name(
            self,
            "HelloFromRegionLambdaRole",
            "HelloFromRegionLambdaRole",
        )

        self.vpc = ec2.Vpc(
            self,
            "VPC",
            vpc_name="Route53DemoVPC",
            ip_addresses=ec2.IpAddresses.cidr(vpc_cidr_range),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PublicSubnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
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
            internet_facing=True,
        )

        listener = alb.add_listener(id="HttpListener", port=80, open=True)

        # add lambda target group to default rule
        listener.add_targets(
            id="HelloFromRegionTarget",
            targets=[
                targets.LambdaTarget(helloFromRegion_lambda),
            ],
        )

        ## create an output with load balancer dns name
        CfnOutput(self, "albDnsName", value="http://" + alb.load_balancer_dns_name)
