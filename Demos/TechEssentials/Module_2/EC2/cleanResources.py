import time

import boto3

# select all ec2 instances in vpc named ComputeDemo

ec2 = boto3.client("ec2")
vpc_list = ec2.describe_vpcs(Filters=[{"Name": "tag:Name", "Values": ["ComputeDemo"]}])
vpc_id = vpc_list["Vpcs"][0]["VpcId"]

ec2_res = boto3.resource("ec2")
vpc = ec2_res.Vpc(vpc_id)
vpc.instances.all().terminate()

all_instances_terminated = False
while all_instances_terminated == False:
    running_instances = ec2.describe_instances(
        Filters=[
            {"Name": "instance-state-name", "Values": ["running", "shutting-down"]}
        ]
    )
    if (
        len(running_instances["Reservations"]) != 0
        and len(running_instances["Reservations"][0]["Instances"]) != 0
    ):
        print("waiting for instances to terminate")
        time.sleep(5)
    else:
        all_instances_terminated = True
        print("all instances terminated in vpc " + vpc_id)

subnet_list = ec2.describe_subnets(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])
subnet_id = subnet_list["Subnets"][0]["SubnetId"]
route_table_list = ec2.describe_route_tables(
    Filters=[{"Name": "association.subnet-id", "Values": [subnet_id]}]
)
if len(route_table_list["RouteTables"]) != 0:
    route_table_id = route_table_list["RouteTables"][0]["RouteTableId"]
    routes = route_table_list["RouteTables"][0]["Routes"]
    has_default_ip = False
    for route in routes:
        if route["DestinationCidrBlock"] == "0.0.0.0/0":
            has_default_ip = True
            break

    if has_default_ip:
        ec2.delete_route(DestinationCidrBlock="0.0.0.0/0", RouteTableId=route_table_id)
        print("route to internet gateway removed for route table " + route_table_id)
    else:
        print(
            "no route to internet gateway to remove for route table " + route_table_id
        )

# detach internate gateway from vpc named ComputeDemo and delete internet gateway

igw_it = ec2_res.internet_gateways.filter(
    Filters=[{"Name": "attachment.vpc-id", "Values": [vpc_id]}]
)
if len(list(igw_it)) == 0:
    print("no internet gateway attached to vpc " + vpc_id)
else:
    igw = list(igw_it)[0]
    vpc.detach_internet_gateway(InternetGatewayId=igw.id)
    print("internet gateway " + igw.id + " detached")
    ec2.delete_internet_gateway(InternetGatewayId=igw.id)
    print("internet gateway " + igw.id + " deleted")
