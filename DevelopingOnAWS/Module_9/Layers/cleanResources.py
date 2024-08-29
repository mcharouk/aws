import os

import boto3

folder_to_remove = "layer-package"
# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("DevelopingOnAWS"):
    new_wd = "Module_9/Layers"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

# delete folder layer-package and all its contents if it exists
if os.path.exists(folder_to_remove):
    for root, dirs, files in os.walk(folder_to_remove, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir(folder_to_remove)
    print(f"Folder {folder_to_remove} has been deleted.")
else:
    print(f"Folder {folder_to_remove} does not exist.")

# delete lambda function named LambdaUsingLayer if it exists
lambda_client = boto3.client("lambda")
function_name = "LambdaUsingLayer"

try:
    response = lambda_client.get_function(FunctionName=function_name)
    lambda_client.delete_function(FunctionName=function_name)
    print(f"Lambda function {function_name} has been deleted.")

except lambda_client.exceptions.ResourceNotFoundException:
    print(f"Lambda function {function_name} does not exist.")

lambda_zip_name = "main-function/Lambda-code.zip"


# get all lambda layer versions
layer_name = "lambda-utils"
response = lambda_client.list_layer_versions(LayerName=layer_name)
if len(response["LayerVersions"]) == 0:
    print(f"No layer versions found for {layer_name}.")
else:
    # delete all lambda layer version
    for layer_version in response["LayerVersions"]:
        lambda_client.delete_layer_version(
            LayerName=layer_name, VersionNumber=layer_version["Version"]
        )
        print(
            f"Layer version {layer_version['Version']} of {layer_name} has been deleted."
        )

# remove lambda zip name if it exists
if os.path.exists(lambda_zip_name):
    os.remove(lambda_zip_name)
    print(f"File {lambda_zip_name} has been deleted.")
else:
    print(f"File {lambda_zip_name} does not exist.")
