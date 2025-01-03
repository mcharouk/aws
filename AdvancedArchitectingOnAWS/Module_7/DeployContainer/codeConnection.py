import boto3

connection_name = "sample-app-repo"

client = boto3.client("codeconnections")
# list connections to get connection arn
connections = client.list_connections(ProviderTypeFilter="GitHub")
for connection in connections["Connections"]:
    if connection_name in connection["ConnectionName"]:
        connection_arn = connection["ConnectionArn"]
        print(connection_arn)


# get code connection

response = client.get_connection(ConnectionArn=connection_arn)
print(response["Connection"])

# delete connection
client.delete_connection(ConnectionArn=connection_arn)

client.create_connection(ProviderType="GitHub", ConnectionName=connection_name)
