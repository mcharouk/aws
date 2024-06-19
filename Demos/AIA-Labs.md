# Lab1

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



# Lab2

* **Normalement, les ACLs doivent être ok, rien a changé**

* Si probléme avec les ip publiques non assignées ou DNS, changer les params du subnet et du vpc et recréer une nouvelle instance publique au lieu de stop/start

Déroulé : 

* Task 1 : VPC creation
  * activate DNS Hostnames
* Task 2 : Create Private and Public Subnets
  * Activate Auto Assign Public IP in Public Subnet
* Task 3 : Create An IGW 
  * Check it's associated to the VPC
* Task 4 : **Public** Subnet Route Table 
  * Ne pas oublier d'associer ma table de routage à mon subnet
  * Vérifier que la table de routage est ok
* Task 5 : **Public** Security Groups
  * HTTP to any ip
  * Il faut que sur l'outbound tout soit ouvert
* Task 6 : **Public** EC2 Instance
  * AMI Linux 2023
  * Network (bon VPC, subnet, security group)
  * Instance Role
  * User Data
* Task 7 : Connection à l'instance avec l'adresse ip public 
  * attention à ne pas se connecter en https, ne pas mettre de port dans l'adresse !
* Task 8 : Connection en commande à l'instance avec un curl
* Task 9 : NAT Gateway
  * Config Table routage privée
* Task 10 : Security group privé
  * authoriser HTTP depuis le Public SG  
* Task 11 : Lancement d'une instance privée (pas de user data).
* Task 12 : Connection à l'instance dans le sous réseau privé
  * On ne pourra pas s'y connecter si il y a un pb avec la NAT Gateway (à cause de session manager)

Bonus : 
* Add ICMP rule in Private SG
* for metadata, check that request is done from **public** instance because public hostname is only available from public instance obviously

# Lab3

* Task 1 : DB creation
  * Faire attention à bien renseigner user/mdp et au nom de la base de données (dans le Aurora mysql)
  * VPC
  * SG
  * **Parameter Group** -> cela entrainera des erreurs lors de la création des read replica si pas bien renseigné
  * Disable encryption
  * Enlever les maintenances mineures
* Task 2 : Création d'un ALB (il y a un ALB mais pas d'ASG)
  * Target Group
    * mettre instances comme type
    * mettre le bon VPC, sinon on pourra pas voir les instances dans la liste à sélectionner
    * bien sélectionner les instances et cliquer sur le bouton **Include As Pending Below**
  * ALB
    * il faut bien spécifier les subnet public et pas privés... Les mettre dans le privé le rendra inaccessible depuis internet
    * sélectionner le bon SG
* Task 3
  * Bien prendre le endpoint du writer et non du reader
* Task 4 : Test connectivité
* Tache facultative : Read Replica
  * Bien sélectionner le VPC
  * Security Group
  * Failure si ParameterGroup pas bon

# Lab4

* Task 1 : just inspection
  * Il y a 3 sec groups : les 2 premiers, auto sur port 80, le 3e 3306 (mysql)
  * **Faire attention au comportement du navigateur**, c'est du http 
* Task 2 : create a launch template config
  * Il ne faut rien mettre dans le réseau (VPC/Subnet), ce sera spécifié dans l'ASG, mais il faut renseigner le Security Group par contre...
  * Points d'attention
    * Security Group -> fait planter au moment du register instance auprès de l'ALB si pas renseigné
    * Instance Profile -> le rôle associé à juste des droits Session Manager, ca ne devrait pas être trop grave si c'est mal configuré
    * Metadata par défaut (V2 only)
* Task 3 : ASG
  * Il faut le mettre dans les private subnet (et le bon VPC) -> pas d'impact si dans les public subnet, ca marche qd même
    * Attention à la grace period (300s), sinon les health check risque de ne pas marcher. Normalement c'est la conf par défaut
    * Il faut bien cocher la case pour collecter les métriques cloudwatch. **Pas d'effet néfaste sur l'application**
    * Attacher au target group existant
    * Les ELB health check ne sont pas activés
* Task 4 : Test
* Task 5 : Test
* Task 6 : Add a read replica
  * attention à bien sélectionner 1 availability zone différente de la 1ere (mais pas d'impact sur le bon fonctionnement de l'application)
* Task 7 : NAT Gateway Resilience
  * Attention à la créer dans le bon public subnet (Le No 2)
  * table de routage associée au bon VPC
  * vérifier la table de routage, et son attachment au subnet. Le subnet associée doit être le même que celui de la NAT Gateway précédemment créé...
  * Qd on regarde les tables de routage, on dirait que les deux sont associés au Private Subnet 2. Il faut bien aller dans les propriétés du subnet pour voir à quelle table de routage il est effectivement associé. On ne peut pas explicitement supprimer l'association qu'il y a entre la table de routage privé 1 et le private subnet 2, faute de droits suffisants.
* Task 8 : Test High Availability of database
  

# Lab 5

* Task 1 : création SNS
* Task 2 : création SQS
  * Déjà eu des problèmes avec thumbnail queue. Je sais pas pourquoi ca marche pas, mais le fait de recréer la queue l'a fait fonctionné.
  * Faire un subscribe SNS à partir de SQS et non à partir de SNS, ca marche mieux, mais je ne sais pas pourquoi.
* Task 3 : création notification S3
  * changement de l'access policy SNS pour autoriser S3 à publier dans la queue. !!! Attention au remplacement des placeholders !!! sinon on ne peut pas créer le trigger s3
  * dans l'évenement s3
    * ingest/ (ne pas oublier le /)
    * attention au coquilles dans le suffix
    * sélection des types d'évenements
    * sélection du topic SNS
* Task 4 : création de 3 lambdas
  * attention au rôle de la lambda (LabExecutionRole)
  * runtime Python 3.9. **Fails if python > 3.9**
  * trigger SQS : taille de batch de 1 mais je ne pense pas que ca a un impact négatif sur le bon fonctionnement
  * attention à changer le nom du handler
* Task 5 : upload d'un fichier et test  
* Task 6 : Validation du test
  * ingest files are still there and it's normal
  * new folders are created
* To debug
  * Use cloudwatch metrics to see who does not receive the message
  * Change default statistic which is Average by SUM to have accurate numbers
  * SNS
    * NumberOfMessagesPublished
    * NumberOfMessagesDelivered
  * SQS
    * NumberOfMessagesSent
    * NumberOfMessagesReceived

* Optionel
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
* Task 5
  * changer la bucket policy pour l'OAC
    * Bien remplacer les placeholder
      * ARN de la distribution cloudfront
      * dans Resource, ARN du bucket S3 avec /*  à la fin.
  * Création d'une origine (OAC) dans CloudFront
    * Origin Path doit être vide
    * Paramètres par défaut de l'OAC normalement
  * Création d'un comportement (behavior)
    * Le chemin doit être cohérent avec le folder créé dans le bucket (on créé un folder CachedObjects normalement)
    * Le chemin doit ressembler à **CachedObjects/*.png**
    * Séléctionner la bonne origine
    * Vérifier Cache Key and origin resquests caractéristiques 
      * Cache policy and origin request policy (recommended)
* Task 6 : bonus, mettre en place une réplication CRR
  * activer dans le bucket primaire le versioning
  * créer un nouveau bucket dans la région secondaire. Vérifier que le versioning est bien activé dessus
  * bien s'assurer que Block Public Access est désactivé (pour pouvoir tester que l'objet est accessible, et pour ne pas avoir d'erreur lorsqu'on crée la bucket policy)
  * faire attention à l'édition de la bucket policy -> ARN + /*. C'est le bucket de destination qui doit être modifié pour pouvoir tester la réplication lorsqu'elle se fera.
  * Créer la règle de réplication dans le bucket source
  * Faire Create New Role au lieu de sélectionner un rôle existant