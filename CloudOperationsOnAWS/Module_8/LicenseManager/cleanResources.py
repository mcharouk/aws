import time

import boto3
import LicenseConfigurationFactory

# terminate all instances in running state
ec2 = boto3.client("ec2", region_name="eu-west-1")
lim = boto3.client("license-manager", region_name="eu-west-1")

response = ec2.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
)
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminating instance {instance_id}")

# get license usage
licenseArn = LicenseConfigurationFactory.get_license_configuration_arn()

while True:
    response = lim.get_license_configuration(
        LicenseConfigurationArn=licenseArn,
    )
    consumed_licenses = response["ConsumedLicenses"]
    if consumed_licenses == 0:
        break
    print(
        f"Consumed licences = {consumed_licenses}. Waiting for all licenses to be released..."
    )
    time.sleep(10)

LicenseConfigurationFactory.remove_license_configuration()

lim.close()
ec2.close()
