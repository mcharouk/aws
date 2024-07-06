import boto3
import time

# change desired task to 0 for ECS Service named scorekeep-service in cluster scorekeep-cluster

ecs_service_name = "scorekeep-service"
ecs_cluster_name = "scorekeep-cluster"

client = boto3.client("ecs", region_name="eu-west-3")
response = client.update_service(
    cluster=ecs_cluster_name, service=ecs_service_name, desiredCount=0
)
print(f"desired task set to 0 for ecs service named {ecs_service_name}")

client.close()

print("sleeping for 15 seconds")
time.sleep(15)

# get first ec2 auto scaling group
autoscaling = boto3.client("autoscaling", region_name="eu-west-3")
response = autoscaling.describe_auto_scaling_groups()
first_asg = response["AutoScalingGroups"][0]["AutoScalingGroupName"]

# put desired count to 0 for first auto scaling group
response = autoscaling.update_auto_scaling_group(
    AutoScalingGroupName=first_asg, DesiredCapacity=0
)
print(f"desired capacity set to 0 for auto scaling group {first_asg}")
autoscaling.close()

print("sleeping for 300 seconds, corresponding to connection draining period")
time.sleep(300)
