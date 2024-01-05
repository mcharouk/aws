import aws_cdk as core
import aws_cdk.assertions as assertions

from step_function.step_function_stack import StepFunctionStack

# example tests. To run these tests, uncomment this file along with the example
# resource in step_function/step_function_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StepFunctionStack(app, "step-function")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
