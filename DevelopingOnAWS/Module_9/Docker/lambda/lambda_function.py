import utils


def lambda_handler(event, context):
    github_urls = utils.get_github_urls()
    return {"statusCode": 200, "body": github_urls["current_user_url"]}
