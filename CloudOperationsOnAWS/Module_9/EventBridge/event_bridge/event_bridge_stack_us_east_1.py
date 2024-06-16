from aws_cdk import RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_cloudtrail as cloudtrail
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from constructs import Construct
from event_bridge.StackConfig import StackConfig


class EventBridgeStackUsEast1(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stackConfig = StackConfig()

        role = self.createRole(
            "EventBridgeInvokeEventBusRole",
            iam.ServicePrincipal("events.amazonaws.com"),
            [self.createEventBridgePolicy(stackConfig=stackConfig)],
        )
        # create an S3 bucket
        bucket = s3.Bucket(
            self,
            "CloudTrailBucket",
            bucket_name=stackConfig.s3_cloudTrailBucketName,
        )
        bucket.apply_removal_policy(RemovalPolicy.DESTROY)

        # create a cloudtrail trail
        cloudtrail.Trail(
            self,
            "Cloudtrail",
            trail_name="management-events",
            bucket=bucket,
            enable_file_validation=False,
        )

        # create an event bridge rule
        rootConnectionRules = events.Rule(
            self,
            "Rule",
            rule_name="root-signin",
            event_pattern=events.EventPattern(
                source=["aws.signin"],
                detail_type=["AWS Console Sign In via CloudTrail"],
                detail={"userIdentity": {"type": ["Root"]}},
            ),
        )

        rootConnectionRules.add_target(
            targets.EventBus(
                events.EventBus.from_event_bus_arn(
                    self,
                    "eventBusParisTarget",
                    event_bus_arn=f"arn:aws:events:eu-west-3:{stackConfig.aws_accountId}:event-bus/default",
                ),
                role=role,
            )
        )

    def createEventBridgePolicy(self, stackConfig):
        invokeEventBusPolicyStatement = iam.PolicyStatement(
            sid="invokeEventBusPolicyStatement",
            effect=iam.Effect.ALLOW,
            actions=["events:PutEvents"],
            resources=[
                f"arn:aws:events:eu-west-3:{stackConfig.aws_accountId}:event-bus/default"
            ],
        )

        return self.createPolicy(
            "EventBridgeInvokeEventBusPolicy",
            [invokeEventBusPolicyStatement],
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
