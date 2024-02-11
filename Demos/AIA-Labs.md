## Lab1

* Step 1 : region choice
  * Search bar
  * Favourites
  * Widgets
* Step 2 : Create a bucket
  * Check it's on the right region
  * Careful about the name of bucket (unique among all aws accounts)
  * Careful about major cases, underscores, etc...
* Step 3 : Create a bucket programmatically
  * to get info about default region
```
aws configure list
```
  * to set the default region
```
aws configure set default.region us-west-2
```
  * create a bucket 
```
aws s3 mb s3://fdkfsjfls
```
  * check commands, the only thing that could really mess up is the name of the bucket. Maybe missing the S3://
  * aws s3 cp /home/ssm-user/HappyFace.jpg s3://labclibucket-NUMBER
  * aws s3 ls s3://labclibucket-NUMBER



## Lab2

Déroulé : 

* VPC
  * activate DNS Hostnames
* Subnets
  * Activate Auto Assign Public IP in Public Subnet
* Public Route Table
  * Ne pas oublier d'associer ma table de routage à mon subnet
* Public Security Groups
* Public EC2 Instance
  * Network
  * Instance Role
  * User Data
* Connection à l'instance avec l'adresse ip public -> attention à ne pas se connecter en https !
* Connection en commande à l'instance avec un curl
* NAT Gateway
* Table routage privée
* Security Group pour privé : authoriser HTTP depuis le Public SG
* Create Private Instance (no user data)

Bonus : 
* Add ICMP rule in Private SG

## Lab3

* DB creation
  * Faire attention à bien au user/mdp renseigé et au nom de la base de données
  * VPC
  * SG
  * Parameter Group !!
  * Disable encryption
  * Enlever les maintenances mineures

* Target Group : faut bien mettre instances comme type, mettre le bon VPC, sinon on pourra pas voir les instances dans la liste

* ALB
  * il faut bien spécifier les subnet public et pas privés...
  * sélectionner le bon SG

* Step 3
  * Bien prendre le endpoint du writer et non du reader

* Read Replica
  * Bien sélectionner le VPC
  * Security Group

# Lab4

* Task 1 : just inspection
  * Il y a 3 sec groups : les 2 premiers, auto sur port 80, le 3e 3306 (mysql)
  * Faire attention au comportement du navigateur, c'est du http 
* Task 2 : create a template config
  * il faut bien spécifier l'AMI Linux 2 et pas 2023 sinon ca marche pas...
  * Attention au Sec Group, Instance Profile, Metadata V1 and V2
  * Ne pas inclure de subnet
* Task 3 : ASG
  * Il faut le mettre dans les private subnet (et le bon VPC)
    * Attention à la grace period (300s), sinon les health check risque de ne pas marcher
    * Il faut bien cocher la case pour collecter les métriques cloudwatch
* Task 4 : Test
* Task 5 : Test
* Task 6 : add a read replica
* Task 7 : NAT Gateway Resilience
  * Attention à la créer dans le bon public subnet
  * table de routage associée au bon VPC
  * vérifier la table de routage, et son attachment au subnet. Le subnet associée doit être le même que celui de la NAT Gateway précédemment créé...
* Task 8 : Test High Availability of database
  

# Lab 5

* Task 1 : création SNS
* Task 2 : création SQS
  * Déjà eu des problèmes avec thumbnail queue. Je sais pas pourquoi ca marche pas, mais le fait de recréer la queue l'a fait fonctionné.
* Task 3 : création notification S3
  * changement de la resource policy SNS. Attention au remplacement des placeholders
  * dans l'évenement s3
    * ingest/ (ne pas oublier le /)
    * attention au coquilles dans le suffix
    * sélection des types d'évenements
    * sélection du topic SNS
* Task 4 : création de 3 lambdas
  * attention au rôle de la lambda (LabExecutionRole)
  * runtime Python 3.9
  * trigger SQS : taille de batch de 1 mais je ne pense pas que ca a un impact négatif sur le bon fonctionnement
  * attention à changer le nom du handler
* Task 5 : upload d'un fichier et test  
* Task 6 : Validation du test

* Optionnel
  * lifecycle policy
    *  regarder les subtilités dans le lab surtout les options à cocher
  * SNS email

# Lab 6

* Task 1 : de l'inspection principalement
* Task 2 : Création d'un bucket S3.
  *  Veiller à ce que le bucket soit créer dans la bonne région (Primary Region)
  *  Pas très grave si dans la région secondaire. Ces primaires et secondaires servent à la question bonus
* Task 3 : Configuration du bucket S3 (accès public)
  * consiste à décocher block public access
  * créer une bucket policy (attention au ARN spécifié). Bien mettre /* à la fin du ARN
* Task 4 : uploader un fichier et tester qu'on y accède en public
* Task 5 : 
  * Création d'une origine (OAI) dans CloudFront
    * Origin Path doit être vide
    * OAI : attention à ne pas créer un OAC
  * Création d'un comportement (behavior)
    * LE chemin doit être cohérent avec le folder créé dans le bucket
    * Séléctionner la bonne origine
    * Vérifier Cache Key and origin resquests caractéristiques 
      * Cache policy and origin request policy (recommended)
      * Cache Policy = CachingOptimized
    * dans Security/Origin Access (dans le menu à droite)
* Task 6 : changer la bucket policy avec le canonical user de cloudfront
* Task 7 : bonus, mettre en place une réplication CRR
  * créer un nouveau bucket dans la région secondaire. Vérifier que le versioning est bien activé dessus
  * bien s'assurer que Block Public Access est désactivé
  * faire attention à l'édition de la bucket policy -> ARN + /*. C'est le bucket de destination qui doit être modifié pour pouvoir tester la réplication lorsqu'elle se fera.
  * Faire Create New Role au lieu de sélectionner un rôle existant