# Lab 1 : Exploration de IAM

## Description

* 3 users
  * S3 readonly
  * EC2 readonly
  * EC2 View/Start/Stop
* Principal tasks
  * Assign policies to group
  * Assign users to group
  * Connect on Console with different users and see policies effect. Use InPrivate browsing whgen connect on Console

## Troubleshooting

* Task 1 : add users to respective groups
* Task 2 : Ouvrir le navigateur en private
* Se connecter en tant que différents users pour executer des actions soit liés à leur rôle, soit autre afin de valider qu'ils n'ont pas accès.

user-1 -> accès à S3 (uniquement le bucket avec le nom s3bucket dedans)
user-2 -> accès à EC2 read only. Pas le droit de stopper des EC2 par exemple
user-3 -> EC2 admin. Droit de start et stopper des EC2 mais aucun droit sur S3

# Lab 2 : Exploration d'un VPC et création d'une instance EC2

## Description

Objective of this lab : Create an EC2 instance, and expose it on the public internet

* Create a VPC will all the necessary components from IGW to SG
* Create EC2 instance

## Troubleshooting

* Dans ce lab, il faut créer 
  * un VPC
  * 2 subnets public
  * une IGW
  * une table de routage
  * un sec group
  * une instance EC2
* Tout est assez basique, la seule chose notable c'est qu'il faut passer par le nouveau wizard pour créer le VPC, ce qui facilite les choses.
* J'ai pas eu besoin de changer la table de routage, elle était déjà bien configurée.
* Ensuite, il faut créer le sec group. Attention à le mettre dans le bon VPC
* Ensuite l'instance -> pas de rôle IAM à donner.

# Lab 3 : S3 + DynamoDB

## Description

Configure S3 and DynamoDB so that the prebuilt web application can access them

* S3
  * Create bucket policy to allow a webapp role to get objects from S3
  * Upload files in S3 buckets (employee photos)
* DynamoDB
  * Create a table 
  * Add items through DynamoDB or through webapp (employee list)


## Troubleshooting

* Task 1 : Create an S3 bucket. Block public access default kept (activated)
* Task 2 : Autorisation à un rôle spécifique de lire les objets du bucket
  * Il faut mettre le bon rôle, et bien spécifier les resources (le bucket et le prefix)
* Task 3 : upload files in S3 bucket. Upload png in root folder
* Task 4 : Create DynamoDB. PartitionKey as String
* Task 6 : Add an employee in DynamoDB through the webapp
* Task 7 : Add an employee in DynamoDB through DynamoDB console


# Lab 4 : Haute disponibilité

## Description

* Main objective : Put an EC2 in an autoscaling group behind a Load Balancer (same webapp than Lab 2 & 3)

* Create ALB and its target group
* Create a launch template
* Create an autoscaling group
  * Set with Target Tracking scaling policy. 
  * Activate ASG notifications 
* Simulate load on webapp to trigger a scale out event

## Troubleshooting


* reference in the lab the availability zone mentioned in the web app, in configuration -> availability zone
* task 2 : create an ALB
  * create a new Sec Group, don't use already existing sec groups !!
  * create a new target group (instance mode)
    * health checks default settings have to be modified. Maybe it will fail if not. In order 2,5,20,30
* task 3 : create a launch template
  * select the box guidance for ASG
  * select AMI Linux 2023, x64
  * don't fill subnets or VPC, only SG
  * fill instance role
  * metadata : v1 & v2 !!! 
  * user data : replace with right placeholder
* task 4 : create an ASG
  * note that updating ASG is not possible (IAM error), deleting it also is not possible
  * fill VPC and all subnets
  * !! Put max instance to 4 and not 2 or it will not autoscale... 
  * turn On ELB health checks
  * Target tracking policy (30% CPU)
  * create an SNS topic for notification with own email address (must confirm subscription manually)
  * terminate the old instance (that was here from the beginning of the lab)
* task 5
  * stress the application. Normally an email should have been recevied when the ASG scales
