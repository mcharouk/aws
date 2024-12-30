# list VPC peering connection
import boto3

ec2 = boto3.client("ec2")


# delete routes that references peering connection
def delete_routes(vpc_peering_id):
    try:
        response = ec2.describe_route_tables(
            Filters=[
                {
                    "Name": "route.vpc-peering-connection-id",
                    "Values": [
                        vpc_peering_id,
                    ],
                },
            ]
        )
        for route_table in response["RouteTables"]:
            for route in route_table["Routes"]:
                if (
                    "VpcPeeringConnectionId" in route
                    and route["VpcPeeringConnectionId"] == vpc_peering_id
                ):
                    route_table_id = route_table["RouteTableId"]
                    destination_cidr_block = route["DestinationCidrBlock"]
                    print(
                        "deleting route from route table "
                        + route_table_id
                        + " destination "
                        + destination_cidr_block
                        + " and vpc peering "
                        + route["VpcPeeringConnectionId"]
                    )
                    ec2.delete_route(
                        RouteTableId=route_table_id,
                        DestinationCidrBlock=destination_cidr_block,
                    )
    except Exception as e:
        raise e
    return None


# list VPC peering connection and return first one
def list_vpc_peering():
    try:
        response = ec2.describe_vpc_peering_connections()
        if len(response["VpcPeeringConnections"]) == 0:
            return None
        for peeringConnection in response["VpcPeeringConnections"]:
            if peeringConnection["Status"]["Code"] == "active":
                return peeringConnection["VpcPeeringConnectionId"]

    except Exception as e:
        raise e
    return None


# delete VPC Peering
def delete_vpc_peering(vpc_peering_id):
    try:
        print("deleting vpc peering " + vpc_peering_id)
        response = ec2.delete_vpc_peering_connection(
            VpcPeeringConnectionId=vpc_peering_id
        )
        return response
    except Exception as e:
        raise e


vpcPeeringConnectionId = list_vpc_peering()
if vpcPeeringConnectionId is not None:
    delete_routes(vpcPeeringConnectionId)
    delete_vpc_peering(vpcPeeringConnectionId)
else:
    print("no vpc peering found")
