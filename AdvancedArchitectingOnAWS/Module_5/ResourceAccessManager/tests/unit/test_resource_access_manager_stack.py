import aws_cdk as core
import aws_cdk.assertions as assertions

from resource_access_manager.resource_access_manager_stack import ResourceAccessManagerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in resource_access_manager/resource_access_manager_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ResourceAccessManagerStack(app, "resource-access-manager")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
