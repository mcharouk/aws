import aws_cdk as core
import aws_cdk.assertions as assertions

from event_bridge.event_bridge_stack import EventBridgeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in event_bridge/event_bridge_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EventBridgeStack(app, "event-bridge")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
