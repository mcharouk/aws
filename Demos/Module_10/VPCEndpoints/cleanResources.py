# delete all sqs queues

import boto3

sqs = boto3.resource("sqs")

for queue in sqs.queues.all():
    queue.delete()
    print(queue.url, "deleted")
