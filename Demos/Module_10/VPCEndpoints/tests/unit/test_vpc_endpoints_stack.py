import aws_cdk as core
import aws_cdk.assertions as assertions

from vpc_endpoints.vpc_endpoints_stack import VpcEndpointsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in vpc_endpoints/vpc_endpoints_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = VpcEndpointsStack(app, "vpc-endpoints")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
