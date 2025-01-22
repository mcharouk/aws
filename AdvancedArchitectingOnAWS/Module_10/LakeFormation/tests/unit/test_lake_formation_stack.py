import aws_cdk as core
import aws_cdk.assertions as assertions

from lake_formation.lake_formation_stack import LakeFormationStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lake_formation/lake_formation_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LakeFormationStack(app, "lake-formation")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
