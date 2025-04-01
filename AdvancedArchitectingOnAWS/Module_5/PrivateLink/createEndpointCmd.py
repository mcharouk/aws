import json

import boto3
import utils

utils.change_current_directory()

region_file_name = "region.json"

# read region.json file
# file content is like this {"region": "region_name"}
# get region name in local variable
with open(region_file_name, "r") as f:
    region_name_content = f.read()
    region_name = json.loads(region_name_content)["region"]

with open("region.json", "r") as f:
    region = f.read()


CfStackName = "PrivateLinkStack"
clientVpcIdCfnOutputKey = "ClientVPCId"
EndpointSgIdCfnOutputKey = "PrivateLinkEndpointSgId"

# get cloudformation outputs

cf = boto3.client("cloudformation", region_name=region_name)
ec2 = boto3.client("ec2", region_name=region_name)


def find_stack(stack_name):
    try:
        return cf.describe_stacks(StackName=stack_name)
    except:
        print("Stack not found")
        return None


stack = find_stack(CfStackName)

outputs = stack["Stacks"][0]["Outputs"]

client_vpc_id = None
endpoint_sg_id = None
for output in outputs:
    if output["OutputKey"] == clientVpcIdCfnOutputKey:
        client_vpc_id = output["OutputValue"]
    if output["OutputKey"] == EndpointSgIdCfnOutputKey:
        endpoint_sg_id = output["OutputValue"]

endpoint_service_name = "private-link-demo-service-endpoint"
# get service name of endpoint service

endpoint_service = ec2.describe_vpc_endpoint_services(
    Filters=[{"Name": "tag:Name", "Values": [endpoint_service_name]}]
)
endpoint_service_name = endpoint_service["ServiceDetails"][0]["ServiceName"]

# get all subnet ids of client vpc
client_vpc = ec2.describe_subnets(
    Filters=[{"Name": "vpc-id", "Values": [client_vpc_id]}]
)
client_vpc_subnets = client_vpc["Subnets"]
client_vpc_subnet_ids = [subnet["SubnetId"] for subnet in client_vpc_subnets]
# join subnets ids with empty space
client_vpc_subnet_ids = " ".join(client_vpc_subnet_ids)

vpc_endpoint_name = "private-link-demo-service"

vpc_endpoint_cmd = f""" aws ec2 create-vpc-endpoint \\
--vpc-id {client_vpc_id} \\
--service-name {endpoint_service_name} \\
--vpc-endpoint-type Interface \\
--subnet-ids {client_vpc_subnet_ids} \\
--security-group-ids {endpoint_sg_id} \\
--region {region_name} \\
--tag-specifications 'ResourceType=vpc-endpoint,Tags=[{{Key=Name,Value={vpc_endpoint_name}}}]' \
"""
print(vpc_endpoint_cmd)

cf.close()
ec2.close()
