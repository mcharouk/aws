import aws_cdk as core
import aws_cdk.assertions as assertions

from q_business.q_business_stack import QBusinessStack

# example tests. To run these tests, uncomment this file along with the example
# resource in q_business/q_business_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = QBusinessStack(app, "q-business")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
