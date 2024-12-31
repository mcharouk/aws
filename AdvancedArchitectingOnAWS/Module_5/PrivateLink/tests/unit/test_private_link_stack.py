import aws_cdk as core
import aws_cdk.assertions as assertions

from private_link.private_link_stack import PrivateLinkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in private_link/private_link_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PrivateLinkStack(app, "private-link")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
