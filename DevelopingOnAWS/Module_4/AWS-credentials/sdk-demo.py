import boto3

profile_name_sqs_admin = "sqsAdmin"
profile_name_sns_admin = "snsAdmin"
profile_name_ddb_admin = "dynamoDBAdminRole"

dynamodbRoleArn = "arn:aws:iam::637423642269:role/DynamodbFullAccessRole"

# get caller identity with profile sqs admin

sts = boto3.Session(profile_name=profile_name_sqs_admin).client("sts")
response = sts.get_caller_identity()

print(response)


queue_name = "sample-queue"

# create sqs queuee with profile sqs admin

sqs = boto3.Session(profile_name=profile_name_sqs_admin).client("sqs")

response = sqs.create_queue(QueueName=queue_name)
queue_url = response["QueueUrl"]
print(queue_url)

# remove queue
sqs.delete_queue(QueueUrl=queue_url)
print("Queue deleted")

sqs.close()

# create sns topic with sqs admin profile
sns_topic_name = "sample-topic"
sns = boto3.Session(profile_name=profile_name_sqs_admin).client("sns")
try:
    print("Creating SNS topic with sqs admin profile")
    response = sns.create_topic(Name=sns_topic_name)
except Exception as e:
    print(e)

# create sns topic with sns admin profile
sns = boto3.Session(profile_name=profile_name_sns_admin).client("sns")

print("Creating SNS topic with sns admin profile")
response = sns.create_topic(Name=sns_topic_name)

# delete sns topic

sns.delete_topic(TopicArn=response["TopicArn"])
print("SNS topic deleted")

sns.close()

# assume a role dynamo db admin role with sqsadmin user

print("assuming dynamodb role")
response = sts.assume_role(
    RoleArn=dynamodbRoleArn,
    RoleSessionName="dynamoDBAdminRoleSession",
)
print(response)

# create dynamodb table with dynamo db admin role
dynamodb = boto3.Session(profile_name=profile_name_ddb_admin).client("dynamodb")
table_name = "sample-table"

print("Creating DynamoDB table")
response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {"AttributeName": "UserId", "KeyType": "HASH"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "UserId", "AttributeType": "S"},
    ],
    ProvisionedThroughput={
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5,
    },
)
# wait until dynamodb table is created
dynamodb.get_waiter("table_exists").wait(TableName=table_name)
print("DynamoDB table created")

# list dynamodb tables
response = dynamodb.list_tables()
print(response["TableNames"])

# remove dynamodb table
print("Deleting DynamoDB table")
dynamodb.delete_table(TableName=table_name)

# wait until dynamodb table is deleted
dynamodb.get_waiter("table_not_exists").wait(TableName=table_name)
print("DynamoDB table deleted")

dynamodb.close()
sts.close()
