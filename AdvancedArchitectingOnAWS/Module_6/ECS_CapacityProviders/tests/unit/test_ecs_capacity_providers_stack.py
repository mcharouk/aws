import aws_cdk as core
import aws_cdk.assertions as assertions

from ecs_capacity_providers.ecs_capacity_providers_stack import EcsCapacityProvidersStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ecs_capacity_providers/ecs_capacity_providers_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EcsCapacityProvidersStack(app, "ecs-capacity-providers")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
