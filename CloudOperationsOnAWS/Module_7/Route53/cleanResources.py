import boto3

# get private hosted zone
route53 = boto3.client("route53")


def get_hosted_zone_id(domain):
    """
    Get the hosted zone ID for a given domain.
    """

    response = route53.list_hosted_zones_by_name(DNSName=domain, MaxItems="1")
    if (
        response["ResponseMetadata"]["HTTPStatusCode"] == 200
        and len(response["HostedZones"]) > 0
    ):
        hosted_zone_id = response["HostedZones"][0]["Id"]
        return hosted_zone_id
    else:
        return None


hosted_zone_id = get_hosted_zone_id("route53.demo.com")

# get all alias records of private hosted zone

if hosted_zone_id:

    response = route53.list_resource_record_sets(
        HostedZoneId=hosted_zone_id, MaxItems="100"
    )
    for record in response["ResourceRecordSets"]:
        if record["Type"] == "A" and record["AliasTarget"]:
            print(f"Deleting record: {record['Name']}")
            route53.change_resource_record_sets(
                HostedZoneId=hosted_zone_id,
                ChangeBatch={
                    "Changes": [{"Action": "DELETE", "ResourceRecordSet": record}]
                },
            )

# delete private hosted zone

if hosted_zone_id:
    route53.delete_hosted_zone(Id=hosted_zone_id)
    print(f"Deleted hosted zone: {hosted_zone_id}")

route53.close()
