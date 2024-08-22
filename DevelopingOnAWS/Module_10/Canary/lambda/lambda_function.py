import json


def lambda_handler(event, context):

    json_message = json.dumps(
        {"message": f"Hello World from version {context.function_version} !"}
    )
    return {"isBase64Encoded": "false", "statusCode": 200, "body": json_message}
