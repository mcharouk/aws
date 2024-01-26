import json


def lambda_handler(event, context):
    # TODO implement
    id = event["pathParameters"]["id"]
    message = "Getting resource from Lambda with id {id}".format(id=id)

    json_message = json.dumps({"message": message})
    return {"isBase64Encoded": "false", "statusCode": 200, "body": json_message}
