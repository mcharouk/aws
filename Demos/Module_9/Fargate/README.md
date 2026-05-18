# Pre-requisities

* ! start **rancher desktop** !

# ECR

* create ECR Repository with name **sample-app**
* service runs on port 5000
* name the service **sample-app**

command to push to ECR
```
uploadToECR.bat sample-app
```

# ECS

## Cluster

* Create an ECS cluster
  * Name : sample-app-ecs-cluster 
  * Fargate Only

## Task definition

* Create a task definition
  * Name : sample-app-task-def
  * Task Role : ecsTaskExecutionRole
  * Network mode : awsvpc
  * Container name : sample-app-container
  * Image : Copy/Paste image URL from ECR
  * Port mapping : 5000 (for container port and port name)

## Service definition

* Service name : sample-app-service
* Compute options
  * Launch Type : Fargate
  * Security Group : CdkFargateStack...


## Test

* Wait until a public ip has been provided
* URL : http://[PublicIP]:5000