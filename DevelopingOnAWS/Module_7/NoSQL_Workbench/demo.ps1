$param1=$args[0]

if ( $param1 -eq "deploy" )
{
    python update-connection-credentials.py
}
ElseIf( $param1 -eq "destroy" )
{    
    python cleanResources.py
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}