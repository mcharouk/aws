import boto3

# deploy cloudformation stack in sandbox_template_v4.yml
# parameter S3ResourceBucket value is demo-marccharouk-labtemplate-123456-code

cf = boto3.client("cloudformation")

cf.create_stack(
    StackName="demo-marccharouk-labtemplate-123456",
    TemplateURL="https://demo-marccharouk-labtemplate-123456-code.s3.eu-west-3.amazonaws.com/sandbox_template_v4.yml",
    Parameters=[
        {
            "ParameterKey": "S3ResourceBucket",
            "ParameterValue": "demo-marccharouk-labtemplate-123456-code",
        },
        {
            "ParameterKey": "DeployCloud9",
            "ParameterValue": "false",
        },
    ],
    Capabilities=["CAPABILITY_NAMED_IAM"],
)
