import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client("dynamodb")
## check id dynamo table exists
table_name = "demo_employee"
bucket_name = "eventnotification-demo-457663"

try:
    response = dynamodb.describe_table(TableName=table_name)
    dynamodb.delete_table(TableName=table_name)
except ClientError as error:
    if error.response["Error"]["Code"] == "ResourceNotFoundException":
        print("Dynamotable does not exist")
    else:
        raise error


s3 = boto3.client("s3", region_name="eu-west-3")

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
