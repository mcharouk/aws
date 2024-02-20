import boto3
from botocore.exceptions import ClientError

## check id dynamo table exists
lambda_name = "DynamoDB-S3Feeder"
bucket_name = "eventnotification-demo-457663"

# delete lambda function
client = boto3.client("lambda")
try:
    response = client.delete_function(FunctionName=lambda_name)
    print("lambda function deleted")
except ClientError as e:
    print(e)
    print("lambda function not found")

# delete S3 notification rules
client = boto3.client("s3")
response = client.put_bucket_notification_configuration(
    Bucket=bucket_name,
    NotificationConfiguration={"LambdaFunctionConfigurations": []},
)
print("S3 notification rules deleted")
