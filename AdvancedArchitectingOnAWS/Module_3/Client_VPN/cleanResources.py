import boto3
import utils

utils.change_current_directory()

domain_name = "server"

client_vpn_endpoint_name = "ClientVPNDemo"


ec2 = boto3.client("ec2")

response = ec2.describe_client_vpn_endpoints(
    Filters=[{"Name": "tag:Name", "Values": [client_vpn_endpoint_name]}]
)

if len(response["ClientVpnEndpoints"]) > 0:
    client_vpn_endpoint_id = response["ClientVpnEndpoints"][0]["ClientVpnEndpointId"]

    response = ec2.describe_client_vpn_target_networks(
        ClientVpnEndpointId=client_vpn_endpoint_id
    )
    # disassociate client vpn from subnet

    ec2.disassociate_client_vpn_target_network(
        ClientVpnEndpointId=client_vpn_endpoint_id,
        AssociationId=response["ClientVpnTargetNetworks"][0]["AssociationId"],
    )

    print(f"Disassociating target network from client vpn {client_vpn_endpoint_id}")

    # delete client vpn
    ec2.delete_client_vpn_endpoint(ClientVpnEndpointId=client_vpn_endpoint_id)

    print(f"client vpn {client_vpn_endpoint_id} deleted")
else:
    print("client vpn does not exist")

# delete imported certificate which has domain domain_name
# should return certificates that has key types RSA_2048 and RSA_4096
acm = boto3.client("acm")
certificates = acm.list_certificates(Includes={"keyTypes": ["RSA_2048", "RSA_4096"]})[
    "CertificateSummaryList"
]

for certificate in certificates:
    if certificate["DomainName"] == domain_name:
        certificate_arn = certificate["CertificateArn"]
        acm.delete_certificate(CertificateArn=certificate_arn)
        print("Certificate deleted")
        break

acm.close()

opvn_config_file_path = "client-config.ovpn"

# delete opvn config file if it exists
import os

try:
    os.remove(opvn_config_file_path)
    print("ovpn file deleted")
except:
    print("ovpn file does not exist")

# remove folder certificates folder if it exists
import shutil

try:
    shutil.rmtree("certificates")
    print("Certificates folder deleted")
except:
    print("Certificates folder does not exist")
