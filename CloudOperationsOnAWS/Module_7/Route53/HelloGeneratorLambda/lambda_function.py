import os

import boto3
import urllib3

ssm = boto3.client("ssm")
dns_name_key_ssm = os.environ["DNS_NAME_KEY_SSM"]


def lambda_handler(event, context):

    http = urllib3.PoolManager()
    domain_name = ssm.get_parameter(Name=dns_name_key_ssm, WithDecryption=False)[
        "Parameter"
    ]["Value"]
    url = "http://{0}".format(domain_name)
    print("calling {0}".format(url))
    response = http.request("GET", "http://{0}".format(domain_name))
    response_str = response.data.decode("utf-8")

    return {"statusCode": 200, "body": response_str}
