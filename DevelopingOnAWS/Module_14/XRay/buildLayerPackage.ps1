New-Item -Path . -Name "python" -ItemType "directory"
$layerPackageFolder = ".\layer-package"
If(!(test-path -PathType container $layerPackageFolder))
{
      New-Item -Path . -Name $layerPackageFolder -ItemType "directory"
} 
Else
{
      Remove-Item $layerPackageFolder\*.*
}

Copy-Item -Path .\layer-code\* -Destination ".\python" -Recurse
Set-Location -Path .\python
pip install -t . -r requirements.txt --no-user
Set-Location -Path .\..

Compress-Archive -Path .\python -DestinationPath $layerPackageFolder\layer-package.zip
Remove-Item '.\python' -Recurse

