$param1=$args[0]

if ( $param1 -eq "deploy" )
{
    cdk deploy --require-approval never   
    cd ../sam-template
    sam deploy
    sam deploy --config-env prod
    cd ../sam-demo
    python generateInvokeAPIScripts.py
}
ElseIf( $param1 -eq "destroy" )
{
    cd ../sam-template
    sam delete --no-prompts
    sam delete --config-env prod --no-prompts
    cd ../sam-demo
    cdk destroy -f
    python cleanResources.py
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}