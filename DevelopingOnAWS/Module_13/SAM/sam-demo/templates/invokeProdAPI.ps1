$url=##INVOKE_URL##
$timeout = new-timespan -Minutes 5
$sw = [diagnostics.stopwatch]::StartNew()
while ($sw.elapsed -lt $timeout){
    Invoke-RestMethod -Uri $url
    start-sleep -seconds 1
}
 
write-host "Timed out"