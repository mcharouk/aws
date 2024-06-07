aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 637423642269.dkr.ecr.eu-west-3.amazonaws.com
docker build -t %1 .
docker tag %1:latest 637423642269.dkr.ecr.eu-west-3.amazonaws.com/%1:latest
docker push 637423642269.dkr.ecr.eu-west-3.amazonaws.com/%1:latest
