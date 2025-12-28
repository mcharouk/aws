import os
# save environment variable AWS_PROFILE in a variable
# set environment variable AWS_PROFILE to null
# restore environment variable AWS_PROFILE to its original value
aws_profile = os.environ.get('AWS_PROFILE')
os.environ.pop("AWS_PROFILE", None)

import boto3

sso_admin = boto3.client('sso-admin')
id_store = boto3.client('identitystore')

instances = sso_admin.list_instances()
if not instances['Instances']:
    print("No IAM Identity Center instances found.")
    exit(1)

identity_store_id = instances['Instances'][0]['IdentityStoreId']
instance_arn = instances['Instances'][0]['InstanceArn']

print(f"Using Identity Store ID: {identity_store_id}\n")

def get_iam_identity_center_users():
    # 3. Use a paginator to handle large numbers of users
    paginator = id_store.get_paginator('list_users')
    
    user_list = []

    for page in paginator.paginate(IdentityStoreId=identity_store_id):
        for user in page['Users']:
            user_info = {
                'UserName': user.get('UserName'),
                'UserId': user.get('UserId'), # This is the ID you want
                'DisplayName': user.get('DisplayName')
            }
            user_list.append(user_info)

    return user_list

# Execute
users = get_iam_identity_center_users()

for u in users:
    print(f"ID: {u['UserId']} | Name: {u['UserName']}")

q_business_application_name = "QBusiness-demo-application"
# get iam identity center aws managed application arn from name

response = sso_admin.list_applications(
    InstanceArn=instance_arn
)

for app in response['Applications']:
    if app['Name'] == q_business_application_name:
        q_business_application_arn = app['ApplicationArn']
        break

if q_business_application_arn is None:
    print("No application found with name: " + q_business_application_name)
    exit(1)

# assign all users to the application it not already assigned
for u in users:
    application_assignments = sso_admin.list_application_assignments_for_principal(
        InstanceArn=instance_arn,
        PrincipalId=u['UserId'],
        PrincipalType='USER'
    )
    # check if user is already assigned to the application
    is_user_assigned = False

    for assignment in application_assignments['ApplicationAssignments']:
        if assignment['ApplicationArn'] == q_business_application_arn:
            is_user_assigned = True
            print(f"User {u['UserName']} already assigned to application {q_business_application_name}")
            break
    

    if is_user_assigned == False:
        print(f"Assigning user {u['UserName']} to application {q_business_application_name}")
        sso_admin.create_application_assignment(            
            ApplicationArn=q_business_application_arn,
            PrincipalId=u['UserId'],
            PrincipalType='USER'
        )




sso_admin.close
id_store.close

os.environ['AWS_PROFILE'] = aws_profile
