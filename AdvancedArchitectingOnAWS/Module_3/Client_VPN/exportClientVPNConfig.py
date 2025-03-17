import boto3
import utils

utils.change_current_directory()

# export client vpn client configuration
ec2 = boto3.client("ec2")

# get first vpn client id
response = ec2.describe_client_vpn_endpoints()
endpoint_id = response["ClientVpnEndpoints"][0]["ClientVpnEndpointId"]

response = ec2.export_client_vpn_client_configuration(
    ClientVpnEndpointId=endpoint_id,
)

ec2.close()

private_key_path = "certificates/client/client.key.pem"
private_cert_path = "certificates/client/client.cert.pem"
opvn_config_file_path = "client-config.ovpn"

# delete opvn config file if it exists
import os

try:
    os.remove(opvn_config_file_path)
    print("File deleted")
except:
    print("File does not exist")


def get_file_content(file_path):
    with open(file_path, "r") as f:
        return f.read()


private_key = get_file_content(private_key_path)
private_cert = get_file_content(private_cert_path)


def append_to_file(f, content, tag_name):
    f.write(b"\n")
    f.write(b"\n")
    f.write(b"<" + tag_name.encode() + b">")
    f.write(b"\n")
    f.write(content.encode())
    f.write(b"</" + tag_name.encode() + b">")


with open(opvn_config_file_path, "wb") as f:
    client_configuration_string = response["ClientConfiguration"]
    f.write(client_configuration_string.encode())

    print(f"appending private key to {opvn_config_file_path}")
    append_to_file(f, private_key, "key")
    print(f"appending certificate to {opvn_config_file_path}")
    append_to_file(f, private_cert, "cert")
