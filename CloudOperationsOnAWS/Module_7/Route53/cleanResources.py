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


hosted_zone_id = get_hosted_zone_id("mcc-aws-demo.fr")

# get all alias records of private hosted zone

if hosted_zone_id:

    response = route53.list_resource_record_sets(
        HostedZoneId=hosted_zone_id, MaxItems="100"
    )
    record_to_delete = []
    for record in response["ResourceRecordSets"]:
        if record["Type"] == "A" and record["GeoLocation"]:
            print(f"Deleting record: {record['Name']}")
            record_to_delete.append({"Action": "DELETE", "ResourceRecordSet": record})

    for record in record_to_delete:
        route53.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={"Changes": record_to_delete},
        )

    if len(record_to_delete) == 0:
        print("No records to delete")


route53.close()
