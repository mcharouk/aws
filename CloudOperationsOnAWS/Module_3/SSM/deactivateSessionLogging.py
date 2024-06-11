import boto3
from StackConfig import StackConfig

# get output named session-logging-bucket-name from cloudformation template named SsmStack

stackConfig = StackConfig()

sessionLoggingBucketName = stackConfig.sessionLoggingBucketName

# empty bucket named sessionLoggingBucketName
s3 = boto3.resource("s3")
bucket = s3.Bucket(sessionLoggingBucketName)
bucket.objects.all().delete()
print("bucket {0} has been cleaned".format(sessionLoggingBucketName))

client = boto3.client("ssm")

# update document named SSM-SessionManagerRunShell with deactivateSessionLogging.json content

response = client.update_document(
    Name="SSM-SessionManagerRunShell",
    Content=open("deactivateSessionLogging.json", "r").read(),
    DocumentFormat="JSON",
    DocumentVersion="$LATEST",
)
print("session logging has been deactivated")
