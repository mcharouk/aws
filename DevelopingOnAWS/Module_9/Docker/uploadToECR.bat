aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 637423642269.dkr.ecr.eu-west-3.amazonaws.com
docker tag lambda-on-docker-demo:latest 637423642269.dkr.ecr.eu-west-3.amazonaws.com/lambda-on-docker-demo:latest
docker push 637423642269.dkr.ecr.eu-west-3.amazonaws.com/lambda-on-docker-demo:latest
