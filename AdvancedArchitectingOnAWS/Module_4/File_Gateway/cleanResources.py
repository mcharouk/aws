import boto3

# delete file gateway file share
client = boto3.client("storagegateway")

# get first file share if it exists and delete it
file_shares = client.list_file_shares()["FileShareInfoList"]
if len(file_shares) > 0:
    file_share_arn = file_shares[0]["FileShareARN"]
    client.delete_file_share(FileShareARN=file_share_arn)
    print("File share deleted")
else:
    print("No file share found")

# get first file gateway and delete it if it exists
file_gateways = client.list_gateways()["Gateways"]
if len(file_gateways) > 0:
    file_gateway_arn = file_gateways[0]["GatewayARN"]
    client.delete_gateway(GatewayARN=file_gateway_arn)
    print("File gateway deleted")
else:
    print("No file gateway found")
