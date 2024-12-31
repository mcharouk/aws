import boto3

client = boto3.client("ec2")

endpoint_name = "private-link-demo-service"

# get endpoint with name private-link-demo-service and delete it
vpc_endpoints = client.describe_vpc_endpoints(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": [endpoint_name],
        },
    ],
)

if len(vpc_endpoints["VpcEndpoints"]) > 0:
    endpoint_id = vpc_endpoints["VpcEndpoints"][0]["VpcEndpointId"]
    client.delete_vpc_endpoints(VpcEndpointIds=[endpoint_id])
    print(f"Endpoint with ID [{endpoint_id}] removed")
else:
    print(f"Endpoint {endpoint_name} not found")


endpoint_service_name = "private-link-demo-service-endpoint"
# get endpoint service with name private-link-demo-service-endpoint and delete it
endpoint_services = client.describe_vpc_endpoint_service_configurations(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": [endpoint_service_name],
        },
    ],
)

if len(endpoint_services["ServiceConfigurations"]) > 0:
    endpoint_service_id = endpoint_services["ServiceConfigurations"][0]["ServiceId"]
    client.delete_vpc_endpoint_service_configurations(ServiceIds=[endpoint_service_id])
    print(f"Endpoint service with ID [{endpoint_service_id}] removed")
else:
    print(f"Endpoint service {endpoint_service_name} not found")

client.close()
