$param1=$args[0]

if ( $param1 -eq "deploy" )
{
    
}
ElseIf( $param1 -eq "destroy" )
{
    python cleanResources.py
    python cleanPolicies.py
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}