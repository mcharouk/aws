$param1=$args[0]

if ( $param1 -eq "deploy" )
{ 
    cdk deploy QBusinessDemoStack --require-approval never
    python add-user-in-application.py
    python execute-sync-job.py
}
ElseIf( $param1 -eq "destroy" )
{    
    cdk destroy -f QBusinessDemoStack        
}
Else
{
    throw 'Action not recognized. Must be deploy or destroy'
}