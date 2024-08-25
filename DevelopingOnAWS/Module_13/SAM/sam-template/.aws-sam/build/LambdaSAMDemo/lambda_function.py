# create a lambda handler function


def lambda_handler(event, context):
    """
    A simple lambda function handler that takes in an event and context object,
    and returns a static string.
    """
    body = "This is my lambda second version"
    return {"statusCode": 200, "body": body}
