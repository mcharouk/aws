import os

os.environ.pop("AWS_PROFILE", None)

# display all scps
import boto3

org = boto3.client("organizations")

# get id or OU named Sandbox

root_id = org.list_roots()["Roots"][0]["Id"]
ou_id = None
ou_name = "Sandbox"
ou_list = org.list_organizational_units_for_parent(ParentId=root_id)
for ou in ou_list["OrganizationalUnits"]:
    if ou["Name"] == ou_name:
        ou_id = ou["Id"]
        break

if ou_id is None:
    print(f"OU {ou_name} OU not found")
    exit(1)

scp_id = None
scp_name = "DenyLargeInstancePolicy"
scps = org.list_policies_for_target(TargetId=ou_id, Filter="SERVICE_CONTROL_POLICY")
for scp in scps["Policies"]:
    if scp["Name"] == scp_name:
        scp_id = scp["Id"]

if scp_id is None:
    print(f"Policy named {scp_name} not found")
    exit(1)

org.detach_policy(PolicyId=scp_id, TargetId=ou_id)

print(f"SCP {scp_name} detached from OU {ou_name}")

org.delete_policy(PolicyId=scp_id)
print(f"SCP {scp_name} deleted")
