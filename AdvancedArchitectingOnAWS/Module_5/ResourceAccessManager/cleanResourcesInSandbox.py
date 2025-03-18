import boto3

ec2_instance_name = "MyWebServer"
# list all ec2 instances which name matches with ec2_instance_name and that are in running status
ec2_client = boto3.client("ec2")

response = ec2_client.describe_instances(
    Filters=[
        {"Name": "tag:Name", "Values": [ec2_instance_name]},
        {"Name": "instance-state-name", "Values": ["running", "pending"]},
    ]
)

if len(response["Reservations"]) == 0:
    print(f"No instance found with name {ec2_instance_name}")
    exit(1)

# terminate all these instances
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        ec2_client.terminate_instances(InstanceIds=[instance["InstanceId"]])
        print(f"Terminating instance {instance['InstanceId']}")

# wait until all instances are terminated
waiter = ec2_client.get_waiter("instance_terminated")
waiter.wait(
    InstanceIds=[
        instance["InstanceId"]
        for reservation in response["Reservations"]
        for instance in reservation["Instances"]
    ]
)
