# Module 1

Console
 * Montrer IAM User
 * MFA / AccessKey
 * Groupes
 * Policies
 * Montrer comment assumer un rôle


# Module 2 : Compute

* Story EC2
* Console
  * AMI
  * Families
  * Demo : Run an EC2
  * Lien [Script](Module_3/VPCSecurity/vpc_security/configure.sh)
  * Lifecycle
* Quizz Families
* Customer Success Story on [ECS](https://aws.amazon.com/solutions/case-studies/flywire-ecs-case-study/?did=cr_card&trk=cr_card)
* Lambda : demo

# Module 3 : VPC

* Mettre un ec2 dans un subnet privé (avec addresse IP publique). 
* but de la démo : convertir le subnet privé en subnet public
* lancer un script qui permet d'installer apache et une page basique
* se connecter à l'instance publique
* Montrer les ACL et SecGroup mais sans les modifier

# Module 4

S3: Démo
* Créer un bucket
* Mettre une image dans avec au moins un folder
* Activer le versionning
* Montrer le block public access et la bucket policy

# Module 5

* User story dynamo (MySQL -> Dynamo)
* Si il y a le temps : créer une table, expliquer sortkey/partitionkey, faire quelques requêtes
* Besoin d'avoir des data samples à charger

# Module 6

* Console
  * Cloudwatch logs et métriques
* Whiteboard
  * ALB/NLB/GLB
  * simple scaling policy / Step scaling policy
  * Story predictive scaling
