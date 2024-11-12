def delete_bucket_if_exists(s3_client, s3_resource, bucket_name):
    # check bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print("Bucket already exists")
        # delete all files in bucket
        s3_resource.Bucket(bucket_name).objects.all().delete()
        s3_client.delete_bucket(
            Bucket=bucket_name,
        )
        print("Bucket deleted")
    except Exception as e:
        print("Bucket does not exist")


def create_bucket(s3_client, bucket_name, region):

    s3_client.create_bucket(
        Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
    )
    waiter = s3_client.get_waiter("bucket_exists")
    waiter.wait(Bucket=bucket_name)

    print("Bucket created")
