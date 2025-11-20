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
       
    response = iam.list_attached_role_policies(RoleName=role_name)
    for policy in response["AttachedPolicies"]:
        awsManagedARNPrefix = "arn:aws:iam::aws"
        iam.detach_role_policy(RoleName=role_name, PolicyArn=policy["PolicyArn"])
        print(policy["PolicyArn"] + " detached successfully")        

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
    print("bucket" + bucket_name + " deleted successfully")
else:
    print("bucket" + bucket_name + " does not exist")
