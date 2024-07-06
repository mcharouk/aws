$param1=$args[0]
$StackName="scorekeep"

if ( $param1 -eq "deploy" )
{
    aws cloudformation deploy --template .\xray-scorekeep\cloudformation\cf-resources.yaml --stack-name $StackName --capabilities CAPABILITY_NAMED_IAM
}
ElseIf( $param1 -eq "destroy" )
{
    aws cloudformation delete-stack --stack-name $StackName 
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}