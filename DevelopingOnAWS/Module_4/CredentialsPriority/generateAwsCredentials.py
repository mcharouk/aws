import boto3

# get outputs of cloudformation stack named CredentialsPriority
cloudformation = boto3.client("cloudformation")

response = cloudformation.describe_stacks(StackName="CredentialsPriority")
outputs = response["Stacks"][0]["Outputs"]

johnFooAccessKeyId = ""
s3AdminRoleArn = ""
johnFooSecretAccessKey = ""

for output in outputs:
    if output["OutputKey"] == "JohnFooAccessKeyId":
        johnFooAccessKeyId = output["OutputValue"]
        continue

    if output["OutputKey"] == "S3AdminRoleArn":
        s3AdminRoleArn = output["OutputValue"]
        continue


# get secret value from secret manager
secretsmanager = boto3.client("secretsmanager")

johnFooSecretAccessKey = secretsmanager.get_secret_value(
    SecretId="JohnFoo-SecretAccessKey"
)["SecretString"]

# get file from templates.aws-config.txt and replace placeholder that starts with $

with open("templates/config.json", "r") as file:
    content = file.read()
    content = content.replace("$johnFooAccessKeyId", johnFooAccessKeyId)
    content = content.replace("$johnFooSecretAccessKey", johnFooSecretAccessKey)
    content = content.replace("$s3AdminRoleArn", s3AdminRoleArn)
    # write results to aws-config-result.txt
    with open("config.json", "w") as result_file:
        result_file.write(content)
