import boto3
import LicenseConfigurationFactory

# terminate all instances in running state

lim = boto3.client("license-manager", region_name="eu-west-1")


my_license_arn = LicenseConfigurationFactory.get_license_configuration_arn()

if my_license_arn is None:
    lim.close()
    exit(0)
# get all resources attached to license
response = lim.list_usage_for_license_configuration(
    LicenseConfigurationArn=my_license_arn,
)
instance_ids = []
for usage in response["LicenseConfigurationUsageList"]:
    # get instance id from ARN
    instance_id = usage["ResourceArn"].split("/")[1]
    instance_ids.append(instance_id)


if len(list(instance_ids)) > 0:
    ec2 = boto3.client("ec2", region_name="eu-west-1")
    print("Terminating " + ",".join(instance_ids))
    ec2.terminate_instances(InstanceIds=instance_ids)
    waiter = ec2.get_waiter("instance_terminated")
    waiter.wait(InstanceIds=instance_ids)
    print("all instances terminated in vpc ")
    ec2.close()
else:
    print("no instances to terminate")

# get license usage
LicenseConfigurationFactory.get_license_configuration_arn()
LicenseConfigurationFactory.remove_license_configuration()
lim.close()
