import awswrangler as wr
import pandas as pd

dynamodb_table_name = "Organizations"
csv_location = "organizations-100.csv"


import os

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("Demos"):
    new_wd = "TechEssentials/Module_5"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

df = pd.read_csv(csv_location)
wr.dynamodb.put_df(df, table_name=dynamodb_table_name)
print("Data ingestion done")
