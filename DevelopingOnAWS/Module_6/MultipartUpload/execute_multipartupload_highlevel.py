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

import utils

utils.delete_bucket_if_exists(s3, s3_resource, bucket_name)
utils.create_bucket(s3, bucket_name, region)

# multipart_threshold : above this size limit, multipart will be activated
# concurrency : max concurrency to upload parts
# chunk size : size of each part
# use threads : must be true so that concurrency can occur
from boto3.s3.transfer import TransferConfig

MB = 1024**2
config = TransferConfig(
    multipart_threshold=100 * MB,
    max_concurrency=10,
    multipart_chunksize=10 * MB,
    use_threads=True,
)


# this class is for tracking progress. It's not mandatory
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
