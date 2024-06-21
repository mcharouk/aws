import os

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("CloudOperationsOnAWS"):
    new_wd = "Module_9/CloudWatchLogs"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

import LogParser as lp
import LogService as ls
from cloud_watch_logs.StackConfig import StackConfig

import LogGenerator as lg

stackConfig = StackConfig()

lg.generate_logs(stackConfig.logs_wait_time)

logs = lp.parseLogs("apache-logs.log")

log_group_name = stackConfig.logs_group_name
log_stream_name = stackConfig.logs_stream_name

ls.send_logs_to_cloudwatch(
    log_group_name=log_group_name, log_stream_name=log_stream_name, logs=logs
)
