import aws_cdk as core
import aws_cdk.assertions as assertions

from command_document.command_document_stack import CommandDocumentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in command_document/command_document_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CommandDocumentStack(app, "command-document")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
