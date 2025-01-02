# Get ECR login token and login to Docker
$app = "capacity-provider-app"
$ecrPassword = aws ecr get-login-password --region eu-west-3
$ecrPassword | docker login --username AWS --password-stdin 637423642269.dkr.ecr.eu-west-3.amazonaws.com

#change directory to sample-app
Set-Location '.\sample-app'

# Build the Docker image
docker build -t $app .

# Tag the image
docker tag "$($app):latest" "637423642269.dkr.ecr.eu-west-3.amazonaws.com/$($app):latest"

# Push the image to ECR
docker push "637423642269.dkr.ecr.eu-west-3.amazonaws.com/$($app):latest"

Set-Location '.\..'

