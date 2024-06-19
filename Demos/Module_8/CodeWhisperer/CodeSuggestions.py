import os

# change working directory to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd

# load the sample-pandas.csv file
# remove duplicates
# sort lines in alphabetical order
# save to sample_sorted_pandas.csv
df = pd.read_csv("sample-pandas.csv", header=None)
df = df.drop_duplicates()
df = df.sort_values(by=list(df.columns))
df.to_csv("sample_sorted_pandas.csv", index=False, header=False)


import boto3

bucket_name = "marc-charouk-codewhisperer-demo"
file_name = "sample.csv"

# create a s3 bucket in eu-west-3 region as LocationConstraint
# upload sample.csv to the bucket
# list the objects in the bucket and print their object keys
# empty the bucket
# delete the bucket
s3 = boto3.client("s3", region_name="eu-west-3")

# create a bucket
s3.create_bucket(
    Bucket=bucket_name, CreateBucketConfiguration={"XXXXXXXXXXXXXXXXXX": "eu-west-3"}
)
# upload a file
s3.upload_file(file_name, bucket_name, file_name)
# list objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
for obj in response["Contents"]:
    print(obj["Key"])

# empty the bucket
s3.delete_objects(
    Bucket=bucket_name,
    Delete={"Objects": [{"Key": obj["Key"]} for obj in response["Contents"]]},
)

# delete the bucket
s3.delete_bucket(Bucket=bucket_name)
print("Bucket deleted")
