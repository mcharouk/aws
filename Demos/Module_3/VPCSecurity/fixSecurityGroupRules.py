import boto3

security_group_name = "VPCSecurityDemo-SecurityGroup"


ec2_client = boto3.client("ec2")

# get security group id
response = ec2_client.describe_security_groups(
    Filters=[{"Name": "group-name", "Values": [security_group_name]}]
)
security_group_id = response["SecurityGroups"][0]["GroupId"]


# add egress rule to security group
def add_egress_rule(security_group_id, from_port, to_port, description):
    ec2_client.authorize_security_group_egress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": from_port,
                "ToPort": to_port,
                "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": description}],
            }
        ],
    )
    print("added ountbound rule to security group")


add_egress_rule(
    security_group_id,
    80,
    80,
    "Allow all outbound http traffic for yum update",
)
add_egress_rule(
    security_group_id,
    443,
    443,
    "Allow all outbound https traffic for yum update",
)
add_egress_rule(
    security_group_id,
    20,
    21,
    "Allow all outbound ftp traffic for yum update",
)
