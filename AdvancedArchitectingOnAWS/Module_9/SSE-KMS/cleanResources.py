import boto3

bucket_name = "aws-training-marccharouk-ssekms"
kms_alias_key = "alias/DemoS3Key"

# if bucket exists, empty and delete bucket

s3 = boto3.resource("s3")

if s3.Bucket(bucket_name).creation_date is not None:
    s3.Bucket(bucket_name).objects.all().delete()
    s3.Bucket(bucket_name).delete()
    print("Bucket deleted")

kms_client = boto3.client("kms")
# get key id from key alias

response = kms_client.list_aliases()


def get_key_id(key_alias):
    for alias in response["Aliases"]:
        if alias["AliasName"] == key_alias:
            return alias["TargetKeyId"]


kms_key_id = get_key_id(kms_alias_key)

# if kms key is not already in pending deletion state, delete kms key
if kms_key_id is not None:
    try:
        response = kms_client.schedule_key_deletion(
            KeyId=kms_key_id, PendingWindowInDays=7
        )
        print("KMS key scheduled for deletion")
    except kms_client.exceptions.KMSInvalidStateException:
        print("KMS key already in pending deletion state")
