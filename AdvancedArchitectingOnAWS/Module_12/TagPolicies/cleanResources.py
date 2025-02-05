import boto3


def cleanTestResources():

    sns_topic_name = "sns-tagpolicy-demo"
    sns = boto3.client("sns")

    response = sns.list_topics()

    topics = response["Topics"]

    for topic in topics:
        if sns_topic_name in topic["TopicArn"]:
            sns_topic_arn = topic["TopicArn"]
            # if topic arn ends with the name, remove it
            if sns_topic_arn.endswith(sns_topic_name):
                print("removing topic: " + sns_topic_arn)
                sns.delete_topic(TopicArn=sns_topic_arn)
            break

    sns.close()

    bucket_name = "aws-training-marccharouk-tagpolicies"

    # if bucket exists, empty it and remove it
    s3 = boto3.resource("s3")

    if s3.Bucket(bucket_name) in s3.buckets.all():
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        bucket.delete()
        print("removing bucket: " + bucket_name)


cleanTestResources()
