import boto3

endpoint_url = "http://localhost:8000"
ddb = boto3.client("dynamodb", endpoint_url=endpoint_url)
response = ddb.list_tables()

# print table names
for table in response["TableNames"]:
    print(table)

# get item from Employee table
response = ddb.get_item(
    TableName="Employee", Key={"LastName": {"S": "James"}, "FirstName": {"S": "Lebron"}}
)
print(response["Item"])
