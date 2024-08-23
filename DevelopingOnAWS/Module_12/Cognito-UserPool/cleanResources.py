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

# remove file
env_file_location = "./webapp/components/.env"
if os.path.exists(env_file_location):
    os.remove(env_file_location)
    print(f"Removed file {env_file_location}")
else:
    print(f"File {env_file_location} does not exist")

response = cognito.list_user_pools(MaxResults=1)
if len(response["UserPools"]) == 0:
    print("No user pools found")
    exit()

user_pool_id = response["UserPools"][0]["Id"]
# get cognito domain url

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
