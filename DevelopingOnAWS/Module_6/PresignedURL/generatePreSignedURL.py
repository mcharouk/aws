import boto3
import utils

test_file = "./sample-document.json"
bucket_name = "demo-marccharouk-presignedurl-6767873"
object_key = "sample-document.json"
region = "eu-west-3"

utils.change_current_directory()

# endpoint_url is needed or there is a SignatureDoesNotMatch exception when trying to get the object with generated URL
s3 = boto3.client(
    "s3", region_name=region, endpoint_url=f"https://s3.{region}.amazonaws.com"
)

s3_resource = boto3.resource("s3", region_name=region)


def delete_bucket_if_exists(bucket_name):
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


def create_bucket(bucket_name):
    s3.create_bucket(
        Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
    )
    waiter = s3.get_waiter("bucket_exists")
    waiter.wait(Bucket=bucket_name)
    print("Bucket created")


delete_bucket_if_exists(bucket_name)
create_bucket(bucket_name)

# upload file to bucket
s3.upload_file(test_file, bucket_name, object_key)

# generate presigned URL
url = s3.generate_presigned_url(
    ClientMethod="get_object",
    Params={"Bucket": bucket_name, "Key": object_key},
    ExpiresIn=300,
)

print(f"PresignedURL is [{url}]")

s3.close()
