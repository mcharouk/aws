import boto3

# empty bucket s3 named marccharouk-staticwebhosting

s3 = boto3.resource("s3")

bucket_name = "marccharouk-staticwebhosting"
# if bucket exists
if s3.Bucket(bucket_name) in s3.buckets.all():
    bucket = s3.Bucket(bucket_name)
    bucket.objects.all().delete()

    # delete bucket
    bucket.delete()
    print(f"bucket {bucket_name} has been deleted")
else:
    print(f"bucket {bucket_name} does not exist")
