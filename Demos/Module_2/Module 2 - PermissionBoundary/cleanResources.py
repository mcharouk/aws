# remove iam role named TechLeadRole
import boto3

techleadRoleName = "TechLeadRole"
iam = boto3.client("iam")

# remove permission boundary from TechLeadRole
response = iam.get_role(RoleName=techleadRoleName)
role = response["Role"]
if "PermissionsBoundary" in role:
    permissionBoundaryARN = role["PermissionsBoundary"]["PermissionsBoundaryArn"]
    iam.delete_role_permissions_boundary(RoleName=techleadRoleName)
    print("Permissions boundary removed successfully")
    # remove permission boundary policy
    iam.delete_policy(PolicyArn=permissionBoundaryARN)
    print(permissionBoundaryARN + " deleted successfully")


response = iam.list_attached_role_policies(RoleName=techleadRoleName)
for policy in response["AttachedPolicies"]:
    awsManagedARNPrefix = "arn:aws:iam::aws"
    iam.detach_role_policy(RoleName=techleadRoleName, PolicyArn=policy["PolicyArn"])
    print(policy["PolicyArn"] + " detached successfully")
    if policy["PolicyArn"].startswith(awsManagedARNPrefix):
        print(policy["PolicyArn"] + " is AWS managed, not deleted")
        continue

    iam.delete_policy(PolicyArn=policy["PolicyArn"])
    print(policy["PolicyArn"] + " deleted successfully")


iam.delete_role(RoleName=techleadRoleName)
print(techleadRoleName + " deleted successfully")

# remove all policies attached to TechLeadRole
