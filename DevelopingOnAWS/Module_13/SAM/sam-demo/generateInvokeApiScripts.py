import boto3
import utils

utils.change_current_directory()
# get cloudformation output named ApiUrl of stack SAMDemoStack


def get_api_url(stack_name, output_name):
    """
    Get the ApiUrl of a CloudFormation stack.
    """
    cloudformation = boto3.client("cloudformation")
    response = cloudformation.describe_stacks(StackName=stack_name)
    outputs = response["Stacks"][0]["Outputs"]
    api_url = ""
    for output in outputs:
        if output["OutputKey"] == output_name:
            output_value = output["OutputValue"]
            print(f"stack name : {stack_name}, API URL: {output_value}")
    return output_value


def replace_placeholder(template_file, output_file, placeholder, api_url):
    with open(template_file, "r") as f:
        content = f.read()
        content = content.replace(placeholder, api_url)
        with open(output_file, "w") as f:
            f.write(content)
            print(f"File {output_file} generated")


placeholder = "##INVOKE_URL##"

stack_name = "SAMDemoStack"
output_name = "ApiUrl"
api_url = get_api_url(stack_name, output_name)

template_file = "templates/invokeDevAPI.ps1"
output_file = "invokeDevAPI.ps1"
replace_placeholder(template_file, output_file, placeholder, api_url)


stack_name = "SAMDemoStackProd"
output_name = "ApiUrl"
api_url = get_api_url(stack_name, output_name)

template_file = "templates/invokeProdAPI.ps1"
output_file = "invokeProdAPI.ps1"
replace_placeholder(template_file, output_file, placeholder, api_url)
