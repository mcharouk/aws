# Module 1 : Infrastructure

## Intro

* AWS est cloud provider qui a inventé le concept de cloud publique en 2006.
* Ils ont construit une infrastructure globale scalable qui a permis a maintes entreprises de pouvoir construire des systèmesqu'ils n'avaient pas la capacité d'opérer on premise
* Le mindset d'AWS vise à offrir leurs services comme enabler de use cases quelque soit leur complexité
* AWS se pose comme un des leaders mondiaux de l'innovation technologique dans le domaine des systèmes d'information
* Il est important de comprendre leurs bonnes pratiques car cela permet à une entreprise de s'imprégner de la culture d'AWS d'excellence.

## Déroulé

* Local Zone : Netflix
* Local Zone vs Edge Locations : Poll questions
* Well Architected Framework : Game to recognize icons
* Well architected Tool
  * Customer success story
  * Show on Console

# Module 2 : Security Account

## Intro

* De manière générale, la sécurité pour AWS est le pillier le plus important. Lorsqu'ils font des architecture en interne, etont le choix entre plusieurs architectures, ils prennent systématiquement la plus sécurisée.
* Les droits sont partout dans AWS, il est très important de comprendre comment cela fonctionne
* Le système de droits est extrêmement fin, mais il est important de bien le comprendre pour designer un système à la foissécurisée et en minimisant les dépendances opérationnelles afin de faciliter l'innovation.

## Déroulé

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

## Intro

* Composants réseaux pour isoler les resources tout en construisant un réseau global privé
* VPC fondamentaux d'AWS, difficile de travailler sur AWS sans comprendre les fondamentaux
* Montrer le Capstone Architecture

## Déroulé

* Whiteboard + analogie pour expliquer les addresses IP
* Table de routage : panneau d'indication
* Whiteboard pour les différentes ENI sur une seule machine
* Démo Security Group / ACL  + Analogie Avion / Cinéma
* Poll question sur les security group / ACL

# Module 4 : Compute

## Intro

* Le compute est depuis le début un des facteurs d'attration majeur d'AWS vis à vis de leurs clients.
* Le service EC2 est une référence depuis sa sortie en 2006.
* L'intérêt du compute sur le cloud publique est l'elasticité, la facilité à obtenir de l'infra performante et EC2 est lapierre angulaire de cette mécanique. L'infrastructure serverless est une forme d'aboutissemnet de l'aspect élastique et lalambda en est un des symboles les plus forts.

## Déroulé 

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

## Intro

* Avec le compute, le storage est une autre attraction du cloud car il permet d'avoir accès à un stockage pas cher, qui scale tout seul, avec une capacité de stockage quasiement illimité, sans faire le moindre effort de provisioning matériel
* Fais souvent partie des premiers use cases cloud pour pouvoir migrer rapidement et s'accoutumer avec cette nouvelle technologie

## Déroulé 

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

## Intro

* Montrer le Gartner
* l'intérêt des bases de données managées, c'est d'avoir des bases résilientes, scalables, performantes, sécurisées avec peu de temps à investir sur la maintenance et le build. Ce sont des bases "DBA-less" (même si le terme peut être un peu exagéré !)

## Déroulé

* Dynamodb customer success story pour illustrer SQL vs NoSQL
* RDS : customer success story
* Link Aurora (livre blanc)
* Aller sur la console qd on crée la table dynamoDB, plutôt que de montrer les slides
* Whiteboard RCU / WCU
* Demo DynamoDB Global Tables
* Link DynamoDB (livre blanc)
* Elasticache : whiteboard si il y a du temps

# Module 7 : Monitoring & scaling

## Intro

* Le scaling et l'elasticité est souvent une des choses que viennent chercher les clients sur le cloud. 
* La virtualisation des ressources étant l'enabler pour avoir accès à de l'elasticité sans limite, celle-ci est en général plus difficile à réaliser on-premise.
* Ce module vise à expliquer le fonctionnement du scaling sur AWS de la collecte de données qui est un des triggers d'autoscaling, jusqu'au provisonnement dynamique des ressources.

## Déroulé


* Analogies sur les dimensions de métriques : Notes sur classe/élève/matière
* Montrer les métriques sur CloudWatch
* Whiteboard CloudWatch / EC2
* Reminder : AWS Organizations for cloudtrail especially
* Demo CloudTrail
* Whiteboard ALB
* Poll ALB use cases
* User story : Predictive scaling

# Module 8 : Automation

## Intro

* L'automatisation de l'infrastructure est un des atouts majeurs d'une plateforme comme AWS. 
* C'est la possibilité de construire des infrastructures éphémères qui est un facteur d'optimisation des coûts
* L'automatisation améliore l'efficacité et permet de passer plus de temps sur les features métiers.
* AWS offre une vaste gamme de solutions plus ou moins managés pour que chacun puisse trouver le meilleur compromis entre customisation et solutions "plug and play"
* On verra aussi dans ce module une innovation à la pointe de la technologie autour de la génération de code automatique (ChatGPT like)

## Déroulé

* InfraAsCode comme l'Imprimante 3D : On écrit les spécifications de la maison, et c'est la machine qui execute 
* Cross stack / Nested Stack, c'est comme dans l'industrie. 
  * Matières premières
  * Composants de bas niveau (semi conducteurs par exemple, des vis..), 
  * Grandes valeur ajouté (moteur d'avion)
  * Assemblage
* Show AWS Solutions Library : Instance Scheduler
* Show CDK on my laptop
* System Manager
  * Whiteboard
  * Customer Success Story
* Demo : Code Whisperer

# Module 9 : Containers

## Intro

* Les containers sont la dernière brique de compute que l'on a pas vu, après EC2 et les FaaS (lambda)
* Les containers ont révolutionné depuis une dizaine d'années le monde des systèmes d'informations
* Dans ce module on va traiter des sujets de conteneurs de la simple définition même du concept jusqu'a à avoir une infrastructure managée, scalable et serverless.

## Déroulé

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

## Intro

* On a vu en 1ere partie les composants fondamentaux du VPC
* Dans la réalité, on est souvent amener à travailler sur un scope plus large qu'un simple VPC
  * Architecture hybride
  * Architecture multi comptes (au moins autant de VPC que de comptes)
  * Archiecture globalisée (plusieurs régions)
* Ce module traite de la connectivité du VPC avec le monde qui l'entoure

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

## Intro

* le serverless est l'aboutissement de ce que peut offrir une société comme AWS, car la promesse initiale est de manager l'infrastructure du client.
* On a déjà vu des services serverless à ce stade (lambda, S3, par ex.), on va voir plusieurs services supplémentaires qui complètent le tableau des services formant le noyau dur d'AWS.

## Déroulé

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

## Intro

* Le edge est une des force d'AWS, c'est ce qui permet d'étendre son réseau afin d'offrir la plus faible latence, la meilleure performance au plus grand nombre
* C'est aussi sur le edge qu'AWS a deployé ses services qui protègent contre les principales attaques informatiques. Elles sont donc incontournables dans le monde d'aujourd'hui ou les attaques sont de plus en plus nombreuses avec un niveau d'intensité de plus en plus fort. AWS a bloqué une attaque en 2020 avec un pic de traffic de l'ordre de **2.3 Tb/s**
* Ce module est un focus sur ces services qui tournent sur le edge.

## Déroulé

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

## Intro

* La gestion des backup et des DR est toujours un sujet compliqué dans l'IT car cela oblige à dupliquer son infrastructure, voire à devoir s'étendre dans un autre pays. Les coûts associés sont toujours très importants.
* AWS avec son réseau global conçu pour sa résilience, et sa capacité à automatiser est un facilitateur sur ce sujet.
* Ce module traite de la gestion de la panne à tous les niveaux avec un focus particulier sur le backup et le DR, où comment se remettre d'un désastre à une échelle régionale.

## Déroulé

* Analogie pour HA vs Fault Tolerance (Moteur d'avion vs roue d'une voiture)
* Poll questions pour les différentes options de Backup
* Whiteboard pour montrer les patterns réseaux
* Montrer la console pour backup

## Infos
* Off-site backup is a method of backing up data to a remote server or to media that's transported off site
* Colocation facilities : ce sont des sites multi-tenant en gros
* Tape retrievals
* On-premise backups are data backups that copy your hardware data to a storage device placed in-house