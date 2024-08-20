import json
import urllib.parse as parse

import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    invocation_id = event["invocationId"]
    invocation_schema_version = event["invocationSchemaVersion"]
    results = []

    for task in event["tasks"]:
        task_id = task["taskId"]
        s3Key = parse.unquote(task["s3Key"])
        s3BucketName = task["s3Bucket"]

        # read json file from s3 bucket

        response = s3.get_object(Bucket=s3BucketName, Key=s3Key)
        file_content = response["Body"].read().decode("utf-8")
        json_content = json.loads(file_content)

        project_name = json_content["Project"]
        department_name = json_content["Department"]

        # Tag file in s3 with key Project and project_name as value
        s3.put_object_tagging(
            Bucket=s3BucketName,
            Key=s3Key,
            Tagging={
                "TagSet": [
                    {"Key": "Project", "Value": project_name},
                    {"Key": "Department", "Value": department_name},
                ]
            },
        )

        result_code = "Succeeded"
        result_string = f"Project is {project_name} and department is {department_name}"
        results.append(
            {
                "taskId": task_id,
                "resultCode": result_code,
                "resultString": result_string,
            }
        )

    return {
        "invocationSchemaVersion": invocation_schema_version,
        "treatMissingKeysAs": "PermanentFailure",
        "invocationId": invocation_id,
        "results": results,
    }
