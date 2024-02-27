# delete all ecs services

import boto3

ecs = boto3.client("ecs")


# delete all ecs clusters
response = ecs.list_clusters()
if len(response["clusterArns"]) == 0:
    print("no clusters to delete")


for cluster in response["clusterArns"]:
    response = ecs.list_services(cluster=cluster)
    for service in response["serviceArns"]:
        print("deleting " + service)
        ecs.delete_service(cluster=cluster, service=service, force=True)
    print("deleting " + cluster)
    ecs.delete_cluster(cluster=cluster)


# delete all ecs task definitions
response = ecs.list_task_definitions()

if len(response["taskDefinitionArns"]) == 0:
    print("no task definitions to delete")

for task in response["taskDefinitionArns"]:
    print("deleting " + task)
    ecs.deregister_task_definition(taskDefinition=task)


# delete all ecr repositories

ecr = boto3.client("ecr")

response = ecr.describe_repositories()

if len(response["repositories"]) == 0:
    print("no repositories to delete")

for repo in response["repositories"]:
    print("deleting " + repo["repositoryName"] + " repository")
    ecr.delete_repository(repositoryName=repo["repositoryName"], force=True)
