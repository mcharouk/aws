aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 270188911144.dkr.ecr.eu-west-3.amazonaws.com
docker build -t %1 .
docker tag %1:latest 270188911144.dkr.ecr.eu-west-3.amazonaws.com/sample-app:%1
docker push 270188911144.dkr.ecr.eu-west-3.amazonaws.com/%1:latest