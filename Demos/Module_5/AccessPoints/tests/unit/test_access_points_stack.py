import aws_cdk as core
import aws_cdk.assertions as assertions

from access_points.access_points_stack import AccessPointsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in access_points/access_points_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AccessPointsStack(app, "access-points")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
