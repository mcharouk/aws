# Sécurité

* Lier le least privilege principle avec le Well Architected Framework
* Pour les organisations, meilleure contrôle des coûts : well architected framework

# Networking

* Rappels sur les régions et les availability zones
* Rappels sur le Well architected framework et la haute dispo (Reliability)
* Rappels sur le Well architected framework et la sécurité (Security groups, NACLs)

# Compute

* EC2 : Instance Role, VPC, Subnet, Security Group
* EBS : vit dans une AZ
* Placement group : rappels AZs pour les spread et les partition
* Lambda : Performance (Well Architected Framework)

# Storage

* Rappel sur EBS : Block storage
* S3 : rappels sur les identity policies vs resource based policies
* Well Architected Framework et encryption (Sécurité)
* Access Point via un VPC
* EFS vit dans un VPC, multi-AZ, ces mount point (via des ENI !) ont un security group qui doivent ouvrir le port NFS (TCP 2049) en inbound
* Transfer Acceleration : Edge Locations
* S3 multi AZ, lives in a single region

# Serverless

Quel composant peut jouer un rôle de point d'entrée d'une architecture micro service ?

* ALB
* GLB
* ECS

# Automation

