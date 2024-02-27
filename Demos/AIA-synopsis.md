# Points importants

* Lorsque c'est possible, si des gens ont déjà utilisés les services, les inciter à partager leur expérience et leur avis sur ce qu'apporte le service
* Si on fait référence à des concepts expliqués dans les cours d'avant, poser des questions simples pour vérifier que les élèves ont bien retenu les points

# Module 1 : Infrastructure

## Intro

* Sur l'infra
  * Montrer le Gartner
  * AWS est le cloud provider qui a inventé le concept de cloud publique en 2006.
  * Ils ont construit une infrastructure globale scalable qui a permis a des entreprises de pouvoir construire des systèmes qu'ils n'avaient pas la capacité d'opérer on premise. J'exposerais des illustrations tout au long de ce cours.
  * Le mindset d'AWS vise à offrir leurs services comme enabler de use cases quelque soit leur complexité
* Sur les bonnes pratiques
  * AWS se pose comme un des leaders mondiaux de l'innovation technologique dans le domaine des systèmes d'information
  * Rejoindre AWS, c'est aussi apprendre et intégrer des bonnes pratiques qui permettent de diffuser la culture de l'excellence prôné par AWS dans l'entreprise

## Déroulé

* Local Zone
  * Netflix
* Local Zone vs Edge Locations
  * Poll questions
* Well Architected Framework
  * Game to recognize icons
* Well architected Tool
  * Customer success story
  * Show on Console

# Module 2 : Security Account

## Intro

* Pour AWS, la sécurité est le pillier le plus important. Lorsqu'ils font des architecture en interne, et ont le choix entre plusieurs architectures, ils prennent systématiquement la plus sécurisée.
* Une système secure est un 
* Les système de droit étant très fin, ils sont partout dans AWS, il est donc très important de comprendre comment cela fonctionne.
* Maitriser les droits sur AWS, c'est de ne pas faire de compromis sur la sécurité tout en minimisant les dépendances opérationnelles afin de faciliter l'innovation.

## Déroulé

* Authentication 
  * Show user part on console
  * AssumeRole / Policier
  * Poll questions
* Authorization
  * Whiteboard on Resource based policy
    * Show identity based vs resource based
    * PPT to show Principal keyword
    * Whiteboard Explicit Deny
  * Permission Boundary
    * Analogie Constitution / Loi
    * whiteboard demo + demo
* Multi account
  * Analogie appartements / syndic
  * Qd on parle du pourquoi d'AWS Organizations
    * Warner Bros  
  * Qd on parle d'AWS Organzations
    * Lien SRA / Control Tower

# Module 3 : Networking 1

## Intro

* AWS met à disposition des composants réseaux permettant d'isoler et sécuriser ses resources, et de le scaler jusqu'à pouvoir développer un réseau global privé
* VPC fondamentaux d'AWS, difficile de travailler sur AWS sans en comprendre le fonctionnement
* Montrer le Capstone Architecture

## Déroulé

* IP Addressing
  * Whiteboard + analogie pour expliquer les addresses IP
* VPC / Subnet
  * Faire des rappels sur la region et les Availability zones
* Route Table
  * Analogie Panneau d'indication
* ENI
  * Whiteboard
* Security Group vs NACL
  * Analogie Avion / Cinema
  * Demo
  * Poll questions

# Module 4 : Compute

## Intro

* Le compute est depuis le début un des facteurs d'attraction principaux d'AWS vis à vis de leurs clients.
* Le service EC2 est une référence depuis sa sortie en 2006.
* L'intérêt du compute sur AWS est 
  * l'elasticité
  * la puissance de calcul disponible avec une grande gamme de types d'instance
  * le côté éphémère qui permet in fine de réduire les coûts
* EC2 est la pierre angulaire de cette mécanique. 
* L'infrastructure serverless est une forme d'aboutissemnet de l'aspect élastique et la lambda en est un des symboles les plus emblématiques.
* Montrer le Capstone Architecture

## Déroulé 

* EC2
  * User Story EC2 : Treat your server like cattle, not like a pet.
  * montrer les propriétés EC2 au fur et à mesure sur la console
  * Type d'instances
    * Quizz sur les use cases par type d'instances
    * montrer Amazon Q qui fait des recommandations sur les types d'instance en fonction du workload
  * EC2 Networking
    * probes/reminder
  * Placement Group : Analogie avec le flex ?
  * Scripts and Metadata
    * A quoi sert le user data ? Rappel sur l'AMI = static, user data = Dynamique
    * Metadata : récupérer des informations dynamiques sur l'instance.
  * Spot Pricing
    * Whiteboard / console (aller dans Spot Requests dans le menu, puis aller dans Pricing History)
* Lambda
  * Montrer whiteboard de demo
  * Demo
    * Montrer la création de la lambda + la configuration de l'event s3    
    * Lancer l'ingestion s3 et montrer les logs
    * Ensuite Montrer les limites (15 min, 10 Go), parler des use cases
    * Raconter la user story
    * A la fin montrer le monitoring de la lambda, on devrait voir le scaling dans les métriques

# Module 5 : Storage

## Intro

* Avec le compute, le storage est une autre attraction majeure du cloud car il permet d'avoir accès à un stockage pas cher, élastique, performant, avec une capacité de stockage quasiment illimité, sans faire le moindre effort de provisioning matériel
* Fais souvent partie des premiers use cases cloud pour pouvoir migrer rapidement et s'accoutumer avec cette nouvelle technologie
* Montrer le Capstone Architecture

## Déroulé 

* Types de storage
  * Analogie sur les types de storage
    * On a un livre, on va stocker une page ou un ensemble de pages sur des étagères différents. C'est plus performant, car lorsque l'on cherche quelque chose, on chercher dans ces pages, plutôt que des chercher dans tous le livre
    * On a un livre, on stocke le livre dans son entiereté mais on le classe dans une hiérarchie à plusieurs niveaux (folder) d'une manière à le trouver plus facilement. Par exemple on a une bibliothèque qui classe les livres par thèmes puis par ordre alphabétique d'auteur, etc...
    * Chaque livre a une référence. On peut facilement retrouver le livre avec sa référence (object key) mais c'est à peu près tout
    * [cloud storage types](https://www.freecodecamp.org/news/cloud-storage-options/)
* S3
  * Montrer sur la console la partie accès
  * Access Point : Analogie
  * Lifecycle policies -> User Story sur l'Intelligent Tiering vs lifecycle policies
  * Demo Bucket Versioning
* EFS
  * Quizz sur les cas d'usage en synthèse
* Storage Gateway
  * Customer Success Story

# Module 6 : Database

## Intro

* Montrer le Gartner
* l'intérêt des bases de données managées, c'est d'avoir des bases résilientes, scalables, performantes, sécurisées avec peu de temps à investir sur la maintenance et le build. Ce sont des bases "DBA-less" (même si le terme peut être un peu exagéré !)
* AWS offre un large choix de BDD, on en verra quelques unes au cours de ce module
* Montrer le Capstone Architecture

## Déroulé

* SQL / NoSQL
  * Dynamodb customer success story 
* RDS
  * Customer success story
* DynamoDB
  * Quizz sur use cases dynamodb
  * Demo
* Elasticache
  * Whiteboard si il y a du temps (détail l'archi Memached vs redis)

# Module 7 : Monitoring & scaling

## Intro

* Le scaling et l'elasticité est souvent une des choses que viennent chercher les clients sur le cloud. 
* La virtualisation des ressources étant l'enabler pour avoir accès à de l'elasticité sans limite, celle-ci est en général plus difficile à réaliser on-premise.
* Ce module vise à expliquer le fonctionnement du scaling sur AWS de la collecte de données qui est un des triggers d'autoscaling, jusqu'au provisonnement dynamique des ressources.
* Montrer le Capstone Architecture

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
* C'est la promesse de construire des infrastructures éphémères qui est un facteur d'optimisation des coûts
* L'automatisation améliore l'efficacité et permet de passer plus de temps sur les features métiers.
* Qd on parle d'automatisation sur AWS c'est entre autres
  * automatisation de l'infra : AWS offre une vaste gamme de solutions plus ou moins managés pour que chacun puisse trouver le meilleur compromis entre customisation et solutions "plug and play"
  * automatisation des opérations de production (day2day maintenance)
  * automatisation du code : On verra dans ce module une innovation à la pointe de la technologie en matière d'IA autour de la génération de code automatique, CodeWhisperer (ChatGPT like)

## Déroulé

* InfraAsCode
  * Analogie imprimante 3d
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
* Code Whisperer
  * Demo

# Module 9 : Containers

## Intro

* Les containers sont la dernière brique de compute que l'on a pas vu, après EC2 et les FaaS (lambda)
* Les containers ont révolutionné depuis une dizaine d'années le monde des systèmes d'informations grâce à la portabilité qui les caractérise.
* Les containers ont bcp contribué au développement d'architecture micro services qui privilégient 
  * la scalabilité
  * la flexibilité
  * la vélocité de livraison de features métiers. 
* L'architecture micro services est fortement recommandé par AWS pour maximiser les avantages de la plateforme.
* Dans ce module on va traiter des sujets de conteneurs de la simple définition du concept jusqu'à décrire comment on obtient une infrastructure managée, scalable et serverless.

## Déroulé

**!! Ne pas oublier de démarrer Rancher Desktop !!**

* Intro
  * Poll questions 
* Micro services
  * N'expliquer avec la machine à café que si quelqu'un ne connait pas les micro services
* Container
  * Analogie Ikea
* ECR
  * 1ere partie Demo
  * Montrer ECR sur la console pour expliquer les features
* EKS
  * User Story
* Fargate
  * Démo
    * Montrer le whiteboard avec celui de la démo pour montrer l'analogie avec les EC2
    * Executer la démo

# Module 10 : Networking 2

## Intro

* On a vu en 1ère partie les composants fondamentaux du VPC
* Dans la réalité, on est souvent amener à travailler sur un scope plus large qu'un simple VPC
  * Architecture hybride
  * Architecture multi-comptes (au moins autant de VPC que de comptes)
  * Architecture globalisée / multi-régions
* Ce module traite de la connectivité du VPC avec le monde qui l'entoure et de la mise à l'échelle globale de ces composants

## Déroulé 

* Intro
  * Poll question au début des rappels réseaux
* VPC Endpoint
  * Whiteboard : parler du choix que l'on a sur S3
* VPC Peering
  * Demo
* Direct connect vs site-to-site VPN
  * Poll questions
* Transit Gateway
  * Introduire le sujet sur la première slide
  * Raconter la customer success story (ZenDesk) 
  * Expliquer le fonctionnement de la transit gateway avec l'analogie sur le whiteboard
  * Puis basculer sur la console pour executer la démo
  * Redérouler les slides en précisant les différents types d'attachement, et en parlant de Network Manager
  * Montrer la centralized inspection pattern comme cas d'usage concret (si il y a du temps)

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

* le serverless est l'aboutissement de ce que peut offrir une plateforme comme AWS, car la promesse initiale est de manager l'infrastructure du client.
  * Les EC2 permettent d'abstraire l'infrastructure physique
  * Le serverless permet d'abstraire l'infrastructure virtuelle et physique
* On a déjà vu des services serverless à ce stade (lambda, S3, DynamoDB par ex.), on va voir plusieurs services supplémentaires qui complètent le tableau des services formant le noyau dur d'AWS.

## Déroulé

* API Gateway
  * Passer rapidement sur les features d'API Gateway
  * ne pas le montrer dans la console
  * Faire la démo avec la Lambda
* SQS
  * Raconter l'exemple IRP buffering pour illustrer SQS  
  * Montrer la console SQS au moment d'aborder les queues Standard et FIFO
  * Montrer les whiteboards pour expliquer le polling et le visibility timeout
  * Question sur les spot instances
* SNS
  * User Story : SNS
  * Faire les poll question SNS/SQS en fonction du timing
* Passer rapidement sur Kinesis
* StepFunction
  * analogie tour de contrôle
  * montrer les exemples de use case sur le dashboard

# Module 12 : Edge

## Intro

* On a à ce stade déjà parlé du edge du point de vue infra, mais pas d'occasion de parler des services qui opèrent dessus.
* Le edge est une des force d'AWS, c'est ce qui permet d'étendre son réseau au delà des régions afin d'offrir la plus faible latence au plus grand nombre
* C'est aussi sur le edge qu'AWS a deployé des services majeurs qui traitent de la lutte contre les cyberattaques. Elles sont donc incontournables dans le monde d'aujourd'hui où les attaques sont de plus en plus nombreuses avec un niveau d'intensité croissant. Notamment, le risques d'attaque commandité par un pays est une menace accrue. AWS a bloqué une attaque en 2020 avec un pic de traffic de l'ordre de **2.3 Tb/s**
* Ce module est un focus sur ces services qui tournent sur le edge, avec en arrière plan 2 pilliers du Well-Architected Framework, la performance et la sécurité 

## Déroulé

* Introduction
  * Poll questions (Rappel edge infra)
  * Analogie Maillage de trains
* Route 53
  * Analogy annuaire
  * montrer la geoproximity avec la console
* CloudFront
  * Analogy distributeur billets pour le cache
  * Raconter l'histoire Zalando au moment du cloudfront overview
  * montrer CloudFront sur la console pour dérouler la configuration
* DDoS
  * Faire la Démo WAF au lieu de montrer le ppt
  * Eventuellement raconter la customer success story Firewall Manager si il y a du temps
* Passer vite sur Outpost

# Module 13 : Backup

## Intro

* La gestion des backup et des DR est toujours un sujet compliqué dans l'IT car cela oblige à dupliquer son infrastructure, voire à devoir s'étendre dans un autre pays. Les coûts associés sont toujours très importants. Cela oblige à mobiliser une infrastructure conséquente sans garantie de l'utiliser réellement, c'est une forme de gaspillage (jusqu'à tant d'avoir un évènement qui justifie cet investissement)
* AWS avec son réseau global et son infrastructure mutualisée, permet de bcp moins gaspiller, d'être plus efficace (grâce à sa capacité à automatiser) mais sans compromis sur la résilience.
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