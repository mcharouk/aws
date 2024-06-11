import aws_cdk as core
import aws_cdk.assertions as assertions

from service_catalog.service_catalog_stack import ServiceCatalogStack

# example tests. To run these tests, uncomment this file along with the example
# resource in service_catalog/service_catalog_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServiceCatalogStack(app, "service-catalog")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
