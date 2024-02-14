# delete all ecs services

import boto3

client = boto3.client("ecs")


# delete all ecs clusters
response = client.list_clusters()
for cluster in response["clusterArns"]:
    response = client.list_services(cluster=cluster)
    for service in response["serviceArns"]:
        print("deleting " + service)
        client.delete_service(cluster=cluster, service=service, force=True)
    print("deleting " + cluster)
    client.delete_cluster(cluster=cluster)


# delete all ecs task definitions
response = client.list_task_definitions()
for task in response["taskDefinitionArns"]:
    print("deleting " + task)
    client.deregister_task_definition(taskDefinition=task)


# delete all ecr repositories

import boto3

client = boto3.client("ecr")

response = client.describe_repositories()

for repo in response["repositories"]:
    print("deleting " + repo["repositoryName"] + " repository")
    client.delete_repository(repositoryName=repo["repositoryName"], force=True)
