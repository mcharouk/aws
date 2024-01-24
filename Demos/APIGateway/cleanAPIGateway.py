# get WAF web ACL

import boto3

# list all apis of api gateway and remove them
apiGateway = boto3.client("apigateway")

restApis = apiGateway.get_rest_apis()

for restAPI in restApis["items"]:
    print("deleting API Gateway named " + restAPI["name"])
    apiGateway.delete_rest_api(restApiId=restAPI["id"])
