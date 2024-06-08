# list all lambda functions
# delete all lambda functions

import boto3

client = boto3.client("lambda")

response = client.list_functions()

for function in response["Functions"]:
    print(function["FunctionName"])
    client.delete_function(FunctionName=function["FunctionName"])
    print("Deleted function " + function["FunctionName"])
