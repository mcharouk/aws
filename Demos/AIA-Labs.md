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
  