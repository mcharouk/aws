# get WAF web ACL

import boto3

client = boto3.client("wafv2")

# get ARN of api gateway stage

# get first web acl
response = client.list_web_acls(Scope="REGIONAL")
first_web_acl = response["WebACLs"][0]
# get web acl arn
web_acl_arn = first_web_acl["ARN"]
web_acl_name = first_web_acl["Name"]
web_acl_id = first_web_acl["Id"]
web_acl_lock_token = first_web_acl["LockToken"]


# remove associated resources of web ACL


resources = client.list_resources_for_web_acl(
    WebACLArn=web_acl_arn, ResourceType="API_GATEWAY"
)
api_gateway_arn = resources["ResourceArns"][0]
print("Disassociating API Gateway " + api_gateway_arn)
client.disassociate_web_acl(ResourceArn=api_gateway_arn)

print("Deleting {web_acl_name}".format(web_acl_name=web_acl_name))
client.delete_web_acl(
    Name=web_acl_name, Id=web_acl_id, LockToken=web_acl_lock_token, Scope="REGIONAL"
)
