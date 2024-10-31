import os

# change working directory to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


import boto3

bucket_name = "marc-charouk-codewhisperer-demo"
file_name = "sample.csv"

# create a s3 bucket in eu-west-3 region as LocationConstraint
# upload sample.csv to the bucket
# list the objects in the bucket and print their object keys
# empty the bucket
# delete the bucket
s3 = boto3.resource("s3", region_name="eu-west-3")

bucket = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint": "eu-west-3"},
)
bucket.upload_file(file_name, file_name)
objects = bucket.objects.all()
for obj in objects:
    print(obj.key)
    obj.delete()
    print(f"Deleted {obj.key}")

bucket.delete()
print(f"Deleted bucket {bucket_name}")
