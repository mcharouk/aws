$param1=$args[0]

if ( $param1 -eq "deploy" )
{  
    # cdk deploy LakeFormationAdminStack --require-approval never
    # cdk deploy LakeFormationStack --require-approval never
    # cdk deploy LakeFormationGlueCrawlerStack --require-approval never
    cdk deploy --all --require-approval never
    python runCrawler.py
}
ElseIf( $param1 -eq "destroy" )
{
    python cleanResources.py   
    cdk destroy -f --all
}
Else
{
throw 'Action not recognized. Must be either deploy or destroy'
}