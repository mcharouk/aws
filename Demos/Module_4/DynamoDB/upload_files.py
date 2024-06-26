folderName = "./Sample-data"
bucket_name = "eventnotification-demo-457664"

# upload all content of folder in s3 bucket

import os

import boto3

s3 = boto3.client("s3")

limit_nb_of_files = False
files_nb_to_upload = 1

import os

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("Demos"):
    new_wd = "Module_4/DynamoDB"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)


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

            if limit_nb_of_files and nb_files_uploaded >= files_nb_to_upload:
                print(
                    "Uploaded {nb_files_uploaded} files, stop file upload".format(
                        nb_files_uploaded=nb_files_uploaded
                    )
                )
                break


upload_files()
