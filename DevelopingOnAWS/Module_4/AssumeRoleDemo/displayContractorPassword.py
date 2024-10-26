import boto3

# get secret called contractor_password and print it in console

client = boto3.client("secretsmanager")

response = client.get_secret_value(SecretId="contractor_password")
secret_string = response["SecretString"]
print(f"contractor password is [{secret_string}]")
