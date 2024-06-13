import boto3

# get app config application called TestAppConfig
appconfig = boto3.client("appconfig")

# get first application
response = appconfig.list_applications()
applications = response["Items"]
if len(applications) > 0:
    application_id = applications[0]["Id"]

    environments = appconfig.list_environments(ApplicationId=application_id)
    # delete all environments
    for environment in environments["Items"]:
        appconfig.delete_environment(
            ApplicationId=application_id, EnvironmentId=environment["Id"]
        )
        print(f"Deleted environment {environment['Name']}")

    # delete all configuration profile
    configurationProfiles = appconfig.list_configuration_profiles(
        ApplicationId=application_id
    )
    for configuration_profile in configurationProfiles["Items"]:
        versions = appconfig.list_hosted_configuration_versions(
            ApplicationId=application_id,
            ConfigurationProfileId=configuration_profile["Id"],
        )
        # delete all versions
        for version in versions["Items"]:
            appconfig.delete_hosted_configuration_version(
                ApplicationId=application_id,
                ConfigurationProfileId=configuration_profile["Id"],
                VersionNumber=version["VersionNumber"],
            )
            print(
                f"Deleted version {version['VersionNumber']} of configuration profile {configuration_profile['Name']}"
            )

        appconfig.delete_configuration_profile(
            ApplicationId=application_id,
            ConfigurationProfileId=configuration_profile["Id"],
        )
        print(f"Deleted configuration profile {configuration_profile['Name']}")

    # delete application
    appconfig.delete_application(ApplicationId=application_id)
    print("Deleted application")

else:
    print("No application found")
