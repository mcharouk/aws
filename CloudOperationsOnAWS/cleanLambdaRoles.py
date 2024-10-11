# get all policies which name starts with AWSLambdaBasicExecutionRole
import boto3


def get_policies_with_prefix(prefix):
    """
    Retrieves a list of policies whose names start with the given prefix.
    """
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_policies")
    policies = []
    for response in paginator.paginate(Scope="Local", PathPrefix="/"):
        for policy in response["Policies"]:
            if policy["PolicyName"].startswith(prefix):
                policies.append(policy)
    return policies


class Role:
    def __init__(self, policy_arn, role_name):
        self.policy_arn = policy_arn
        self.role_name = role_name


# get all roles that are associated with these policies
def get_roles_for_policies(policies):
    """
    Retrieves a list of roles that are associated with the given policies.
    """
    iam = boto3.client("iam")
    roles = []
    for policy in policies:
        paginator = iam.get_paginator("list_entities_for_policy")
        for response in paginator.paginate(PolicyArn=policy["Arn"]):
            for role in response["PolicyRoles"]:
                roles.append(Role(policy["Arn"], role["RoleName"]))
    return roles


# Example usage
policies = get_policies_with_prefix("AWSLambdaBasicExecutionRole")
for policy in policies:
    print(policy["PolicyName"])
roles = get_roles_for_policies(policies)
for role in roles:
    print(role.role_name)

# for each role, detach the policies
# delete all roles
# delete all policies

# detach policies from roles
iam = boto3.client("iam")

for role in roles:
    iam.detach_role_policy(RoleName=role.role_name, PolicyArn=role.policy_arn)
    print(f"Detached {policy['PolicyName']} from {role}")

    # delete roles
    iam.delete_role(RoleName=role.role_name)
    print(f"Deleted {role}")

for policy in policies:
    # delete policies
    iam.delete_policy(PolicyArn=policy["Arn"])
    print(f"Deleted {policy['PolicyName']}")
