import boto3

table_name = "Employee"

# if table exists, delete it and wait until delete is completed
client = boto3.client("dynamodb")

try:
    response = client.delete_table(TableName=table_name)
    waiter = client.get_waiter("table_not_exists")
    waiter.wait(TableName=table_name)
    print(f"table {table_name} has been deleted")
except:
    print(f"table {table_name} does not exist")
