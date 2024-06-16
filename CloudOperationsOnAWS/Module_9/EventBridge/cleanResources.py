import boto3
from event_bridge.StackConfig import StackConfig

stackConfig = StackConfig()
cloudTrailBucketName = stackConfig.s3_cloudTrailBucketName

# empty S3 CloudTrail bucket in us-east-1
s3 = boto3.resource("s3", region_name="us-east-1")
bucket = s3.Bucket(cloudTrailBucketName)
bucket.objects.all().delete()
print(f"Bucket {cloudTrailBucketName} emptied successfully")

# delete all event bridge rules in eu-west-3
events = boto3.client("events", region_name="eu-west-3")

response = events.list_rules()
rules = response["Rules"]

for rule in rules:
    # delete all rules targets
    targets = events.list_targets_by_rule(Rule=rule["Name"])["Targets"]
    for target in targets:
        events.remove_targets(Rule=rule["Name"], Ids=[target["Id"]])
        print(f"Target {target['Id']} removed from rule {rule['Name']}")

    ruleName = rule["Name"]
    print(f"Deleting rule {ruleName}...")
    events.delete_rule(Name=ruleName)
    print(f"Rule {ruleName} deleted successfully")
