import json

import boto3

bucket_name = "my_bucket"
S3_allowed_prefix = "folder1/folder2"
s3_role_name = "my_s3_role"
sqs_role_name = "my_sqs_role"
account_id = "5654768654"
s3_policy_name = "my_s3_policy"
trusted_policy = "my_trusted_policy"
sqs_policy_name = "my_sqs_policy"
region_name = "eu-west-3"
queue_name = "my_queue"
# create a customer managed policy that allow GetObject action to a specific S3 object prefix
# create an assume role policy that allow an AWS Principal of the current account
# create a role and associate it with the policy.

iam = boto3.client("iam")

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        }
    ],
}
iam.create_policy(
    PolicyName=s3_policy_name,
    PolicyDocument=json.dumps(policy),
    Description="my policy",
)
policy_arn = iam.get_policy(PolicyArn=s3_policy_name)["Policy"]["Arn"]
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": account_id},
            "Action": "sts:AssumeRole",
        }
    ],
}

role = iam.create_role(
    RoleName=s3_role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy),
    Description="my role",
)

iam.attach_role_policy(PolicyArn=policy_arn, RoleName=s3_role_name)


policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sqs:CreateQueue",
            "Resource": f"arn:aws:sqs:{region_name}:{account_id}:{queue_name}",
        }
    ],
}
iam.create_policy(
    PolicyName=sqs_policy_name,
    PolicyDocument=json.dumps(policy),
    Description="my policy",
)
policy_arn = iam.get_policy(PolicyArn=sqs_policy_name)["Policy"]["Arn"]
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": account_id},
            "Action": "sts:AssumeRole",
        }
    ],
}

role = iam.create_role(
    RoleName=sqs_role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy),
    Description="my role",
)
iam.attach_role_policy(PolicyArn=policy_arn, RoleName=sqs_role_name)
