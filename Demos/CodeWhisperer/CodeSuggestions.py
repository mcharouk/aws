import random

import boto3

# create a random number between 100000 and 999999
random_number = random.randint(100000, 999999)
# convert the random number to a string
random_number_str = str(random_number)

bucket_name = "test-codewhisperer-" + random_number_str
file_name = "AWS.png"


# function that creates an S3 Bucket
def create_s3_bucket(bucket_name):
    s3_client = boto3.client("s3")
    s3_client.create_bucket(Bucket=bucket_name)
    print("S3 bucket created successfully!")


# function that put an Object into S3 bucket
def put_object_into_s3_bucket(bucket_name, file_name):
    s3_client = boto3.client("s3")
    s3_client.upload_file(file_name, bucket_name, "codewhisperer/" + file_name)
    print("Object uploaded successfully!")
