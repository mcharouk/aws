import boto3

cdkBucketNameParis = "cdk-hnb659fds-assets-637423642269-eu-west-3"
cdkBucketNameIreland = "cdk-hnb659fds-assets-637423642269-eu-west-1"


def empty_S3_buckets(region_name, cdk_bucket_name):

    s3 = boto3.client("s3", region_name=region_name)

    response = s3.list_object_versions(Bucket=cdk_bucket_name)

    # delete all s3 object version
    if "Versions" in response:
        for version in response["Versions"]:
            s3.delete_object(
                Bucket=cdk_bucket_name,
                Key=version["Key"],
                VersionId=version["VersionId"],
            )
            print(
                f"Deleted {version['Key']} version {version['VersionId']} in region {region_name}"
            )
    else:
        print("No Versions to delete in region {0}".format(region_name))

    # delete all s3 object
    if "DeleteMarkers" in response:
        for obj in response["DeleteMarkers"]:
            s3.delete_object(
                Bucket=cdk_bucket_name, Key=obj["Key"], VersionId=obj["VersionId"]
            )
            print(
                f"Deleted {obj['Key']} version {obj['VersionId']} in region {region_name}"
            )
    else:
        print("No delete markers to delete in region {0}".format(region_name))


def purge_cloudwatch_log_groups(region_name):
    logs = boto3.client("logs", region_name=region_name)
    # list all cloudwatch log groups
    log_groups = logs.describe_log_groups()

    if "logGroups" in log_groups:
        if len(log_groups["logGroups"]) == 0:
            print("No log groups to delete in region {0}".format(region_name))
        for group in log_groups["logGroups"]:
            print(f"Deleting {group['logGroupName']} in region {region_name}")
            logs.delete_log_group(logGroupName=group["logGroupName"])
    else:
        print("No log groups to delete in region {0}".format(region_name))


empty_S3_buckets(region_name="eu-west-3", cdk_bucket_name=cdkBucketNameParis)
purge_cloudwatch_log_groups(region_name="eu-west-3")

empty_S3_buckets(region_name="eu-west-1", cdk_bucket_name=cdkBucketNameIreland)
purge_cloudwatch_log_groups(region_name="eu-west-1")
