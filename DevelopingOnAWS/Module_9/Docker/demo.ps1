$param1=$args[0]

if ( $param1 -eq "deploy" )
{
    cdk deploy --require-approval never    
}
ElseIf( $param1 -eq "destroy" )
{
    cdk destroy -f
    .\kill-container.ps1
    python cleanResources.py
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}