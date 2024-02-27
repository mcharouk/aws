import boto3
from botocore.exceptions import ClientError
from cdk.StackConfig import StackConfig

stackConfig = StackConfig()
## check id dynamo table exists
lambda_name = stackConfig.lambdaName
bucket_name = stackConfig.bucketName

# delete lambda function
lambda_client = boto3.client("lambda")
s3 = boto3.client("s3", region_name="eu-west-3")

if stackConfig.generate_lambda == False:
    try:
        response = lambda_client.delete_function(FunctionName=lambda_name)
        print("lambda function {0} deleted".format(lambda_name))

        # delete S3 notification rules
        response = s3.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration={"LambdaFunctionConfigurations": []},
        )
        print("S3 notification rules deleted")

    except ClientError as e:
        print("lambda function {0} not found".format(lambda_name))

response = s3.list_object_versions(Bucket=bucket_name)
# delete all objects in S3 bucket

if "Versions" in response:
    for version in response["Versions"]:
        s3.delete_object(
            Bucket=bucket_name,
            Key=version["Key"],
            VersionId=version["VersionId"],
        )
        print(f"Deleted {version['Key']} version {version['VersionId']}")
    print("All objects deleted successfully!")
else:
    print("No objects found in the bucket.")
