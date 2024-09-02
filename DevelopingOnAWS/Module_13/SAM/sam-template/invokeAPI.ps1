# invoke api https://8xkfai1c6g.execute-api.eu-west-3.amazonaws.com/Prod every 1 seconds
$url="https://ibtxgfex9a.execute-api.eu-west-3.amazonaws.com/prod"
$timeout = new-timespan -Minutes 5
$sw = [diagnostics.stopwatch]::StartNew()
while ($sw.elapsed -lt $timeout){
    Invoke-RestMethod -Uri $url
    start-sleep -seconds 1
}
 
write-host "Timed out"