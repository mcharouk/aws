import aws_cdk as core
import aws_cdk.assertions as assertions

from credentials_priority.credentials_priority_stack import CredentialsPriorityStack

# example tests. To run these tests, uncomment this file along with the example
# resource in credentials_priority/credentials_priority_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CredentialsPriorityStack(app, "credentials-priority")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
