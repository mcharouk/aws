# create a lambda handler function


def lambda_handler(event, context):
    """
    A simple lambda function handler that takes in an event and context object,
    and returns a static string.
    """

    # get lambda current version
    current_string = "hello"
    version = context.function_version
    body = f"lambda version : [{version}], current string : [{current_string}]"
    return {"statusCode": 200, "body": body}
