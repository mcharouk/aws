import boto3

# delete ssm command document named CloudWatchApacheInstall

ssm = boto3.client("ssm")

document_name = "CloudWatchApacheInstall"

# get document information
response = ssm.list_documents(
    Filters=[
        {"Key": "Name", "Values": [document_name]},
        {"Key": "Owner", "Values": ["Self"]},
    ]
)

# if document exists, delete it
if len(response["DocumentIdentifiers"]) > 0:
    response = ssm.delete_document(
        Name=document_name,
    )
    print("document named {0} deleted".format(document_name))
else:
    print("document named {0} does not exist".format(document_name))
