# Get ECR login token and login to Docker
$app = "cicd-sample-app"

#check image exists

if (docker images -q $app) {
    # image exists
    docker image rm $app --force
} else {
    # image does not exist
    Write-Output "image does not exist"
}


