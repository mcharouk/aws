$param1=$args[0]

if ( $param1 -eq "deploy" )
{
    npx aws-cdk deploy --require-approval never    
}
ElseIf( $param1 -eq "destroy" )
{
    npx aws-cdk destroy -f
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}