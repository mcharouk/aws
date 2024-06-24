import boto3

# loop on all glue databases and drop all tables
glue = boto3.client("glue")
databases = glue.get_databases()["DatabaseList"]
for database in databases:
    database_name = database["Name"]
    print(f"Deleting tables of database: {database_name}")
    tables = glue.get_tables(DatabaseName=database_name)["TableList"]
    for table in tables:
        table_name = table["Name"]
        glue.delete_table(DatabaseName=database_name, Name=table_name)
        print(f"Table {table_name} deleted")
