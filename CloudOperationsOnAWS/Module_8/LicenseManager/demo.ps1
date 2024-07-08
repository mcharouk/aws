$param1=$args[0]

if ( $param1 -eq "deploy" )
{
    python LicenseConfigurationInitializer.py
    cdk deploy --all --require-approval never
}
ElseIf( $param1 -eq "destroy" )
{
    cdk destroy -f --all
    python cleanResources.py
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}