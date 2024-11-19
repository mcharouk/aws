import os

import boto3

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("CloudOperationsOnAWS"):
    new_wd = "Module_12/MountPoints"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

# list all efs created
# get first one
# get efs ID


def get_efs_id():
    client = boto3.client("efs")
    response = client.describe_file_systems()
    return response["FileSystems"][0]["FileSystemId"]


efs_id = get_efs_id()
print(f"generate scripts for efs id {efs_id}")


def generate_output_file(file_name):
    # read  file in script-templates/readFile.sh
    with open(f"script-templates/{file_name}", "r") as f:
        read_file_script = f.read()
        # replace placeholders with {{efs_id}} with efs_id
        read_file_script = read_file_script.replace("{{EFS_ID}}", efs_id)
        # write to file in scripts/readFile.sh
        with open(file_name, "w") as f:
            f.write(read_file_script)


generate_output_file("readFile.sh")
generate_output_file("writeFile.sh")
