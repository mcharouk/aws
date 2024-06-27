# Activate session logging does not work with cloudformation, that's why it must be activated by a python script
import boto3
from StackConfig import StackConfig

# get output named session-logging-bucket-name from cloudformation template named SsmStack

stackConfig = StackConfig()

sessionLoggingBucketName = stackConfig.sessionLoggingBucketName
sessionLoggingKeyPrefix = stackConfig.sessionLoggingKeyPrefix

# replace placeholder DOC-EXAMPLE-BUCKET with sessionLoggingBucketName in file activateSessionLogging.json

with open("activateSessionLogging.json", "r") as file:
    filedata = file.read()
    filedata = filedata.replace("S3-BUCKET-NAME", sessionLoggingBucketName).replace(
        "S3-KEY-PREFIX", sessionLoggingKeyPrefix
    )

# update document named SSM-SessionManagerRunShell with filedata content with latest version

client = boto3.client("ssm")

response = client.update_document(
    Name="SSM-SessionManagerRunShell",
    Content=filedata,
    DocumentFormat="JSON",
    DocumentVersion="$LATEST",
)

print("session logging has been activated")
