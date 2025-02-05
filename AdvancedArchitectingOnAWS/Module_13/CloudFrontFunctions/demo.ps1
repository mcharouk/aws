$param1=$args[0]

if ( $param1 -eq "deploy" )
{  
    # cdk deploy CloudFrontFunctionsStack 
    # cdk deploy CloudFrontDistributionStack 
    cdk deploy --all --require-approval never   
    python generate-script-files.py
}
ElseIf( $param1 -eq "destroy" )
{
    # cdk destroy CloudFrontFunctionsStack 
    # cdk destroy CloudFrontDistributionStack 
    python cleanResources.py
    cdk destroy -f --all
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}