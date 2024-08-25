import aws_cdk as core
import aws_cdk.assertions as assertions

from sam_demo.sam_demo_stack import SamDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sam_demo/sam_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SamDemoStack(app, "sam-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
