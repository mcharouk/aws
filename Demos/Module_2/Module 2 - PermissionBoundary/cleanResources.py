# remove iam role named LambdaRole
import boto3

role_name = "LambdaRole"
iam = boto3.client("iam")

# check if role exists

try:
    response = iam.get_role(RoleName=role_name)

    # remove permission boundary
    role = response["Role"]
    if "PermissionsBoundary" in role:
        permissionBoundaryARN = role["PermissionsBoundary"]["PermissionsBoundaryArn"]
        iam.delete_role_permissions_boundary(RoleName=role_name)
        print("Permissions boundary removed successfully")
        # remove all version of policy
        response = iam.list_policy_versions(PolicyArn=permissionBoundaryARN)
        for version in response["Versions"]:
            if not version["IsDefaultVersion"]:
                iam.delete_policy_version(
                    PolicyArn=permissionBoundaryARN, VersionId=version["VersionId"]
                )
                print(
                    permissionBoundaryARN
                    + " version "
                    + version["VersionId"]
                    + " deleted successfully"
                )
        # remove permission boundary policy
        iam.delete_policy(PolicyArn=permissionBoundaryARN)
        print(permissionBoundaryARN + " deleted successfully")

    response = iam.list_attached_role_policies(RoleName=role_name)
    for policy in response["AttachedPolicies"]:
        awsManagedARNPrefix = "arn:aws:iam::aws"
        iam.detach_role_policy(RoleName=role_name, PolicyArn=policy["PolicyArn"])
        print(policy["PolicyArn"] + " detached successfully")
        if policy["PolicyArn"].startswith(awsManagedARNPrefix):
            print(policy["PolicyArn"] + " is AWS managed, not deleted")
            continue
        policy_arn = policy["PolicyArn"]
        response = iam.list_policy_versions(PolicyArn=policy_arn)
        for version in response["Versions"]:
            if not version["IsDefaultVersion"]:
                iam.delete_policy_version(
                    PolicyArn=policy_arn, VersionId=version["VersionId"]
                )
                print(
                    policy_arn
                    + " version "
                    + version["VersionId"]
                    + " deleted successfully"
                )
        iam.delete_policy(PolicyArn=policy_arn)
        print(policy_arn + " deleted successfully")

    iam.delete_role(RoleName=role_name)
    print(role_name + " deleted successfully")

except iam.exceptions.NoSuchEntityException:
    print(role_name + " does not exist")


bucket_name = "marccharouk-permissionboundary-demo-657489457"
# if bucket exists, empty it and delete it
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

if bucket.creation_date:
    bucket.objects.all().delete()
    bucket.delete()
    print(bucket_name + " deleted successfully")
else:
    print(bucket_name + " does not exist")
