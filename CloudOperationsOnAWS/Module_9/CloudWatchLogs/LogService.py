import boto3

cloudwatch_client = boto3.client("logs")


def send_logs_to_cloudwatch(log_group_name, log_stream_name, logs):
    """Send logs to CloudWatch"""

    # Call CloudWatch API to send logs
    response = cloudwatch_client.put_log_events(
        logGroupName=log_group_name, logStreamName=log_stream_name, logEvents=logs
    )

    return response
