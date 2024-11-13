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


utils.delete_bucket_if_exists(
    s3_client=s3, s3_resource=s3_resource, bucket_name=bucket_name
)
utils.create_bucket(
    s3_resource=s3_resource, bucket_name=bucket_name, region_name=region, s3_client=s3
)

# upload file to bucket
s3.upload_file(test_file, bucket_name, object_key)

# generate presigned URL
url = s3.generate_presigned_url(
    ClientMethod="get_object",  # can be any method supported by s3 client
    Params={"Bucket": bucket_name, "Key": object_key},
    ExpiresIn=300,
)

print(f"PresignedURL is [{url}]")

s3.close()
