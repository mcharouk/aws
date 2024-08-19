import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_explorer.aws_explorer_stack import AwsExplorerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_explorer/aws_explorer_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsExplorerStack(app, "aws-explorer")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
