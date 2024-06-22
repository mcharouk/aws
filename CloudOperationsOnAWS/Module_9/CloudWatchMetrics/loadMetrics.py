import datetime
import random

import boto3

namespace = "ExampleCorp-Factory"
# factory_names = ["Plant-p76", "Plant-p77"]
factory_names = ["Plant-p76", "Plant-p77"]
machine_names = ["Hoven-h476483", "Hoven-h904736", "Hoven-284748"]


now = datetime.datetime.now()
midnight = datetime.datetime.combine(now.date(), datetime.time.min)

# put metrics in cloudwatch with factory name and machine name as dimension
client = boto3.client("cloudwatch")

metrics = []


def generate_metrics_for_plant(factory_name, machine_name):
    return {
        "MetricName": "Temperature",
        "Dimensions": [
            {"Name": "FactoryName", "Value": factory_name},
            {"Name": "MachineName", "Value": machine_name},
        ],
        "Value": random.randint(0, 30),
        "Unit": "None",
        "Timestamp": midnight + datetime.timedelta(minutes=i * 5),
    }


metrics = []
for i in range(int((datetime.datetime.now() - midnight).total_seconds() / 60 / 5)):
    for factory_name in factory_names:
        for machine_name in machine_names:
            metric = generate_metrics_for_plant(factory_name, machine_name)
            metrics.append(metric)

client.put_metric_data(
    Namespace=namespace,
    MetricData=metrics,
)
