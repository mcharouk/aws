import os

import urllib3


def lambda_handler(event, context):

    dns_name = os.environ["DNS_NAME"]
    http = urllib3.PoolManager()
    url = "http://{0}".format(dns_name)
    print("calling {0}".format(url))
    response = http.request("GET", "http://{0}".format(dns_name))
    response_str = response.data.decode("utf-8")

    return {"statusCode": 200, "body": response_str}
