import csv
import json

import boto3

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    # TODO implement

    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    file_name = event["Records"][0]["s3"]["object"]["key"]

    # log all lines of csv file named file_name in bucket_name and skip header

    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    lines = obj["Body"].read().decode("utf-8").splitlines()

    csv_file = csv.DictReader(lines)
    table = dynamodb.Table("demo_employee")
    for row in csv_file:
        print(row)
        table.put_item(Item=row)
        print("Row inserted successfully")

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
