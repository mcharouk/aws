# create a lambda handler

import boto3

sqs = boto3.client("sqs")
s3 = boto3.client("s3", region_name="eu-west-3")
sns = boto3.client("sns")


def lambda_handler(event, context):
    # set default region to eu-west-3

    # create sqs queue
    # try to create a sqs queue, log if creation fails
    try:
        response = sqs.create_queue(QueueName="test")
        print("SQS queue created successfully")
        queue_url = response["QueueUrl"]
        sqs.delete_queue(QueueUrl=queue_url)

    except Exception as e:
        print(f"Error creating SQS queue: {e}")

    # create a S3 bucket and remove it

    bucket_name = "permissionboundarydemo-marccharouk-1238478"
    try:
        location = {"LocationConstraint": "eu-west-3"}
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print("S3 bucket created successfully")
        s3.delete_bucket(Bucket=bucket_name)
        print("S3 bucket deleted successfully")

    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

    # try to create a sns topic and remove it, log if creation fails

    try:
        response = sns.create_topic(Name="test")
        print("SNS topic created successfully")
        topic_arn = response["TopicArn"]
        sns.delete_topic(TopicArn=topic_arn)

    except Exception as e:
        print(f"Error creating SNS topic: {e}")

    return
