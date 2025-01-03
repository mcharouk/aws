import boto3

route_table_name = "NetworkFirewallStack/VPC/IGW"
# get route table and remove all edge associations

client = boto3.client("ec2")

response = client.describe_route_tables(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": [
                route_table_name,
            ],
        },
    ],
)
route_table_id = response["RouteTables"][0]["RouteTableId"]
route_table_associations = response["RouteTables"][0]["Associations"]
for association in route_table_associations:
    client.disassociate_route_table(
        AssociationId=association["RouteTableAssociationId"]
    )
    print(f"Disassociated {association['RouteTableAssociationId']}")

# delete all non default routes
for route in response["RouteTables"][0]["Routes"]:
    if route["DestinationCidrBlock"] != "10.0.0.0/16":
        client.delete_route(
            RouteTableId=route_table_id,
            DestinationCidrBlock=route["DestinationCidrBlock"],
        )
        print(f"Deleted route {route['DestinationCidrBlock']}")


vpc_name = "Network-firewall-VPC"

# get id of VPC
response = client.describe_vpcs(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": [
                vpc_name,
            ],
        },
    ],
)
vpc_id = response["Vpcs"][0]["VpcId"]
# get id of internet gateway attached to VPC
response = client.describe_internet_gateways(
    Filters=[
        {
            "Name": "attachment.vpc-id",
            "Values": [
                vpc_id,
            ],
        },
    ],
)
igw_id = response["InternetGateways"][0]["InternetGatewayId"]


route_table_name = "NetworkFirewallStack/VPC/PublicSubnet1"

# change the route with destination as 0.0.0.0/0, to target internet gateway
response = client.describe_route_tables(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": [
                route_table_name,
            ],
        },
    ],
)

route_table_id = response["RouteTables"][0]["RouteTableId"]
for route in response["RouteTables"][0]["Routes"]:
    if route["DestinationCidrBlock"] == "0.0.0.0/0":
        client.replace_route(
            RouteTableId=route_table_id,
            DestinationCidrBlock=route["DestinationCidrBlock"],
            GatewayId=igw_id,
        )
        print(f"Replaced route {route['DestinationCidrBlock']}")
