import boto3

# remove all identity pool
client = boto3.client("cognito-identity")

response = client.list_identity_pools(MaxResults=10)
for identity_pool in response["IdentityPools"]:
    print(f"Deleting {identity_pool['IdentityPoolName']}")
    client.delete_identity_pool(IdentityPoolId=identity_pool["IdentityPoolId"])


role_name = "IdentityPoolTestRole"

# remove role
iam = boto3.client("iam")
try:
    role = iam.get_role(RoleName=role_name)

    # remove all attached policies
    policies = iam.list_attached_role_policies(RoleName=role_name)["AttachedPolicies"]
    for policy in policies:
        iam.detach_role_policy(RoleName=role_name, PolicyArn=policy["PolicyArn"])
        print(f"Policy {policy['PolicyName']} detached")
        if policy["PolicyName"] != "IdentityPoolTestPolicy":
            iam.delete_policy(PolicyArn=policy["PolicyArn"])
            print(f"Policy {policy['PolicyName']} deleted")

    if role:
        iam.delete_role(RoleName=role_name)
        print(f"Role {role_name} deleted")
    else:
        print(f"Role {role_name} not found")


except iam.exceptions.NoSuchEntityException:
    print(f"Role {role_name} not found")

iam.close()
client.close()
