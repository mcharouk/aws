import boto3

security_group_name = "VPCSecurityDemo-SecurityGroup"


ec2_client = boto3.client("ec2")

# get security group id
response = ec2_client.describe_security_groups(
    Filters=[{"Name": "group-name", "Values": [security_group_name]}]
)
security_group_id = response["SecurityGroups"][0]["GroupId"]


# remove ingress rule from security group
def remove_security_group_rule(security_group_id, from_port, to_port, ip_ranges):
    print(
        "removing inbound security groupe rule from port "
        + str(from_port)
        + " to "
        + str(to_port)
        + " from "
        + ip_ranges
    )
    ec2_client.revoke_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": from_port,
                "ToPort": to_port,
                "IpRanges": [{"CidrIp": ip_ranges}],
            }
        ],
    )


# remove_security_group_rule(security_group_id, 80, 80, "0.0.0.0/0")


# remove network acl inbound rule
def remove_nacl_rule(egress, network_acl_id, rule_number):
    print(
        "removing nacl rule number "
        + str(rule_number)
        + " from "
        + network_acl_id
        + " and egress "
        + str(egress)
    )
    ec2_client.delete_network_acl_entry(
        Egress=egress,
        NetworkAclId=network_acl_id,
        RuleNumber=rule_number,
    )


# get inbound rule number that allows http from anywhere
def get_network_acl_rule_number(
    network_acls_entries, egress, port_from, port_to, protocol, cidrblock, rule_action
):

    for entry in network_acls_entries:
        if (
            "PortRange" in entry
            and entry["Egress"] == egress
            and entry["PortRange"]["From"] == port_from
            and entry["PortRange"]["To"] == port_to
            and entry["Protocol"] == protocol
            and entry["CidrBlock"] == cidrblock
            and entry["RuleAction"] == rule_action
        ):
            return entry["RuleNumber"]

    return None


def remove_acl_rule(
    network_acl_id,
    entries,
    egress,
    port_from,
    port_to,
    protocol,
    cidrblock,
    rule_action,
):
    rule_number = get_network_acl_rule_number(
        entries, egress, port_from, port_to, protocol, cidrblock, rule_action
    )
    if rule_number is not None:
        remove_nacl_rule(egress, network_acl_id, rule_number)


networkAclName = "VPCSecurityDemo-PublicNetworkAcl"
# select acl id
response = ec2_client.describe_network_acls(
    Filters=[{"Name": "tag:Name", "Values": [networkAclName]}]
)
network_acl_id = response["NetworkAcls"][0]["NetworkAclId"]

network_acls = ec2_client.describe_network_acls(
    NetworkAclIds=[
        network_acl_id,
    ]
)

remove_acl_rule(
    network_acl_id,
    response["NetworkAcls"][0]["Entries"],
    False,
    80,
    80,
    "6",
    "0.0.0.0/0",
    "allow",
)

remove_acl_rule(
    network_acl_id,
    response["NetworkAcls"][0]["Entries"],
    True,
    1024,
    65535,
    "6",
    "0.0.0.0/0",
    "allow",
)
