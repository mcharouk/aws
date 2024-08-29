folder_name = "C:/Users/charouk.m/.aws/cli/cache"

# in specified folder, get first json file ordered by last modified date
import os


def get_latest_json(folder):
    files = [f for f in os.listdir(folder) if f.endswith(".json")]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)
    return files[0]


file = get_latest_json(folder_name)
# print file name
print(f"file name is {file}")

# read file and extract Credentials.AccessKeyId, Credentials.SecretAccessKey, Credentials.SessionToken
import json

with open(folder_name + "/" + file, "r") as f:
    data = json.load(f)
    access_key_id = data["Credentials"]["AccessKeyId"]
    secret_access_key = data["Credentials"]["SecretAccessKey"]
    session_token = data["Credentials"]["SessionToken"]
    expiration_time = data["Credentials"]["Expiration"]

    print(f"expiration time of token is {expiration_time}")

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
