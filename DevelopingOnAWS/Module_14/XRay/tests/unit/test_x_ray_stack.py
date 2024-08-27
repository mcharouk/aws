import aws_cdk as core
import aws_cdk.assertions as assertions

from x_ray.x_ray_stack import XRayStack

# example tests. To run these tests, uncomment this file along with the example
# resource in x_ray/x_ray_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = XRayStack(app, "x-ray")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
