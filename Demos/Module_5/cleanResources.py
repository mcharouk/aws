import boto3

bucketname = "marccharouk-demo-45756383"

# remove all object versions in this bucket and remove it
s3 = boto3.client("s3")

response = s3.list_object_versions(Bucket=bucketname)

# delete all s3 object version
if "Versions" in response:
    for version in response["Versions"]:
        s3.delete_object(
            Bucket=bucketname, Key=version["Key"], VersionId=version["VersionId"]
        )
        print(f"Deleted {version['Key']} version {version['VersionId']}")

else:
    print("No Versions to delete")

# delete all s3 object delete markers
if "DeleteMarkers" in response:
    for marker in response["DeleteMarkers"]:
        s3.delete_object(
            Bucket=bucketname, Key=marker["Key"], VersionId=marker["VersionId"]
        )
        print(f"Deleted {marker['Key']} delete marker {marker['VersionId']}")

else:
    print("No delete markers to delete")

s3.delete_bucket(Bucket=bucketname)
print(f"Deleted bucket {bucketname}")
