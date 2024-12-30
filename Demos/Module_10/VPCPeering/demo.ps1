$param1=$args[0]
#second parameter with default value as eu-west-3
$param2=$args[1]

if ( $null -eq $param2 )
{
    $param2="eu-west-3"
}

#set environment variable AWS_DEFAULT_REGION as second parameter
$env:AWS_DEFAULT_REGION=$param2

if ( $param1 -eq "deploy" )
{
    cdk deploy --require-approval never      
}
ElseIf( $param1 -eq "destroy" )
{
    python cleanResources.py
    cdk destroy -f
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}