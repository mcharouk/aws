import aws_cdk as core
import aws_cdk.assertions as assertions

from static_web_hosting.static_web_hosting_stack import StaticWebHostingStack

# example tests. To run these tests, uncomment this file along with the example
# resource in static_web_hosting/static_web_hosting_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StaticWebHostingStack(app, "static-web-hosting")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
