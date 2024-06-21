# send logs to cloudwatch

import re
from datetime import datetime


def parseLogs(file_path):
    # parse file apache-logs.log line by line
    file1 = open(file_path, "r")
    lines = file1.readlines()

    logs = []

    for line in lines:
        date_str = re.findall("\[(.*)\]", line.strip())[0].replace(" +0000", "")
        date = datetime.strptime(date_str, "%Y-%m-%d:%H:%M:%S")

        logs.append(
            {
                "timestamp": int(date.timestamp() * 1000),
                "message": line.strip(),
            }
        )

    return logs
