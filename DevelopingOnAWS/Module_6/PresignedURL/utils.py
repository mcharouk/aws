import os


def change_current_directory():
    # get the current working directory
    current_working_directory = os.getcwd()
    # print output to the console
    print("current directory : " + current_working_directory)

    if current_working_directory.endswith("DevelopingOnAWS"):
        new_wd = "Module_6/PresignedURL"
        print(
            "changing working directory to " + current_working_directory + "/" + new_wd
        )
        os.chdir(new_wd)


def delete_bucket_if_exists(s3_resource, bucket_name):
    # check bucket exists
    try:
        s3_resource.head_bucket(Bucket=bucket_name)
        print("Bucket already exists")
        # delete all files in bucket
        s3_resource.Bucket(bucket_name).objects.all().delete()
        s3_resource.delete_bucket(
            Bucket=bucket_name,
        )
        print("Bucket deleted")
    except Exception as e:
        print("Bucket does not exist")


def create_bucket(s3_resource, bucket_name, region_name):
    s3_resource.create_bucket(
        Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
    )
    waiter = s3_resource.get_waiter("bucket_exists")
    waiter.wait(Bucket=bucket_name)
    print("Bucket created")
