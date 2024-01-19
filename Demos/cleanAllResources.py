import boto3

s3 = boto3.client("s3", region_name="eu-west-3")
logs = boto3.client("logs", region_name="eu-west-3")

cdkBucketName = "cdk-hnb659fds-assets-270188911144-eu-west-3"

response = s3.list_object_versions(Bucket=cdkBucketName)

# delete all s3 object version
if "Versions" in response:
    for version in response["Versions"]:
        s3.delete_object(
            Bucket=cdkBucketName, Key=version["Key"], VersionId=version["VersionId"]
        )
        print(f"Deleted {version['Key']} version {version['VersionId']}")
else:
    print("No Versions to delete")

# delete all s3 object
if "DeleteMarkers" in response:
    for obj in response["DeleteMarkers"]:
        s3.delete_object(
            Bucket=cdkBucketName, Key=obj["Key"], VersionId=obj["VersionId"]
        )
        print(f"Deleted {obj['Key']} version {obj['VersionId']}")
else:
    print("No delete markers to delete")


# list all cloudwatch log groups
log_groups = logs.describe_log_groups()

if "logGroups" in log_groups:
    if len(log_groups["logGroups"]) == 0:
        print("No log groups to delete")
    for group in log_groups["logGroups"]:
        print(f"Deleting {group['logGroupName']}")
        boto3.client("logs").delete_log_group(logGroupName=group["logGroupName"])
else:
    print("No log groups to delete")
