$param1=$args[0]

if ( $param1 -eq "deploy" )
{
    .\buildLayerPackage.ps1
    cdk deploy --require-approval never
    python testAPI.py
}
ElseIf( $param1 -eq "destroy" )
{
    cdk destroy -f
    python cleanResources.py
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}