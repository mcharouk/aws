import os

import boto3


def detach_and_delete_policy(org, ou_id, policy_id):
    org.detach_policy(PolicyId=policy_id, TargetId=ou_id)
    print(f"Policy {policy_id} detached from OU {ou_id}")
    org.delete_policy(PolicyId=policy_id)
    print(f"Policy {policy_id} deleted")


def get_policy_id(org, ou_id, policy_name, policy_type):

    policies = org.list_policies_for_target(TargetId=ou_id, Filter=policy_type)

    for policy in policies["Policies"]:
        if policy["Name"] == policy_name:
            return policy["Id"]

    print(f"Policy named {policy_name} not found")


def get_scp_id(org, ou_id, scp_name):
    return get_policy_id(org, ou_id, scp_name, "SERVICE_CONTROL_POLICY")


def get_tag_policy_id(org, ou_id, tag_policy_name):
    return get_policy_id(org, ou_id, tag_policy_name, "TAG_POLICY")


def get_ou_id(org, ou_name):

    # get id or OU named Sandbox

    root_id = org.list_roots()["Roots"][0]["Id"]

    ou_list = org.list_organizational_units_for_parent(ParentId=root_id)
    for ou in ou_list["OrganizationalUnits"]:
        if ou["Name"] == ou_name:
            return ou["Id"]

    print(f"OU {ou_name} OU not found")
    exit(1)


def cleanPoliciesResources():
    os.environ.pop("AWS_PROFILE", None)
    org = boto3.client("organizations")
    ou_name = "Sandbox"
    ou_id = get_ou_id(org, ou_name)

    scp_name = "EnforceTagOnSNS"
    scp_id = get_scp_id(org, ou_id, scp_name)
    if scp_id is not None:
        detach_and_delete_policy(org, ou_id, scp_id)

    tag_policy_name = "TeamNamePolicy"
    tag_policy_id = get_tag_policy_id(org, ou_id, tag_policy_name)
    if tag_policy_id is not None:
        detach_and_delete_policy(org, ou_id, tag_policy_id)

    org.close()


cleanPoliciesResources()
