* De manière générale, solliciter les sachants à partager leurs bonnes pratiques sur les sujets qu'ils maitrisent

# Module 1 : Infrastructure

* Local Zone : Netflix
* Local Zone vs Edge Locations : Poll questions
* Well Architected Framework : Game to recognize icons
* Well architected Tool
  * Customer success story
  * Show on Console

# Module 2 : IAM

* Authentication 
  * Show user part on console
  * AssumeRole / Policier
  * Poll questions
* Authorization
  * Whiteboard on Resource based policy
  * Permission Boundary
    * Analogie Constitution / Loi
    * whiteboard + demo
* Multi account
  * Analogie appartements / syndic
  * Qd on parle du pourquoi d'AWS Organizations
    * Warner Bros  
  * Qd on parle d'AWS Organzations
    * Lien SRA / Control Tower

# Module 3 : Networking 1

* Whiteboard + analogie pour expliquer les addresses IP
* Table de routage : panneau d'indication
* Whiteboard pour les différentes ENI sur une seule machine
* Démo Security Group / ACL  + Analogie Avion / Cinéma
* Poll question sur les security group / ACL

# Module 4 : Compute

* User Story EC2 : Treat your server like cattle, not like a pet.
* montrer les propriétés EC2 au fur et à mesure
* Type d'instances
  * Quizz sur les use cases par type d'instances
  * montrer Amazon Q qui fait des recommandations sur les types d'instance en fonction du workload
* EC2 Networking : probes ?
* Placement Group : Analogie avec le flex
* Scripts and Metadata
  * A quoi sert le user data ? Rappel sur l'AMI = static, user data = Dynamique
  * Metadata : récupérer des informations dynamiques sur l'instance.
* Spot Pricing
  * Whiteboard
  * Montrer les prix sur la console (aller dans Spot Requests dans le menu, puis aller dans Pricing History)
* Lambda   
  * Ne pas trop montrer les slides, plutôt montrer le whiteboard de démo et la démo
  * User Story : Lambda pour illustrer les cas d'usages

# Module 5 : Storage

* Analogie sur les types de storage
  * On a un livre, on va stocker une page ou un ensemble de pages sur des étagères différents. C'est plus performant, car lorsque l'on cherche quelque chose, on chercher dans ces pages, plutôt que des chercher dans tous le livre
  * On a un livre, on stocke le livre dans son entiereté mais on le classe dans une hiérarchie à plusieurs niveaux (folder) d'une manière à le trouver plus facilement. Par exemple on a une bibliothèque qui classe les livres par thèmes puis par ordre alphabétique d'auteur, etc...
  * Chaque livre a une référence. On peut facilement retrouver le livre avec sa référence (object key) mais c'est à peu près tout
  [cloud storage types](https://www.freecodecamp.org/news/cloud-storage-options/)
* S3 : Montrer sur la console la partie accès
* Access Point : Analogie
* Lifecycle policies
  * User Story : sur l'Intelligent Tiering 
* Demo : Bucket Versioning
* Quizz sur les cas d'usage en synthèse d'EFS
* Customer Success Story sur la storage gateway

# Module 6 : Database

* Dynamodb customer success story pour illustrer SQL vs NoSQL
* RDS : customer success story
* Link Aurora (livre blanc)
* Aller sur la console qd on crée la table dynamoDB, plutôt que de montrer les slides
* Whiteboard RCU / WCU
* Demo DynamoDB Global Tables
* Link DynamoDB (livre blanc)
* Elasticache : whiteboard si il y a du temps

# Module 7 : Monitoring & scaling

* Analogies sur les dimensions de métriques : Notes sur classe/élève/matière
* Montrer les métriques sur CloudWatch
* Whiteboard CloudWatch / EC2
* Reminder : AWS Organizations for cloudtrail especially
* Demo CloudTrail
* Whiteboard ALB
* User story : Predictive scaling

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