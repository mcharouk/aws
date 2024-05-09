# Lab 1 : Exploration de IAM

* Task 1 : add users to respective groups
* Task 2 : Ouvrir le navigateur en private
* Se connecter en tant que différents users pour executer des actions soit liés à leur rôle, soit autre afin de valider qu'ils n'ont pas accès.

user-1 -> accès à S3 (uniquement le bucket avec le nom s3bucket dedans)
user-2 -> accès à EC2 read only. Pas le droit de stopper des EC2 par exemple
user-3 -> EC2 admin. Droit de start et stopper des EC2 mais aucun droit sur S3

# Lab 2 : Exploration d'un VPC et création d'une instance EC2

* Dans ce lab, il faut créer 
  * un VPC
  * 2 subnets public
  * une IGW
  * une table de routage
  * un sec group
  * une instance EC2
* Tout est assez basique, la seule chose notable c'est qu'il faut passer par le nouveau wizard pour créer le VPC, ce qui facilite les choses.
* J'ai pas eu besoin de changer la table de routage, elle était déjà bien configurée.
* Ensuite, il faut créer le sec group. Attention à le mettre dans le bon VPC
* Ensuite l'instance -> pas de rôle IAM à donner.

# Lab 3 : S3 + DynamoDB

* Task 1 : Create an S3 bucket. Block public access default kept (activated)
* Task 2 : Autorisation à un rôle spécifique de lire les objets du bucket
  * Il faut mettre le bon rôle, et bien spécifier les resources (le bucket et le prefix)
* Task 3 : upload files in S3 bucket. Upload png in root folder
* Task 4 : Create DynamoDB. PartitionKey as String
* Task 6 : Add an employee in DynamoDB through the webapp
* Task 7 : Add an employee in DynamoDB through DynamoDB console


# Lab 4 : Haute disponibilité
