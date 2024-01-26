# remove all state machines of step functions

import boto3

client = boto3.client("stepfunctions")

response = client.list_state_machines()

for state_machine in response["stateMachines"]:
    print(state_machine["name"])
    client.delete_state_machine(stateMachineArn=state_machine["stateMachineArn"])
    print("deleted")
