import aws_cdk as core
import aws_cdk.assertions as assertions

from cloud_front_functions.cloud_front_functions_stack import CloudFrontFunctionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cloud_front_functions/cloud_front_functions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CloudFrontFunctionsStack(app, "cloud-front-functions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
