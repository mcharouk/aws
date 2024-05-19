import aws_cdk as core
import aws_cdk.assertions as assertions

from TechEssentials.Module_2.module_2.module_2_stack import Module1Stack


# example tests. To run these tests, uncomment this file along with the example
# resource in module_1/module_1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Module1Stack(app, "module-1")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
