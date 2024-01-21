folderName = "Sample-data"
bucket_name = "eventnotification-demo-457663"

# upload all content of folder in s3 bucket

import os

import boto3

s3 = boto3.client("s3")

limit_nb_of_files = True
files_nb_to_upload = 1


def upload_files():
    nb_files_uploaded = 0
    for subdir, dirs, files in os.walk(folderName):
        for file in files:
            full_path = os.path.join(subdir, file)

            with open(full_path, "rb") as data:
                object_prefix = "files/" + full_path[len(folderName) + 1 :]
                print(f"Uploading {full_path} to {bucket_name}/{object_prefix}")
                s3.upload_fileobj(data, bucket_name, object_prefix)
                nb_files_uploaded += 1
                print(f"Upload successfull")

            if limit_nb_of_files and nb_files_uploaded >= files_nb_to_upload:
                print("Stopping to upload files because of limiting rule")
                break


upload_files()
