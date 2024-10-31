import json
import os

import boto3
import utils

utils.change_current_directory()

unset_aws_profile = False
load_env_variables = True
load_credentials_in_code = True


def print_env_variables(key_name):
    if key_name not in os.environ:
        print(f"{key_name} is not set")
        return
    print(f"{key_name} has value [{os.environ[key_name]}]")


# print environment variables named AWS_PROFILE
sts = None

with open("config.json", "r") as file:
    config = json.load(file)
    johnFoo_accesskeyId = config["john.foo"]["accessKeyId"]
    johnFoo_secretAccessKey = config["john.foo"]["secretAccessKey"]
    s3_admin_role_arn = config["S3AdminRole"]["arn"]

if load_credentials_in_code:
    sts = boto3.client("sts")
    # assume role s3_admin_role_arn
    assumed_role = sts.assume_role(
        RoleArn=s3_admin_role_arn,
        RoleSessionName="s3-admin-session",
    )
    # create new boto3 session
    s3FullAccessRole_session = boto3.Session(
        aws_access_key_id=assumed_role["Credentials"]["AccessKeyId"],
        aws_secret_access_key=assumed_role["Credentials"]["SecretAccessKey"],
        aws_session_token=assumed_role["Credentials"]["SessionToken"],
    )
    # create s3 client
    sts = s3FullAccessRole_session.client("sts")


if load_env_variables:
    # set environment variables
    os.environ["AWS_ACCESS_KEY_ID"] = johnFoo_accesskeyId
    os.environ["AWS_SECRET_ACCESS_KEY"] = johnFoo_secretAccessKey

# remove environment variables
if unset_aws_profile:
    os.environ.pop("AWS_PROFILE", None)

print_env_variables("AWS_PROFILE")
print_env_variables("AWS_ACCESS_KEY_ID")
print_env_variables("AWS_SECRET_ACCESS_KEY")


if sts is None:
    print("creating default sts client")
    sts = boto3.client("sts")

# get caller identity
caller_identity = sts.get_caller_identity()
print(caller_identity)

sts.close()
