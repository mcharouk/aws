# delete all ecs services

import time

import boto3

ecs = boto3.client("ecs")

cluster_name = "sample-app-cluster"

# get cluster arn if it exists
response = ecs.describe_clusters(clusters=[cluster_name])

if len(response["clusters"]) == 0:
    print("no cluster to delete")
else:
    cluster_arn = response["clusters"][0]["clusterArn"]
    response = ecs.list_services(cluster=cluster_arn)
    for service in response["serviceArns"]:
        print("setting desired count to 0 " + service)
        ecs.update_service(cluster=cluster_arn, service=service, desiredCount=0)

        nb_running_tasks = 1
        while nb_running_tasks > 0:
            tasks = ecs.list_tasks(
                cluster=cluster_arn, serviceName=service, desiredStatus="RUNNING"
            )
            nb_current_tasks = len(tasks["taskArns"])
            print("service {0} has {1} running tasks".format(service, nb_current_tasks))
            nb_running_tasks = nb_current_tasks
            time.sleep(3)

        print("deleting " + service)
        ecs.delete_service(cluster=cluster_arn, service=service)

    auto_scaling_group = "ECSAutoScalingGroup"

    # update auto scaling group desired size to 0
    asg = boto3.client("autoscaling")
    asg.update_auto_scaling_group(
        AutoScalingGroupName=auto_scaling_group, DesiredCapacity=0, MinSize=0
    )
    # wait for all instances to be terminated
    nb_instances = 1
    while nb_instances > 0:
        instances = asg.describe_auto_scaling_groups(
            AutoScalingGroupNames=[auto_scaling_group]
        )["AutoScalingGroups"][0]["Instances"]
        nb_current_instances = len(instances)
        print(
            "auto scaling group {0} has {1} instances".format(
                auto_scaling_group, nb_current_instances
            )
        )
        nb_instances = nb_current_instances
        time.sleep(3)

    print("deleting cluster " + cluster_name)
    ecs.delete_cluster(cluster=cluster_arn)


# delete all ecs task definitions
response = ecs.list_task_definitions()

if len(response["taskDefinitionArns"]) == 0:
    print("no task definitions to delete")

for taskDef in response["taskDefinitionArns"]:
    print("deregistering task definition " + taskDef)
    ecs.deregister_task_definition(taskDefinition=taskDef)


if len(response["taskDefinitionArns"]) > 0:
    print("deleting all task definitions")
    ecs.delete_task_definitions(taskDefinitions=response["taskDefinitionArns"])


# delete all namespaces
serviceDiscovery = boto3.client("servicediscovery")
namespaces = serviceDiscovery.list_namespaces()

if len(namespaces["Namespaces"]) == 0:
    print("no namespaces to delete")


for namespace in namespaces["Namespaces"]:
    print("deleting namespace " + namespace["Name"])
    serviceDiscovery.delete_namespace(Id=namespace["Id"])

ecs.close()
# delete all ecr repositories

ecr = boto3.client("ecr")

repository_name = "capacity-provider-app"

# delete all images of repository
response = ecr.list_images(repositoryName=repository_name)

if len(response["imageIds"]) == 0:
    print("no images to delete")

for image in response["imageIds"]:
    print("deleting image " + image["imageDigest"])
    ecr.batch_delete_image(repositoryName=repository_name, imageIds=[image])
    print("deleted image " + image["imageDigest"])

ecr.close()
