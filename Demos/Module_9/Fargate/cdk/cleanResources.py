# delete all ecs services

import time

import boto3

ecs = boto3.client("ecs")


# delete all ecs clusters
response = ecs.list_clusters()
if len(response["clusterArns"]) == 0:
    print("no clusters to delete")


for cluster in response["clusterArns"]:
    response = ecs.list_services(cluster=cluster)
    for service in response["serviceArns"]:
        print("setting desired count to 0 " + service)
        ecs.update_service(cluster=cluster, service=service, desiredCount=0)

        nb_running_tasks = 1
        while nb_running_tasks > 0:
            tasks = ecs.list_tasks(
                cluster=cluster, serviceName=service, desiredStatus="RUNNING"
            )
            nb_current_tasks = len(tasks["taskArns"])
            print("service {0} has {1} running tasks".format(service, nb_current_tasks))
            nb_running_tasks = nb_current_tasks
            time.sleep(3)

        print("deleting " + service)
        ecs.delete_service(cluster=cluster, service=service)
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
