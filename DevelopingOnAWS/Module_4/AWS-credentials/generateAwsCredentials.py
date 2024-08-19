import boto3

# get outputs of cloudformation stack named AwsCredentialsStack
cloudformation = boto3.client("cloudformation")

response = cloudformation.describe_stacks(StackName="AwsCredentialsStack")
outputs = response["Stacks"][0]["Outputs"]

dynamoDbAdminRole = ""
sqsAdminAccessKeyId = ""
sqsAdminSecretAccessKey = ""
snsAdminAccessKeyId = ""
snsAdminSecretAccessKey = ""

for output in outputs:
    if output["OutputKey"] == "DynamoDBRoleARN":
        dynamoDbAdminRole = output["OutputValue"]
        continue

    if output["OutputKey"] == "sqsAdminAccessKeyId":
        sqsAdminAccessKeyId = output["OutputValue"]
        continue

    if output["OutputKey"] == "snsAdminAccessKeyId":
        snsAdminAccessKeyId = output["OutputValue"]
        continue

# get secret value from secret manager
secretsmanager = boto3.client("secretsmanager")

sqsAdminSecretAccessKey = secretsmanager.get_secret_value(
    SecretId="SqsAdmin-SecretAccessKey"
)["SecretString"]

snsAdminSecretAccessKey = secretsmanager.get_secret_value(
    SecretId="SnsAdmin-SecretAccessKey"
)["SecretString"]

# get file from templates.aws-config.txt and replace placeholder that starts with $

with open("templates/aws-config.txt", "r") as file:
    content = file.read()
    content = content.replace("$dynamoDbAdminRole", dynamoDbAdminRole)
    # write results to aws-config-result.txt
    with open("aws-config-result.txt", "w") as result_file:
        result_file.write(content)

with open("templates/aws-credentials.txt", "r") as file:
    content = file.read()
    content = content.replace("$sqsAdminAccessKeyId", sqsAdminAccessKeyId)
    content = content.replace("$sqsAdminSecretAccessKey", sqsAdminSecretAccessKey)
    content = content.replace("$snsAdminAccessKeyId", snsAdminAccessKeyId)
    content = content.replace("$snsAdminSecretAccessKey", snsAdminSecretAccessKey)
    with open("aws-credentials-result.txt", "w") as result_file:
        result_file.write(content)
