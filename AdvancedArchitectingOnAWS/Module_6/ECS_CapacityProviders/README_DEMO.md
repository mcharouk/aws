# ECS Capacity Provider

## Create cluster

* name

```
sample-app-cluster
```

* select fargate and ec2 instances as capacity providers
* select predefined auto scaling group
* can show autoscaling group option during demo
* creation can take up to 1 min
* check in infrastructure tab, that there is one instance registered with capacity provider

## Create ECS Task Definition

* name
```
ecs-capacity-provider-task-def
```
* Task size
  * .25 CPU or 256 Units
  * .5 GB or 512 units
* No task role (equivalent to lambda execution role)
* task execution role : ECSTaskExecutionRoleDemo
* can show task placement (but must remove fargate option as capacity provider)
* container name

```
capacity-provider-app
```

* image uri : get image URI in ECR (not repository uri)
* container port : **5000**
* Port name : leave blank
* remove cloudwatch log collection

## Create ECS Service

* use capacity provider strategy
* define a custom strategy
  * select EC2 capacity provider. Can leave base to 0 or 1
* Specify Task definition family
* Service Name

```
capacity-provider-app-service
```

* Networking
  * select ecs vpc
  * Subnets : choose private subnets so that tasks are instantiated privately
  * Sec Group : Choose ECSServiceSG : open HTTP inbound for ALB
  * Turn off public ip
* Load Balancing
  * Type : Application Load Balancer
  * Select ALB created by CF
  * Use an existing listener : **80:HTTP**
  * Use an existing target group : 