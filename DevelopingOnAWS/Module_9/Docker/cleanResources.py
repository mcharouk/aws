import boto3

lambda_client = boto3.client("lambda")
function_name = "LambdaOnDockerDemo"
try:
    response = lambda_client.get_function(FunctionName=function_name)
    lambda_client.delete_function(FunctionName=function_name)
    print(f"Lambda function {function_name} has been deleted.")
except lambda_client.exceptions.ResourceNotFoundException:
    print(f"Lambda function {function_name} does not exist.")


ecr = boto3.client("ecr")

response = ecr.describe_repositories()

if len(response["repositories"]) == 0:
    print("no repositories to delete")

for repo in response["repositories"]:
    print("deleting " + repo["repositoryName"] + " repository")
    ecr.delete_repository(repositoryName=repo["repositoryName"], force=True)
