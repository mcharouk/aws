import aws_cdk as core
import aws_cdk.assertions as assertions

from stackset.stackset_stack import StacksetStack

# example tests. To run these tests, uncomment this file along with the example
# resource in stackset/stackset_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StacksetStack(app, "stackset")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
