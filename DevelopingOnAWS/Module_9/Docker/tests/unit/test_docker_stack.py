import aws_cdk as core
import aws_cdk.assertions as assertions

from docker.docker_stack import DockerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in docker/docker_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DockerStack(app, "docker")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
