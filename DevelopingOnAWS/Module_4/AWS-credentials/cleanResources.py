# delete file aws-config-result.txt and aws-credentials-result.txt
import os

config_file_path = "aws-config-result.txt"
credential_file_path = "aws-credentials-result.txt"
# check if file exists and remove it if so

if os.path.exists(config_file_path):
    os.remove(config_file_path)
    print("aws-config-result.txt has been deleted successfully")
else:
    print(f"{config_file_path} does not exist")

if os.path.exists(credential_file_path):
    os.remove(credential_file_path)
    print(f"{credential_file_path} has been deleted successfully")
else:
    print(f"{credential_file_path} does not exist")


# delete all sqs queues
import boto3

sqs = boto3.resource("sqs")

for queue in sqs.queues.all():
    queue.delete()
    print(f"Queue {queue.url} has been deleted successfully")
print("All SQS queues have been deleted successfully")

# delete all sns topics

sns = boto3.resource("sns")

topic_not_delete_name = "aws-controltower-SecurityNotifications"
for topic in sns.topics.all():
    if topic.arn.split(":")[-1] == topic_not_delete_name:
        print(f"Topic {topic.arn} has been skipped because it relates to control tower")
        continue
    topic.delete()
    print(f"Topic {topic.arn} has been deleted successfully")
print("All SNS topics have been deleted successfully")


# delete all dynamodb tables
dynamodb = boto3.resource("dynamodb")
for table in dynamodb.tables.all():
    table.delete()
    print(f"Table {table.name} has been deleted successfully")
print("All DynamoDB tables have been deleted successfully")
