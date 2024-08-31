import boto3

# get first ec2 auto scaling group
autoscaling = boto3.client("autoscaling")
ec2 = boto3.client("ec2")
response = autoscaling.describe_auto_scaling_groups()

if len(response["AutoScalingGroups"]) == 0:
    print("no auto scaling groups found")
else:
    first_asg = response["AutoScalingGroups"][0]["AutoScalingGroupName"]

    # get all ec2 instances of autoscaling group

    response = autoscaling.describe_auto_scaling_groups(
        AutoScalingGroupNames=[first_asg], MaxRecords=100
    )
    instances = response["AutoScalingGroups"][0]["Instances"]
    instance_ids = [instance["InstanceId"] for instance in instances]
    print(f"instances in auto scaling group {first_asg}: {instance_ids}")

    # put desired count to 0 for first auto scaling group
    response = autoscaling.update_auto_scaling_group(
        AutoScalingGroupName=first_asg, DesiredCapacity=0, MinSize=0
    )
    print(f"desired capacity set to 0 for auto scaling group {first_asg}")

    # wait for all ec2 instances to be terminated

    print(f"waiting for {len(instance_ids)} instances to be terminated")
    waiter = ec2.get_waiter("instance_terminated")

    waiter.wait(InstanceIds=instance_ids)
    print("all instances terminated")

    # delete autoscaling group
    response = autoscaling.delete_auto_scaling_group(
        AutoScalingGroupName=first_asg, ForceDelete=True
    )


# check launch template exists
try:
    response = ec2.describe_launch_templates(LaunchTemplateNames=["ASGDemoTemplate"])
    response = ec2.delete_launch_template(LaunchTemplateName="ASGDemoTemplate")
    print("launch template deleted")
except Exception as e:
    print("launch template does not exist")

# delete cloudwatch alarm named ASGDemoAlarm
cloudwatch = boto3.client("cloudwatch")
# check cloudwatch alarm exists
try:
    response = cloudwatch.describe_alarms(AlarmNames=["ASGDemoAlarm"])
    response = cloudwatch.delete_alarms(AlarmNames=["ASGDemoAlarm"])
    print("cloudwatch alarm deleted")
except Exception as e:
    print("cloudwatch alarm does not exist")


ec2.close()
cloudwatch.close()
autoscaling.close()
