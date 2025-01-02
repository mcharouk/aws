$param1=$args[0]

if ( $param1 -eq "deploy" )
{  
    cdk deploy --require-approval never
    .\uploadToECR.ps1
}
ElseIf( $param1 -eq "destroy" )
{
    python cleanResources.py
    .\cleanLocalImage.ps1
    cdk destroy -f
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}