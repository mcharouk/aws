$param1=$args[0]

if ( $param1 -eq "deploy" )
{  
    cdk deploy CreateRepositoryStack --require-approval never
    .\uploadToECR.ps1
    cdk deploy DeployContainerStack --require-approval never
}
ElseIf( $param1 -eq "destroy" )
{
    python cleanResources_deployContainer.py
    python cleanResources_createRepo.py
    .\cleanLocalImage.ps1
    cdk destroy DeployContainerStack -f
    cdk destroy CreateRepositoryStack -f
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}