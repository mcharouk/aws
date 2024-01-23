* De manière générale, solliciter les sachants à partager leurs bonnes pratiques sur les sujets qu'ils maitrisent

# Infrastructure

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

# IAM

Reminder : pas trop

* Analogie : AssumeRole / Policier
* Quizz avant d'aborder les policies.


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
  
Security Reference Architecture : [SRA](https://docs.aws.amazon.com/prescriptive-guiance/latest/security-reference-architecture/architecture.html)

# Networking 1

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

Démo Security Group / ACL  + Analogies

Quizz sur les security group / ACL à la place du tableau de synthèse

# Compute

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

# Storage

* Quizz sur les cas d'usage, sachant qu'on est dans un mode Write Once - Read Many
* Reminder : sur identity based policies vs resource based policy pour le bucket S3
* Petit quizz sur la syntaxe d'une policy
* Access Point : Analogie
* User Story : Intelligent Tiering
* Demo : Bucket Versioning
* User Story : Lambda
* Quizz sur les cas d'usage, sachant les contraintes de la lambda
* Eventuellement une petite démo Lambda pour montrer la facilité d'usage

* Console : 
  * montrer le bucket s3
  * montrer en live le block public access
  * le bucket policy qui donne un accès publique

# Database

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

# Monitoring

* Poll questions on why we should care about monitoring ? 

* Reminder : AWS Organizations for cloudtrail especially
* User story : Logging

* Reminder : utilisation du user data et AMI pour la cloudwatch log agent.
On peut aussi l'installer dans une AMI, mais il faut que 
* la config soit mise à jour dynamiquement
* faire attention aux mises à jour du log agent
* Ne pas mettre les AWS Credentials dans l'AMI

* Quizz on what ? Use cases for ELB maybe ?

* Analogies sur les Target Group / ELB -> Service après vente

* Console ! le plus sympa c'est de créer une instance EC2 en avance de phase pour montrer les métriques dessus (CPU) et créer une alarme.

# Automation

* InfraAsCode comme l'Imprimante 3D : On écrit les spécifications de la maison, et c'est la machine qui execute 
* Cross stack / Nested Stack, c'est comme dans l'industrie. On a des acteurs qui récupère les matières premières, d'autres qui font des composants de bas niveau (semi conducteurs par exemple, des vis..), d'autres acteurs qui font des choses de grandes valeur ajouté (moteur d'avion), puis l'assemblage.
* Reminder : EC2 Session Manager, Operational excellence (WA Framework)
* Quizz ? on peut demander aux gens si ils ont déjà pratiqué du LLM, ChatGPT pour coder.
* Show AWS Solutions Library : [Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/?did=fs_card&trk=fs_card)
* User Story : System Manager
* Demo : Code Whisperer

Console : CDK, montrer mon poste

# Containers

* Solliciter des personnes pour expliquer l'intérêt des containers ou de l'orchestrateur de container
* Quizz as Reminder : Target Groups, ELB
* User Story : EKS
* Analogy : Coffee Machine, Panier pour des recettes
* Demo : Fargate & ECR
* Console : faire la démo en 2 temps (ECR et Fargate ensuite)

# Networking 2

* As introduction : Reminder on public subnet / private subnet. 
* Analogy sur How to access AWS endpoints :  Je possède deux apparts adjacents. Au lieu de sortir dans le couloir à chaque fois pour accéder à l'autre appartement, je vais construire une porte entre les 2 appartements pour ne pas passer par le couloir à chaque fois.

* Probes : Site-to-site VPN ou direct connect
  * Voyez vous un SPOF sur le schéma (site to site) ? 
* Quizz : Direct connect vs Site-to-site VPN
* Demo & Analogy : Transit Gateway / réseau sociaux
* Console : montrer les VPC endpoints SSM dans la démo de la transit gateway
* Reminder : Security group sur la démo de la transit gateway

# Serverless

* User Story : SNS
* Analogy : SQS restaurant, Orchestrateur vs choregraphy
* Demo : API Gateway, maybe Step Functions
* Quizz : SNS vs SQS en Quizz
* Reminder : 
  * Différences et similitude avec API Gateway / ALB. Dire comment intéger un ALB dans l'archi API Gateway
  * Parler de SQS et scaling sur ApproximateNumberOfMessage : Créer une cloudwatch alarm, ASG, etc...
* Probes : 
  * Qui connait le pattern API Gateway
  * Qui connait la différence entre la chroégraphie et l'orchestration ?
* Console : API Gateway / StepFunction. 
Le reste est pas trop intéressant et est déjà montré dans le lab

# Edge

* User Story : Firewall Manager & Shield
* Analogy : CloudFront, maillage de trains. Route 53 annuaire.
* Demo : AWS WAF
* Quizz : Local Zone / Edge Locations / Snowball / Region
* Reminder : 
  * Edge Locations. 
  * Local zone quant on parle d'outpost.
* Probes
  * Citer des attaques déni de service
  * Est ce que quelqu'un sait ce qu'est un CDN ?
* Console : 
  * montrer CloudFront peut être intéressant, pour montrer ce qu'on doit configurer
  * Montrer l'éditeur de policy de route53, intéressant pour le geoproximity

# Backup

* User Story : ---
* Analogy : Car wheels and airplanes engines for difference between high availability and fault tolerant
* Demo : AWS Backup
* Quizz sur les stratégies de DR
* Probes : 
  * A quoi est il important de pense qd on fait des backup ?
  * Poser des questions sur le RTO / RPO
