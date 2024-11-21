import os

import boto3

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("CloudOperationsOnAWS"):
    new_wd = "Module_9/CloudWatchLogs"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

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

# delete file apache-logs.log if it exists
if os.path.exists("apache-logs.log"):
    os.remove("apache-logs.log")
    print("Deleted file apache-logs.log")

client.close()
