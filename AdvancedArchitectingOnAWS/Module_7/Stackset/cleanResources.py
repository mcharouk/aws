import time

import boto3

stackset_name = "stackset-demo-sqs"


# get stack set,
client = boto3.client("cloudformation")

# catch StackSetNotFoundException
try:
    response = client.describe_stack_set(StackSetName=stackset_name)
    # delete stack instances
    if len(response["StackSet"]["Regions"]) > 0:
        delete_stack_instances_response = client.delete_stack_instances(
            StackSetName=stackset_name,
            RetainStacks=False,
            Regions=response["StackSet"]["Regions"],
            DeploymentTargets={
                "OrganizationalUnitIds": response["StackSet"]["OrganizationalUnitIds"]
            },
        )
        operation_id = delete_stack_instances_response["OperationId"]
        # wait until all stack instances are deleted
        operation_status = None
        while operation_status != "SUCCEEDED":
            operation = client.describe_stack_set_operation(
                StackSetName=stackset_name, OperationId=operation_id
            )
            operation_status = operation["StackSetOperation"]["Status"]
            time.sleep(5)
            print(f"operation status: {operation_status}")
        print("stack instances have been deleted")

    # delete stack set
    response = client.delete_stack_set(StackSetName=stackset_name)
    print(f"stackset {stackset_name} has been deleted")


except client.exceptions.StackSetNotFoundException as e:
    print(f"stackset {stackset_name} has not been found")
