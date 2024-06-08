import boto3
from botocore.config import Config


def delete_all_images(config):
    print("deleting images on region " + config.region_name)
    ec2 = boto3.client("ec2", config=config)

    # list all custom AMIs in eu-west-1 and eu-west-3 region
    # deregister all custom AMIs

    response = ec2.describe_images(Owners=["self"])
    for image in response["Images"]:
        print(image["ImageId"])
        ec2.deregister_image(ImageId=image["ImageId"])
        print("Deleted image: ", image["ImageId"])


delete_all_images(Config(region_name="eu-west-1"))
delete_all_images(Config(region_name="eu-west-3"))

# list all EBS snapshots
# delete all EBS snapshots


ec2 = boto3.client("ec2")

response = ec2.describe_snapshots(OwnerIds=["self"])
print(response)

for snapshot in response["Snapshots"]:
    print(snapshot["SnapshotId"])
    ec2.delete_snapshot(SnapshotId=snapshot["SnapshotId"])
    print("Deleted snapshot: ", snapshot["SnapshotId"])

# delete all image pipelines in image builder

imagebuilder = boto3.client("imagebuilder")

response = imagebuilder.list_image_pipelines()
for pipeline in response["imagePipelineList"]:
    print(pipeline["name"])
    imagebuilder.delete_image_pipeline(imagePipelineArn=pipeline["arn"])
    print("Deleted image pipeline: ", pipeline["name"])

# delete all image recipes in image builder

imagebuilder = boto3.client("imagebuilder")

response = imagebuilder.list_image_recipes()

for recipe in response["imageRecipeSummaryList"]:
    print(recipe["name"])
    imagebuilder.delete_image_recipe(imageRecipeArn=recipe["arn"])
    print("Deleted image recipe: ", recipe["name"])

# delete all infrastructure configurations in image builder

response = imagebuilder.list_infrastructure_configurations()

for config in response["infrastructureConfigurationSummaryList"]:
    print(config["name"])
    imagebuilder.delete_infrastructure_configuration(
        infrastructureConfigurationArn=config["arn"]
    )
    print("Deleted infrastructure configuration: ", config["name"])

# delete all distribution settings in image builder

response = imagebuilder.list_distribution_configurations()
for config in response["distributionConfigurationSummaryList"]:
    print(config["name"])
    imagebuilder.delete_distribution_configuration(
        distributionConfigurationArn=config["arn"]
    )
    print("Deleted distribution configuration: ", config["name"])


# delete all image components in image builder

response = imagebuilder.list_components()
for component in response["componentVersionList"]:
    print(component["arn"])
    build_versions = imagebuilder.list_component_build_versions(
        componentVersionArn=component["arn"]
    )
    for buildVersion in build_versions["componentSummaryList"]:
        print(buildVersion["arn"])
        imagebuilder.delete_component(componentBuildVersionArn=buildVersion["arn"])
        print("Deleted component: ", buildVersion["arn"])
