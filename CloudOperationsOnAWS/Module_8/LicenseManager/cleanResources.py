import boto3
import LicenseConfigurationFactory

# terminate all instances in running state
ec2 = boto3.client("ec2", region_name="eu-west-1")
lim = boto3.client("license-manager", region_name="eu-west-1")

response = ec2.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
)
instance_ids = []
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        instance_ids.append(instance_id)
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminating instance {instance_id}")

if len(list(instance_ids)) > 0:
    waiter = ec2.get_waiter("instance_terminated")
    waiter.wait(InstanceIds=instance_ids)
    print("all instances terminated in vpc ")
else:
    print("no instances to terminate")

# get license usage
licenseArn = LicenseConfigurationFactory.get_license_configuration_arn()
LicenseConfigurationFactory.remove_license_configuration()

lim.close()
ec2.close()
