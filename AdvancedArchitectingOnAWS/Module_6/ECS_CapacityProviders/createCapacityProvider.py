import boto3

asg_name = "ECSAutoScalingGroup"
capacity_provider_name = "sample-app-capacity-provider"

# delete capacity provider if it exists

client = boto3.client("ecs")
response = client.describe_capacity_providers(
    capacityProviders=[capacity_provider_name]
)

if len(response["capacityProviders"]) > 0:
    client.delete_capacity_provider(capacityProvider=capacity_provider_name)
    print("deleted capacity provider " + capacity_provider_name)
else:
    print("no capacity provider to delete")


# get arn of autoscaling group
def get_asg_arn(asg_name):
    client = boto3.client("autoscaling")
    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    return response["AutoScalingGroups"][0]["AutoScalingGroupARN"]


asg_arn = get_asg_arn(asg_name)


# create ecs capacity provider
def create_ecs_capacity_provider(asg_arn):
    client = boto3.client("ecs")
    response = client.create_capacity_provider(
        name="sample-app-capacity-provider",
        autoScalingGroupProvider={
            "autoScalingGroupArn": asg_arn,
        },
    )
    print(response)
    return response


ec2_capacity_provider = create_ecs_capacity_provider(asg_arn)


# create an ecs cluster with EC2 capacity provider and fargate capacity provider
def create_ecs_cluster(cluster_name):
    client = boto3.client("ecs")
    response = client.create_cluster(
        clusterName=cluster_name,
        capacityProviders=[
            "FARGATE",
            ec2_capacity_provider["capacityProvider"]["name"],
        ],
    )
    print(response)
    return response


cluster_name = "sample-app-cluster"
create_ecs_cluster(cluster_name)
