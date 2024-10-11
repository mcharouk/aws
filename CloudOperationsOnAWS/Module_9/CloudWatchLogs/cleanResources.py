import boto3

client = boto3.client("logs")

log_group_name = "logs_demo"


# delete all metric filters of log group
def delete_metric_filters(client, log_group_name):
    response = client.describe_metric_filters(logGroupName=log_group_name)
    for metric_filter in response["metricFilters"]:
        client.delete_metric_filter(
            logGroupName=log_group_name, filterName=metric_filter["filterName"]
        )
        print(f"Deleted metric filter: {metric_filter['filterName']}")


delete_metric_filters(client, log_group_name)

client.close()
