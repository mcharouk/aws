import boto3

codebuild_iam_role_name = "ECS-CICD-CodeBuildServiceRole"

iam = boto3.client("iam")

# get iam role if it exists
response = iam.list_attached_role_policies(RoleName=codebuild_iam_role_name)

# detach all policies except one that starts with ECSCICDCodeBuildPolicy
for policy in response["AttachedPolicies"]:
    if not policy["PolicyName"].startswith("ECSCICDCodeBuildPolicy"):
        policy_arn = policy["PolicyArn"]
        iam.detach_role_policy(RoleName=codebuild_iam_role_name, PolicyArn=policy_arn)

        # remove all policy versions
        response = iam.list_policy_versions(PolicyArn=policy_arn)
        for version in response["Versions"]:
            if not version["IsDefaultVersion"]:
                iam.delete_policy_version(
                    PolicyArn=policy_arn, VersionId=version["VersionId"]
                )
        # remove policy
        print(f"Deleting policy {policy_arn}")
        iam.delete_policy(PolicyArn=policy_arn)

iam.close()

ecr = boto3.client("ecr")

repository_name = "cicd-sample-app"
# delete all images of repository if repository exists
try:
    ecr.describe_repositories(repositoryNames=[repository_name])

    response = ecr.list_images(repositoryName=repository_name)

    if len(response["imageIds"]) == 0:
        print("no images to delete")

    for image in response["imageIds"]:
        print("deleting image " + image["imageDigest"])
        ecr.batch_delete_image(repositoryName=repository_name, imageIds=[image])
        print("deleted image " + image["imageDigest"])
except ecr.exceptions.RepositoryNotFoundException:
    print("repository " + repository_name + " does not exist")

ecr.close()
