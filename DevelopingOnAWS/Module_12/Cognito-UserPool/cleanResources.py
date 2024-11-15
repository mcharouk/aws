import os

import boto3

cognito = boto3.client("cognito-idp")

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)


if current_working_directory.endswith("DevelopingOnAWS"):
    new_wd = "Module_12/Cognito-UserPool"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)


def remove_file(file_location):
    if os.path.exists(file_location):
        os.remove(file_location)
        print(f"Removed file {file_location}")
    else:
        print(f"File {file_location} does not exist")


# remove file

remove_file("./webapp/components/.env")
remove_file("./webapp/tokens.json")

# get user pool with name UserPoolDemo
cognito = boto3.client("cognito-idp")

response = cognito.list_user_pools(MaxResults=10)
if len(response["UserPools"]) == 0:
    print("No user pools found")
    exit()

user_pool_id = ""
for user_pool in response["UserPools"]:
    if user_pool["Name"] == "UserPoolDemo":
        user_pool_id = user_pool["Id"]

if user_pool_id == "":
    print("No user pool named UserPoolDemo found")
    exit()

response = cognito.describe_user_pool(UserPoolId=user_pool_id)
cognito_domain = response["UserPool"]["Domain"]

# deactivate deletion protection
cognito.update_user_pool(
    UserPoolId=user_pool_id,
    DeletionProtection="INACTIVE",
    AutoVerifiedAttributes=["email"],
)

# delete cognito domain
cognito.delete_user_pool_domain(UserPoolId=user_pool_id, Domain=cognito_domain)
print("cognito domain deleted")

# delete cognito user pool
cognito.delete_user_pool(UserPoolId=user_pool_id)
print("cognito user pool deleted")


cognito.close()
