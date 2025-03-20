$param1=$args[0]


if ( $param1 -eq "synth" )
{
    $env:AWS_PROFILE = $null
    cdk synth 
}
ElseIf( $param1 -eq "deploy" )
{
    $env:AWS_PROFILE = $null
    cdk deploy --require-approval never      
}
ElseIf( $param1 -eq "destroy" )
{
    $env:AWS_PROFILE = $null
    python cleanResources.py        
    cdk destroy -f
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}
