import boto3

database_name = "training-data"
table_name = "cities"
data_filter_name = "JapaneseCities"
principal = "businessAnalystRole"

# get ARN of principal

iam = boto3.client("iam")

response = iam.get_role(RoleName=principal)
principal_arn = response["Role"]["Arn"]
iam.close()

# select lake formation permissions with principals as

lf = boto3.client("lakeformation")


print(f"Revoking permission of {principal_arn}")
try:
    permissions = lf.revoke_permissions(
        Principal={"DataLakePrincipalIdentifier": principal_arn},
        Resource={
            "DataCellsFilter": {
                "DatabaseName": database_name,
                "TableName": table_name,
                "Name": data_filter_name,
            },
        },
        Permissions=["SELECT"],
    )
    print("Permission revoked")
except lf.exceptions.EntityNotFoundException:
    print("Permission does not exist")


# delete data filter
print(f"Deleting data filter {data_filter_name}")

# get current account
sts = boto3.client("sts")
account_id = sts.get_caller_identity()["Account"]
sts.close()
try:
    lf.delete_data_cells_filter(
        TableCatalogId=account_id,
        DatabaseName=database_name,
        TableName=table_name,
        Name=data_filter_name,
    )
    print("Data filter deleted")
except lf.exceptions.EntityNotFoundException:
    print("Data filter does not exist")


lf.close()
# remove glue table if it exists
glue_client = boto3.client("glue")

try:
    glue_client.delete_table(DatabaseName=database_name, Name=table_name)
    print("Table deleted")
except glue_client.exceptions.EntityNotFoundException:
    print("Table does not exist")

glue_client.close()
