import boto3

# delete cloudformation stack named demo-marccharouk-labtemplate-123456
client = boto3.client("cloudformation")

client.delete_stack(StackName="demo-marccharouk-labtemplate-123456")
print("Stack deleted")
