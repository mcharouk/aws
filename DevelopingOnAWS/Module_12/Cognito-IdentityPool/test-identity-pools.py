import base64
import hashlib
import hmac

# read identity-config.json to feed variables
import json

import boto3
import utils
from Config import Config

utils.change_current_directory()
config = Config()

# finance user
USER_NAME = "john.foo"
USER_PASSWORD = "john.foo"

# rh user
# USER_NAME = "dave.bar"
# USER_PASSWORD = "dave.bar"


def get_secret_hash(username, app_client_id, client_secret):
    message = bytes(username + app_client_id, "utf-8")
    key = bytes(client_secret, "utf-8")
    secret_hash = base64.b64encode(
        hmac.new(key, message, digestmod=hashlib.sha256).digest()
    ).decode()
    return secret_hash


# initiate-auth with cognito user pool
idp = boto3.client("cognito-idp")
response = idp.initiate_auth(
    ClientId=config.user_pool_client_id,
    AuthFlow="USER_PASSWORD_AUTH",
    AuthParameters={
        "USERNAME": USER_NAME,
        "PASSWORD": USER_PASSWORD,
        "SECRET_HASH": get_secret_hash(
            USER_NAME, config.user_pool_client_id, config.user_pool_client_secret
        ),
    },
)

# get id token
id_token = response["AuthenticationResult"]["IdToken"]

print(f"id token is {id_token}")

# get cognito identity id with id_token. Each user has a unique identity id, generated the first time he calls identity pool
cognito_identity = boto3.client("cognito-identity")

response = cognito_identity.get_id(
    IdentityPoolId=config.identity_pool_id,
    Logins={
        f"cognito-idp.eu-west-3.amazonaws.com/{config.user_pool_id}": id_token,
    },
)

# get identity id
identity_id = response["IdentityId"]

print(f"identity_id is {identity_id}")

# get credentials for identity id
credentials = cognito_identity.get_credentials_for_identity(
    IdentityId=identity_id,
    Logins={
        f"cognito-idp.eu-west-3.amazonaws.com/{config.user_pool_id}": id_token,
    },
)


# get access key id, secret key and session token
ACCESS_KEY = credentials["Credentials"]["AccessKeyId"]
SECRET_KEY = credentials["Credentials"]["SecretKey"]
SESSION_TOKEN = credentials["Credentials"]["SessionToken"]


print(f"access_key_id is {ACCESS_KEY}")
print(f"secret_access_key is {SECRET_KEY}")
print(f"session_token is {SESSION_TOKEN}")

# set an S3 client with specific credentials
s3_client = boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN,
    region_name=config.region_name,
)


# get object named bruce_wayne/identity.txt from bucket
# print content


def get_object(bucket_name, key):
    print(f"Trying to get {key} content")
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        content = response["Body"].read()
        file_content = content.decode("utf-8")
        print(f"content is [{file_content}]")
    except Exception as e:
        print(e)


get_object(config.bucket_name, "finance/some-file.txt")
get_object(config.bucket_name, "rh/some-file.txt")


s3_client.close()
idp.close()
cognito_identity.close()
