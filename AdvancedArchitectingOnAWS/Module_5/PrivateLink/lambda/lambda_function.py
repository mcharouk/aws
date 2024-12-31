import json
import os

region = os.environ["AWS_REGION"]


def lambda_handler(event, context):

    bodyContent = {"text": "Hello from PrivateLink in {0} !".format(region)}

    return {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(bodyContent),
    }
