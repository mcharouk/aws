import aws_cdk as core
import aws_cdk.assertions as assertions

from transit_gateway.transit_gateway_stack import TransitGatewayStack

# example tests. To run these tests, uncomment this file along with the example
# resource in transit_gateway/transit_gateway_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TransitGatewayStack(app, "transit-gateway")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
