import os

import boto3

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("DevelopingOnAWS"):
    new_wd = "Module_12/Cognito-UserPool"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

# get first cognito user pool
cognito = boto3.client("cognito-idp")

response = cognito.list_user_pools(MaxResults=1)
user_pool_id = response["UserPools"][0]["Id"]

# get cognito domain url

response = cognito.describe_user_pool(UserPoolId=user_pool_id)
cognito_domain = response["UserPool"]["Domain"]

# get first client app
response = cognito.list_user_pool_clients(UserPoolId=user_pool_id, MaxResults=1)
client_id = response["UserPoolClients"][0]["ClientId"]

# get client secret of client app
response = cognito.describe_user_pool_client(
    UserPoolId=user_pool_id, ClientId=client_id
)
client_secret = response["UserPoolClient"]["ClientSecret"]


# open file env-template.txt and replace placeholder with actual values
with open("env-template.txt", "r") as f:
    content = f.read()
    content = content.replace("{{COGNITO_DOMAIN}}", cognito_domain)
    content = content.replace("{{CLIENT_ID}}", client_id)
    content = content.replace("{{CLIENT_SECRET}}", client_secret)

    target_file_location = "./webapp/components/.env"
    # delete file .env if it exists
    if os.path.exists(target_file_location):
        os.remove(target_file_location)
    # open file .env in write mode and
    # write content in file .env located in webapp/components
    with open(target_file_location, "w") as f2:
        f2.write(content)

    print(f"Updated file {target_file_location}")

cognito.close()
