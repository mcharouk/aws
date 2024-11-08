# in specified folder, get first json file ordered by last modified date
import json
import os

import boto3

folder_name = "C:/Users/charouk.m/.aws/sso/cache"
files = [
    f
    for f in os.listdir(folder_name)
    if f.endswith(".json") and not f.startswith("aws-toolkit-vscode")
]
files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_name, x)), reverse=True)

start_url = "https://d-806701dc07.awsapps.com/start/#"
# parse all json files and select the one where startUrl exists and matches with provided one
for file in files:
    with open(folder_name + "/" + file, "r") as f:
        data = json.load(f)
        if "startUrl" in data and data["startUrl"] == start_url:
            print(f"file name is {file}")
            access_token = data["accessToken"]
            print(f"access token is {access_token}")
            break


# get account id
client = boto3.client("sts")

response = client.get_caller_identity()
account_id = response["Account"]

sso_client = boto3.client("sso")
response = sso_client.get_role_credentials(
    roleName="AdministratorAccess", accountId=account_id, accessToken=access_token
)

# get access key id, secret access key and session token
access_key_id = response["roleCredentials"]["accessKeyId"]
secret_access_key = response["roleCredentials"]["secretAccessKey"]
session_token = response["roleCredentials"]["sessionToken"]

print(f"access key id is {access_key_id}")
print(f"secret access key is {secret_access_key}")
print(f"session token is {session_token}")


with open(folder_name + "/" + file, "r") as f:
    data = json.load(f)

    # update credentials for profile NoSQLWorkbench in .aws/credentials file
    import configparser

    profile_name = "NoSQLWorkbench"

    config = configparser.ConfigParser()
    config.read(os.path.expanduser("~/.aws/credentials"))
    config.set(profile_name, "aws_access_key_id", access_key_id)
    config.set(profile_name, "aws_secret_access_key", secret_access_key)
    config.set(profile_name, "aws_session_token", session_token)
    with open(os.path.expanduser("~/.aws/credentials"), "w") as f:
        config.write(f)
        print(f"credentials of profile {profile_name} have been updated")
