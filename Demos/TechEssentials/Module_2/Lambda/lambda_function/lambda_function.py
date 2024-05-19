import json

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("organizations")


def lambda_handler(event, context):
    for record in event["Records"]:
        payload = record["body"]
        payload_dict = json.loads(payload)
        response = table.put_item(Item=payload_dict)
        print("Wrote message to DynamoDB:", json.dumps(response))
