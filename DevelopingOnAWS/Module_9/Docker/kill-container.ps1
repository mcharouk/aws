$psCmdOutput = docker ps -a -q --filter ancestor=lambda-on-docker-demo

if (! [string]::IsNullOrEmpty($psCmdOutput)) {
Write-Output $psCmdOutput
$stopCmdOutput = docker stop $psCmdOutput
Write-Output $stopCmdOutput
docker rm $stopCmdOutput
} else {
   Write-Output "no container found for image lambda-on-docker-demo"
}

$imgCmdOutput = docker images -af reference='lambda-on-docker-demo*' -q

if (! [string]::IsNullOrEmpty($imgCmdOutput)) {
    docker image rm lambda-on-docker-demo:latest
} else {
   Write-Output "no image found for lambda-on-docker-demo"
}
