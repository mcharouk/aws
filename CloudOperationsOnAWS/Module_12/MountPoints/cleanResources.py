import os
import time

import boto3

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("CloudOperationsOnAWS"):
    new_wd = "Module_12/MountPoints"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

efs = boto3.client("efs")

response = efs.describe_file_systems()

for file_system in response["FileSystems"]:
    # get all mount points and delete them
    mount_points = efs.describe_mount_targets(FileSystemId=file_system["FileSystemId"])[
        "MountTargets"
    ]

    origin_mount_points_nb = len(mount_points)
    for mount_point in mount_points:
        mount_target_id = mount_point["MountTargetId"]
        efs.delete_mount_target(MountTargetId=mount_target_id)
        print(f"Deleted mount point with ID: {mount_target_id}")

    mount_deleted_target_ids = []
    # loop every 5 seconds to check that mount points have been deleted
    while True:
        mount_points = efs.describe_mount_targets(
            FileSystemId=file_system["FileSystemId"]
        )["MountTargets"]
        if len(mount_points) == 0:
            break

        mount_points_deleted = 0
        for mount_point in mount_points:
            if mount_point["LifeCycleState"] == "deleted":
                mount_points_deleted += 1
        if mount_points_deleted == len(mount_points):
            break
        else:
            print(
                f"Waiting for {len(mount_points) - mount_points_deleted} mount points to be deleted..."
            )
            time.sleep(5)

    file_system_id = file_system["FileSystemId"]
    efs.delete_file_system(FileSystemId=file_system_id)
    print(f"Deleted EFS file system with ID: {file_system_id}")


# delete file readFile.sh and writeFile.sh if they exist


def remove_file_if_exists(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Deleted {file_name}")
    else:
        print(f"{file_name} does not exist")


remove_file_if_exists("readFile.sh")
remove_file_if_exists("writeFile.sh")
