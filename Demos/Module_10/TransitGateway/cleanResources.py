# select all transit gateway route tables

import time

import boto3

ec2 = boto3.client("ec2")


def get_transit_gateway_route_tables():
    response = ec2.describe_transit_gateway_route_tables()
    return response["TransitGatewayRouteTables"]


route_tables = get_transit_gateway_route_tables()

default_route_table = None
custom_route_table = None

if len(route_tables) == 0:
    print("no route tables found")

for route_table in route_tables:
    if route_table["DefaultAssociationRouteTable"] == True:
        default_route_table = route_table
    else:
        custom_route_table = route_table

if custom_route_table is not None:
    # disassociate all associations
    custom_route_table_id = custom_route_table["TransitGatewayRouteTableId"]
    associations = ec2.get_transit_gateway_route_table_associations(
        TransitGatewayRouteTableId=custom_route_table_id
    )["Associations"]

    attachments = []
    for association in associations:
        attachmentId = association["TransitGatewayAttachmentId"]
        ec2.disassociate_transit_gateway_route_table(
            TransitGatewayRouteTableId=custom_route_table_id,
            TransitGatewayAttachmentId=attachmentId,
        )
        attachments.append(attachmentId)

    attachmentDisassosiationCompleted = False
    while attachmentDisassosiationCompleted == False:
        print("checking for associations")
        associations = ec2.get_transit_gateway_route_table_associations(
            TransitGatewayRouteTableId=custom_route_table_id
        )["Associations"]

        attachmentDisassosiationCompleted = True
        for association in associations:
            if association["State"] != "disassociated":
                attachmentDisassosiationCompleted = False
                break

        if attachmentDisassosiationCompleted == False:
            print("waiting for attachments to disassociate")
            time.sleep(5)

    print("attaching to default route table")
    for attachment_id in attachments:
        ec2.associate_transit_gateway_route_table(
            TransitGatewayRouteTableId=default_route_table[
                "TransitGatewayRouteTableId"
            ],
            TransitGatewayAttachmentId=attachment_id,
        )

    print("deleting custom route table")
    ec2.delete_transit_gateway_route_table(
        TransitGatewayRouteTableId=custom_route_table_id
    )
else:
    print("no custom route table found")
