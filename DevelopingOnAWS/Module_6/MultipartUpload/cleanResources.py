import boto3

bucket_name = "demo-marccharouk-multipartupload-58767497"

s3 = boto3.client("s3")
s3_resource = boto3.resource("s3")
# check bucket exists
try:
    s3.head_bucket(Bucket=bucket_name)
    print("Bucket already exists")
    # delete all files in bucket
    s3_resource.Bucket(bucket_name).objects.all().delete()
    s3.delete_bucket(
        Bucket=bucket_name,
    )
    print("Bucket deleted")
except Exception as e:
    print("Bucket does not exist")

s3.close()
