import boto3


# create license configuration
def create_license_configuration():
    client = boto3.client("license-manager", region_name="eu-west-1")

    response = client.create_license_configuration(
        Name="MyTestLicense",
        Description="Test license backed by Launch Template",
        LicenseCountingType="Instance",
        LicenseCount=1,
        LicenseCountHardLimit=True,
    )
    client.close()
    licenseConfigurationARN = response["LicenseConfigurationArn"]
    print(f"License Configuration created with ARN {licenseConfigurationARN}")


def remove_license_configuration():
    client = boto3.client("license-manager", region_name="eu-west-1")

    # get all license configuration and remove them
    response = client.list_license_configurations()

    if len(response["LicenseConfigurations"]) == 0:
        print("No license configuration found")
        return

    for licenseConfiguration in response["LicenseConfigurations"]:
        licenseConfigurationArn = licenseConfiguration["LicenseConfigurationArn"]
        print(f"Removing License Configuration with ARN {licenseConfigurationArn}")
        client.delete_license_configuration(
            LicenseConfigurationArn=licenseConfigurationArn
        )

    client.close()


def get_license_configuration_arn():
    client = boto3.client("license-manager", region_name="eu-west-1")

    response = client.list_license_configurations()
    if len(response["LicenseConfigurations"]) == 0:
        print("No license configuration found")
        return None

    client.close()
    return response["LicenseConfigurations"][0]["LicenseConfigurationArn"]
