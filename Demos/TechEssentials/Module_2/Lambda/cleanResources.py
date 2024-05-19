import boto3
from botocore.exceptions import ClientError
from lambdaDemo.StackConfig import StackConfig

stackConfig = StackConfig()

lambda_name = stackConfig.lambdaName
lambda_client = boto3.client("lambda")
sqs_queue_name = stackConfig.sqsQueueName
sqs_client = boto3.client("sqs")


queues = sqs_client.list_queues()


def get_queue_arn(sqs_queue_name):
    for queue in queues["QueueUrls"]:
        if sqs_queue_name in queue:
            return sqs_client.get_queue_attributes(
                QueueUrl=queue, AttributeNames=["QueueArn"]
            )["Attributes"]["QueueArn"]


## get queue arn of queue with name sqs_queue_name
queue_arn = get_queue_arn(sqs_queue_name)
print(queue_arn)

response = lambda_client.list_event_source_mappings(
    EventSourceArn=queue_arn, FunctionName=lambda_name
)
# get uuid of event source mapping
if len(response["EventSourceMappings"]) > 0:
    sqsQueue_uuid = response["EventSourceMappings"][0]["UUID"]
    lambda_client.delete_event_source_mapping(UUID=sqsQueue_uuid)
    print("event source mapping {0} deleted".format(sqsQueue_uuid))
else:
    print("no event source mapping found")

try:
    response = lambda_client.delete_function(FunctionName=lambda_name)
    print("lambda function {0} deleted".format(lambda_name))

except ClientError as e:
    print("lambda function {0} not found".format(lambda_name))
