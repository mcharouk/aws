import boto3


region = "eu-west-1"

cloudformation = boto3.client('cloudformation', region_name=region)
qbusiness = boto3.client('qbusiness', region_name=region)

stack_name = "QBusinessDemoStack"
applicationIdOutputName = "QBusinessApplicationId"
indexIdOutputName = "QBusinessIndexId"
dataSourceIdOutputName = "QBusinessS3DatasourceId"

#get cloud formation outputs
response = cloudformation.describe_stacks(StackName=stack_name)

applicationId = None
indexId = None
dataSourceId = None
outputs = response['Stacks'][0]['Outputs']

for output in outputs:
    if output['OutputKey'] == applicationIdOutputName:
        applicationId = output['OutputValue']
    elif output['OutputKey'] == indexIdOutputName:
        indexId = output['OutputValue']
    elif output['OutputKey'] == dataSourceIdOutputName:
        dataSourceId = output['OutputValue']
# throw error if one of these outputs are null

if applicationId is None or indexId is None or dataSourceId is None:
    raise Exception("One of the outputs is null")

print("Syncing data source: " + dataSourceId)
response = qbusiness.start_data_source_sync_job(
            applicationId=applicationId,
            indexId=indexId,
            dataSourceId=dataSourceId
        )

# wait until sync job is finished
response = qbusiness.get_data_source_sync_job(
    applicationId=applicationId,
    jobId=response['jobId']
)

cloudformation.close
qbusiness.close
