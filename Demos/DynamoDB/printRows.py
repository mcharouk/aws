import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("demo_employee")

# print all rows of dynamotable named demo_employee

response = table.scan()
for i in response["Items"]:
    print(i)
