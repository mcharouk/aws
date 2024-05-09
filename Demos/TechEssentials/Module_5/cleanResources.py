import boto3

dynamodb_table_name = "Organizations"

# delete dynamodb table
dynamodb = boto3.resource("dynamodb")
dynamodb.Table(dynamodb_table_name).delete()
print("DynamoDB table deleted successfully")
