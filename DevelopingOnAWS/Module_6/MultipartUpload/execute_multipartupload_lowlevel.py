import boto3

# upload test_file with multipart upload

s3 = boto3.client("s3")
s3_resource = boto3.resource("s3")

test_file = "C:/Users/charouk.m/Documents/AWS/1GB.bin"
bucket_name = "demo-marccharouk-multipartupload-58767497"
object_key = "1GB-lowlevel.bin"
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

# create part
multipart_upload = s3.create_multipart_upload(
    Bucket=bucket_name,
    ContentType="application/binary",
    Key=object_key,
)

# means 10 Mb
parts_size = 10000000
parts = []
with open(test_file, "rb") as f:
    part_index = 1
    while True:
        part_data = f.read(parts_size)
        if not len(part_data):
            break

        print("Uploading part %i" % part_index)
        upload_part = s3_resource.MultipartUploadPart(
            bucket_name, object_key, multipart_upload["UploadId"], part_index
        )
        uploadPartResponse = upload_part.upload(
            Body=part_data,
        )
        print(f"Transfer finished, collecting ETag {uploadPartResponse["ETag"]} and part number {part_index}")
        parts.append({"PartNumber": part_index, "ETag": uploadPartResponse["ETag"]})
        part_index += 1

print("All parts uploaded, completing multipart upload")

completeResult = s3.complete_multipart_upload(
    Bucket=bucket_name,
    Key=object_key,
    MultipartUpload={"Parts": parts},
    UploadId=multipart_upload["UploadId"],
)

print("Multipart upload completed")

s3.close()
