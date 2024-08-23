$param1=$args[0]
$StackName="StepFunctionDemo-StockOrder"

if ( $param1 -eq "deploy" )
{
    aws cloudformation deploy --template .\cloudformation\stepfunction_template.yaml --stack-name $StackName --capabilities CAPABILITY_NAMED_IAM
    aws cloudformation wait stack-create-complete --stack-name $StackName 
}
ElseIf( $param1 -eq "destroy" )
{
    aws cloudformation delete-stack --stack-name $StackName 
    aws cloudformation wait stack-delete-complete --stack-name $StackName 
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}