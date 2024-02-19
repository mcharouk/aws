* De manière générale, solliciter les sachants à partager leurs bonnes pratiques sur les sujets qu'ils maitrisent

# Module 1 : Infrastructure

* Sondage : 
What do you consider personally being the best driver to move to the cloud ?
  * Cost
  * Time To Market
  * Innovation
  * No infra maintenance
  * Security
  * Easy and (near) unlimited scaling

* Analogies : Edge Location / Local Zone
* Quizz :  Local Zone / Edge Locations

* Jeu sur le Well Architected Framework
* Demo : Montrer le Well architected Tool

# Module 2 : IAM

Reminder : pas trop

* Analogie
  * AssumeRole / Policier -> ne pas en parler car le timing est juste sur ce module...
  * Permission Boundary / policies : Constitution / Loi
  * Boite de nuit pour expliquer les resources based / identity based -> pas le temps
* Quizz avant d'aborder les policies : pas le temps
* Dashboard sur l'intérêt des multi account : essayer de pas trop prendre de temps

## Policies

* Console : montrer les policy avec la console (comment les éditer, différents types d'identity based policies)

* Analogie au moment d'expliquer l'explicit deny :  Accès à une boite de nuit
  * Identity based policy = on possède une entrée
  * Resource Based policy = on a une autorisation d'un dirigeant de la boite de nuit
  * Explicit Deny : c'est comme si le videur avait une black list. Quelque soit les autorisations que l'on peut donner, tu ne peux pas rentrer tant que tu es sur la blacklist.

## Permission Boundary

* Check for experience : 
  * Au moment des permission boundary, poser la question quel est le challenge que pose least privilege principle ?

* Analogies : Permission Boundary : Constitution & loi
Démo

## Multi Account

* Quels sont les problèmes d'avoir peu de comptes ? 
  * Analogies : Syndic
  * Arguments : 
    * Plus facile de mettre des restrictions spécifiques en fonction de l'environnement,
des applications, ou de la réglementation.
    * Si un compte doit être HIPAA compliant, pas la peine d'imposer ses contraintes à tout le monde.
    * Si l'organisation des personnes, des rôles et des responsabilités différe d'un env à un autre, plus facile de séggreger. Chacun à son pré, et on ne prend pas le risque que les administrateurs se marchent dessus.
    * Plus facile de gérer les coûts car ils sont liés directement à un compte.
    * Service Quotas
    * Blast Radius

* Pourquoi AWS Organization ?
  * Quels sont les challenges posés par le fait d'avoir plusieurs comptes ?
  

# Module 3 : Networking 1

Analogies : 
* Security Group / ACLs : Avion / Cinéma
* Masque Sous réseau / Host : Classe / élèves
* Table de routage : panneau d'indication

Rappel sur la haute disponibilité, et sur le concept de région

Poll questions :
* Est ce que vous pouvez me dire à quoi va ressembler la table de routage d'un subnet privé ?
* Est ce que vous voyez quel problème peut poser des IP publiques éphémères ?
* Est ce que vous voyez à quoi peut servir d'avoir plusieurs ENI sur une même machine ?

Préciser les use cases pour avoir plusieurs ENI sur une seule machine, ou use case pour voir une EIP
* Contraintes de sécurité (une ENI public, et une ENI privée)
* Connection à plusieurs VPC (dans le même compte)
* Low cost HA solution : transfer ENI to another EC2
* MAC-Based Licensing

Démo Security Group / ACL  + Analogies

Quizz sur les security group / ACL à la place du tableau de synthèse

# Module 4 : Compute

* User Story EC2 : Treat your server like cattle, not like a pet.
* Quizz sur les use cases par type d'instances
* Key pair : analogie cadenas / clef
* Probes 
  * Qu'est ce qui porte l'adresse IP d'une instance ?
  * Comment gère-t-on la sécurité d'un EC2
    * Instance Role
    * Security Group
  * ENI
* Placement Group : analogie avec le flex
* Scripts and Metadata
  * A quoi sert le user data ? Rappel sur l'AMI = static, user data = Dynamique
  * Metadata : récupérer des informations dynamiques sur l'instance.

* Console : 
  * montrer les propriétés EC2 au fur et à mesure
  * montrer Amazon Q qui fait des recommandations sur les types d'instance en fonction du workload
  * montrer la lambda dans la console, mieux que le powerpoint. Faire un démo en même temps.

# Module 5 : Storage

* Quizz sur les cas d'usage, sachant qu'on est dans un mode Write Once - Read Many
* Reminder : sur identity based policies vs resource based policy pour le bucket S3
* Petit quizz sur la syntaxe d'une policy
* Access Point : Analogie
* Analogie
  * On a un livre, on va stocker une page ou un ensemble de pages sur des étagères différents. C'est plus performant, car lorsque l'on cherche quelque chose, on chercher dans ces pages, plutôt que des chercher dans tous le livre
  * On a un livre, on stocke le livre dans son entiereté mais on le classe dans une hiérarchie à plusieurs niveaux (folder) d'une manière à le trouver plus facilement. Par exemple on a une bibliothèque qui classe les livres par ordre alphabétique.
  * Chaque livre a une référence. On peut facilement retrouver le livre avec sa référence (object key) mais c'est à peu près tout
  [cloud storage types](https://www.freecodecamp.org/news/cloud-storage-options/)
* User Story : Intelligent Tiering
* Demo : Bucket Versioning
* User Story : Lambda
* Quizz sur les cas d'usage, sachant les contraintes de la lambda
* Eventuellement une petite démo Lambda pour montrer la facilité d'usage

* Console : 
  * montrer le bucket s3
  * montrer en live le block public access
  * le bucket policy qui donne un accès publique

# Module 6 : Database

Il faudrait une analogie pour expliquer la différence entre SQL et NoSQL
Supermarché vs panier customisé

* Quizz on noSQL vs SQL to validate knowledge in case people already know that.
* User Story
* Reminder : sur les zones de disponibilité, sur les régions pour le DR éventuellement.
* Autour de la sécurité : en plus de l'encryption, poser la question comment peut on sécuriser la base en terme de réseau, d'accés. Question piège sur l'accès à la data.
* Quizz sur les use cases possible de DynamoDB
  * Sur la sécurité :
    *  Poser des questions sur le réseau (question piège car dynamo ne vit pas dans un VPC)
    *  Opérations sur l'infra et la data (IAM dans les 2 cas)
* Demo DynamoDB

# Module 7 : Monitoring & scaling

* Poll questions on why we should care about monitoring ? 

* Reminder : AWS Organizations for cloudtrail especially
* User story : Predictive scaling

* Reminder : utilisation du user data et AMI pour la cloudwatch log agent.
On peut aussi l'installer dans une AMI, mais il faut que 
  * la config soit mise à jour dynamiquement
  * faire attention aux mises à jour du log agent
  * Ne pas mettre les AWS Credentials dans l'AMI

* Quizz on what ? Use cases for ELB maybe ?

* Analogies sur les Target Group / ELB -> Service après vente
* Analogies sur les dimensions de métriques : Notes sur classe/élève/matière

* Console : cloudwatch metrics + cloudtrail

# Module 8 : Automation

* InfraAsCode comme l'Imprimante 3D : On écrit les spécifications de la maison, et c'est la machine qui execute 
* Cross stack / Nested Stack, c'est comme dans l'industrie. On a des acteurs qui récupère les matières premières, d'autres qui font des composants de bas niveau (semi conducteurs par exemple, des vis..), d'autres acteurs qui font des choses de grandes valeur ajouté (moteur d'avion), puis l'assemblage.
* Reminder : EC2 Session Manager, Operational excellence (WA Framework)
* Pas de quizz, pas d'idée et pas trop le temps
* Show AWS Solutions Library : Instance Scheduler
* User Story : System Manager
* Demo : Code Whisperer

Console : CDK, AWS Solutions library

# Module 9 : Containers

* N'expliquer avec la machine à café que si quelqu'un ne connait pas les micro services
* On peut faire le quizz au tout début 
* User Story : EKS 
* Analogy : Ikea pour les container
* Faire la démo en 2 temps
  * !! Ne pas oublier de démarrer Rancher Desktop !!
  * D'abord ECR. Montrer ECR sur la console pendant que le docker push s'execute
  * Démo Fargate au moment où on parle de Fargate
    * Montrer le whiteboard avec celui de la démo pour montrer l'analogie avec les EC2
    * Executer la démo Fargate

# Module 10 : Networking 2

## Déroulé 

* Demo : VPC Peering
* Quizz : Direct connect vs Site-to-site VPN
* Transit Gateway
  * Introduire le sujet sur la première slide
  * Raconter la customer success story (ZenDesk) 
  * Expliquer le fonctionnement de la transit gateway avec l'analogie sur le whiteboard
  * Puis basculer sur la console pour executer la démo
  * Redérouler les slides en précisant les différents types d'attachement, et en parlant de Network Manager

## Requirements Direct Connect

* Single-mode fiber
  * 1000BASE-LX (1310 nm) transceiver for 1 G 
  * 10GBASE-LR (1310 nm) transceiver for 10 G
  * 100GBASE-LR4 for 100 G
* 802.1Q VLAN encapsulation must be supported
* Auto-negotiation for the port must be disabled
* Port speed and full-duplex mode must be configured manually
* End Customer Router (on-premises) must support Border Gateway Protocol (BGP) and BGP MD5 authentication
* (optional) Bidirectional Forwarding Detection


# Module 11 : Serverless

* Passer rapidement sur les features d'API Gateway, ne pas le montrer dans la console
* Faire la démo avec la Lambda
* Raconter l'exemple IRP buffering pour illustrer SQS
  * Spot instances avec sqs (fault tolerant workload)
* Montrer la console SQS au moment d'aborder les queues Standard et FIFO
* Montrer les whiteboards pour expliquer le polling et le visibility timeout
* User Story : SNS
* Faire les poll question SNS/SQS
* Passer très vite sur Kinesis et StepFunction. Pas le temps de faire une démo à priori
* Si il y a le temps, parler de l'analogie nature vs tour de contrôle pour la step function
 
# Module 12 : Edge

* Poll question pour l'introduction aux Edge
  * Maillage de trains
* Route 53
  * Analogy annuaire
  * montrer la geoproximity avec la console
* Raconter l'histoire Zalando au moment du cloudfront overview
* montrer CloudFront sur la console pour dérouler la configuration
* Faire la Démo WAF au lieu de montrer le ppt
* Eventuellement raconter la customer success story Firewall Manager si il y a du temps
* Passer vite sur Outpost

# Module 13 : Backup

* User Story : ---
* Analogy : Car wheels and airplanes engines for difference between high availability and fault tolerant
* Demo : AWS Backup
* Quizz sur les stratégies de DR
* Probes : 
  * A quoi est il important de pense qd on fait des backup ?
  * Poser des questions sur le RTO / RPO


* Off-site backup is a method of backing up data to a remote server or to media that's transported off site
* Colocation facilities : ce sont des sites multi-tenant en gros
* Tape retrievals
* On-premise backups are data backups that copy your hardware data to a storage device placed in-house