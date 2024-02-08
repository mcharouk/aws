import boto3
from botocore.exceptions import ClientError

## check id dynamo table exists
lambda_name = "DynamoDB-S3Feeder"

# delete lambda function
client = boto3.client("lambda")
try:
    response = client.delete_function(FunctionName=lambda_name)
    print("lambda function deleted")
except ClientError as e:
    print(e)
    print("lambda function not found")
