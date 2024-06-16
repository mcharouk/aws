from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_sns as sns
from constructs import Construct
from event_bridge.StackConfig import StackConfig


class EventBridgeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stackConfig = StackConfig()

        # create an sns topic
        snsTopic = sns.Topic(self, "RootAccessTopic", topic_name="root-access-topic")

        # create a mail subscription
        sns.Subscription(
            self,
            "mailSubscription",
            topic=snsTopic,
            protocol=sns.SubscriptionProtocol.EMAIL,
            endpoint=stackConfig.sns_mail,
        )
