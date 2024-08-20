import os
import sys
import threading

import boto3

# upload test_file with multipart upload

s3 = boto3.client("s3")
s3_resource = boto3.resource("s3")

test_file = "C:/Users/charouk.m/Documents/AWS/1GB.bin"
bucket_name = "demo-marccharouk-multipartupload-58767497"
object_key = "1GB-highlevel.bin"
region = "eu-west-3"


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

s3.create_bucket(
    Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
)
print("Bucket created")

# multipart_threshold : above this size limit, multipart will be activated
# concurrency : max concurrency to upload parts
# chunk size : size of each part
# use threads : must be true so that concurrency can occur
from boto3.s3.transfer import TransferConfig

config = TransferConfig(
    multipart_threshold=1024 * 25,
    max_concurrency=10,
    multipart_chunksize=1024 * 10,
    use_threads=True,
)


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)"
                % (self._filename, self._seen_so_far, self._size, percentage)
            )
            sys.stdout.flush()


s3_resource.Object(bucket_name, object_key).upload_file(
    test_file,
    ExtraArgs={"ContentType": "application/binary"},
    Config=config,
    Callback=ProgressPercentage(test_file),
)


s3.close()
