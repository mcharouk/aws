# list all lambda functions
# delete all lambda functions

import boto3

client = boto3.client("lambda")

lambda_name = "PassRoleLambdaTest"
response = client.list_functions()

for function in response["Functions"]:
    if function["FunctionName"] != lambda_name:
        continue
    client.delete_function(FunctionName=function["FunctionName"])
    print("Deleted function " + function["FunctionName"])
