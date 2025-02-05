import os

import boto3
import utils

stack_name = "CloudFrontDistributionStack"
output_name = "DistributionDomainName"
template_folder = "demo_template_scripts"
placeholder_key = "{{cloudfront_url}}"
output_folder = "demo"

utils.change_current_directory()

# get output value of stack
cloudformation = boto3.client("cloudformation")

response = cloudformation.describe_stacks(StackName=stack_name)

outputs = response["Stacks"][0]["Outputs"]
domain_name = None
for output in outputs:
    if output["OutputKey"] == output_name:
        domain_name = output["OutputValue"]
        break
print(f"Domain name is {domain_name}")

# for all files in template_folder, replace placeholder_key with domain name
# generate new file in output folder
# if output file in output folder already exists, overwrite it
for file in os.listdir(template_folder):
    with open(f"{template_folder}/{file}", "r") as f:
        content = f.read()
        content = content.replace(placeholder_key, domain_name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        with open(f"{output_folder}/{file}", "w") as f:
            print(f"Writing file {output_folder}/{file}")
            f.write(content)

test_files_folder = "test_files"
# in output folder create a test_files_folder folder
if not os.path.exists(f"{output_folder}/{test_files_folder}"):
    print(f"Creating folder {output_folder}/{test_files_folder}")
    os.makedirs(f"{output_folder}/{test_files_folder}")
