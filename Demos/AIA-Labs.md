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
