import boto3


# remove resource share named SubnetShareDemo if it exists
def remove_resource_share():
    ram = boto3.client("ram")
    response = ram.get_resource_shares(
        name="SubnetShareDemo", resourceOwner="SELF", resourceShareStatus="ACTIVE"
    )
    if len(response["resourceShares"]) > 0:
        resource_share_arn = response["resourceShares"][0]["resourceShareArn"]
        ram.delete_resource_share(resourceShareArn=resource_share_arn)
        print(f"Resource share with ARN [{resource_share_arn}] removed")
    else:
        print("Resource share not found")


remove_resource_share()
