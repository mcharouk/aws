import os
import shutil

import utils

utils.change_current_directory()

# delete folder layer-package if it exists
folder_path = "layer-package"

if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    print("The folder has been deleted successfully.")
else:
    print("The folder does not exist.")


# delete all application in CloudWatch Application Insights
import boto3

application_insights = boto3.client("applicationinsights")
resource_group = boto3.client("resource-groups")


response = application_insights.list_applications()
applications = response["ApplicationInfoList"]
resource_group_name = ""
for application in applications:
    resource_group_name = application["ResourceGroupName"]
    print(f"Deleting application {resource_group_name}")
    application_insights.delete_application(ResourceGroupName=resource_group_name)
    print(f"Deleted application linked to resource group {resource_group_name}")
    # delete resource group
    resource_group.delete_group(GroupName=resource_group_name)
    print(f"Deleted resource group {resource_group_name}")

application_insights.close()
resource_group.close()
