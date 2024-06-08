import aws_cdk as core
import aws_cdk.assertions as assertions

from image_builder.image_builder_stack import ImageBuilderStack

# example tests. To run these tests, uncomment this file along with the example
# resource in image_builder/image_builder_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ImageBuilderStack(app, "image-builder")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
