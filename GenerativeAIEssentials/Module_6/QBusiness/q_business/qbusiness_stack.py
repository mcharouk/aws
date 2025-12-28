from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_iam as iam,
    aws_qbusiness as qbusiness,
    CfnOutput,
    RemovalPolicy,
)
from constructs import Construct


class QBusinessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket for sample data
        self.sample_data_bucket = s3.Bucket(
            self,
            "SampleDataBucket",
            bucket_name="marccharouk-qbusiness-sampledata",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            versioned=False,
            public_read_access=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        # Upload sample files to S3
        s3deploy.BucketDeployment(
            self,
            "DeploySampleData",
            sources=[s3deploy.Source.asset("data/")],
            destination_bucket=self.sample_data_bucket,
            include=["Anycompany.txt", "dog-breeds.txt"],
            retain_on_delete=False,
        )        

        # Create minimal role for S3 data source access
        self.s3_data_source_role = self.create_s3_data_source_role()

        # Create Q Business web experience role
        self.web_experience_role = self.create_web_experience_role()

        # Get Identity Center URLs for SAML configuration
        self.identity_center_urls = self.get_identity_center_urls()

        # Create Q Business application
        self.qbusiness_application = self.create_qbusiness_application()

        # Create Q Business web experience with proper SAML configuration
        self.web_experience = self.create_web_experience()

        self.index = self.create_index()
        # Create data source for S3
        self.datasource = self.create_s3_data_source()

        # Outputs       
        CfnOutput(
            self,
            "QBusinessApplicationId",
            value=self.qbusiness_application.attr_application_id,
            description="Q Business Application ID",
        )

        CfnOutput(
            self,
            "QBusinessApplicationArn",
            value=self.qbusiness_application.attr_application_arn,
            description="Q Business Application ARN",
        )

        CfnOutput(
            self,
            "QBusinessIndexId",
            value=self.index.attr_index_id,
            description="Q Business Index Id",
        )

        CfnOutput(
            self,
            "QBusinessS3DatasourceId",
            value=self.datasource.attr_data_source_id,
            description="Q Business S3 Datasource Id",
        )


        

    def create_s3_data_source_role(self):
        """Create minimal IAM role for S3 data source access only"""
        role = iam.Role(
            self,
            "S3DataSourceRole",
            assumed_by=iam.ServicePrincipal("qbusiness.amazonaws.com"),
            description="Role for Q Business S3 data source access",
        )

        # Add only S3 permissions needed for data source
        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:GetObject",
                    "s3:ListBucket",
                    "s3:GetBucketLocation",
                ],
                resources=[
                    self.sample_data_bucket.bucket_arn,
                    f"{self.sample_data_bucket.bucket_arn}/*",
                ],
            )
        )

        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                sid="AllowsAmazonQToIngestDocuments",
                actions=["qbusiness:BatchPutDocument", "qbusiness:BatchDeleteDocument"],
                resources=["*"],
            )
        )

        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                sid="AllowsAmazonQToCallPrincipalMappingAPIs",
                actions=[
                    "qbusiness:PutGroup",
                    "qbusiness:CreateUser",
                    "qbusiness:DeleteGroup",
                    "qbusiness:UpdateUser",
                    "qbusiness:ListGroups",
                ],
                resources=["*"],
            )
        )

        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                sid="AllowsAmazonQToPassCustomerRole",
                actions=[
                    "iam:PassRole"
                ],
                resources=[f"arn:aws:iam::"+ self.account +":role/QBusiness-DataSource-*"],
                conditions={
                    "StringLike": {
                        "iam:PassedToService": "qbusiness.amazonaws.com"
                    }
                }
            )
        )

        return role

    def create_web_experience_role(self):
        """Create IAM role for Q Business web experience"""

        # Create assume role policy document with required actions for Identity Center integration
        assume_role_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "application.qbusiness.amazonaws.com"},
                    "Action": ["sts:AssumeRole", "sts:SetContext"],
                }
            ],
        }

        role = iam.Role(
            self,
            "QBusinessWebExperienceRole",
            assumed_by=iam.ServicePrincipal("application.qbusiness.amazonaws.com"),
            description="Web experience role for Q Business application",
        )

        # 2. Override the Trust Policy (Assume Role Policy)
        # to include both sts:AssumeRole and sts:SetContext
        role.assume_role_policy.add_statements(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                principals=[
                    iam.ServicePrincipal("application.qbusiness.amazonaws.com")
                ],
                actions=["sts:AssumeRole", "sts:SetContext"],
            )
        )

        # Add necessary permissions for web experience
        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                sid="QBusinessCorePermissions",
                actions=[
                    "qbusiness:Chat",
                    "qbusiness:ChatSync",
                    "qbusiness:ListMessages",
                    "qbusiness:ListConversations",
                    "qbusiness:DeleteConversation",
                    "qbusiness:PutFeedback",
                    "qbusiness:GetWebExperience",
                    "qbusiness:GetApplication",
                    "qbusiness:ListPlugins",
                    "qbusiness:GetUser",
                    "qbusiness:GetGroup",
                    "qbusiness:PutGroup",
                    "qbusiness:CreateUser",
                    "qbusiness:DeleteGroup",
                    "qbusiness:ListGroups",
                    "qbusiness:GetChatControlsConfiguration",
                ],
                resources=["*"],
            )
        )

        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                sid="QBusinessAttachmentPermissions",
                actions=["qbusiness:ListAttachments", "qbusiness:DeleteAttachment"],
                resources=["*"],
            )
        )

        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                sid="QBusinessPluginPermissions",
                actions=[
                    "qbusiness:ListPluginActions",
                    "qbusiness:ListPluginTypeMetadata",
                    "qbusiness:ListPluginTypeActions",
                ],
                resources=["*"],
            )
        )

        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                sid="QBusinessMediaPermissions",
                actions=["qbusiness:GetMedia"],
                resources=["*"],
            )
        )

        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                sid="QBusinessDocumentPermissions",
                actions=["qbusiness:GetDocumentContent"],
                resources=["*"],
            )
        )

        return role

    def get_identity_center_urls(self):
        """Get Identity Center URLs for SAML configuration"""
        instance_id = "ssoins-6656599b102550ba"

        # Return the authentication URL for SAML configuration
        authentication_url = (
            f"https://portal.sso.eu-west-3.amazonaws.com/saml/sso/{instance_id}"
        )

        return {"authentication_url": authentication_url}

    def create_qbusiness_application(self):
        """Create Q Business application"""
        # Q Business application uses the service-linked role automatically
        # No need to specify a role_arn - it will use the service-linked role
        application = qbusiness.CfnApplication(
            self,
            "QBusinessApplication",
            display_name="QBusiness-demo-application",
            description="Demo application for AWS Q Business with sample data",
            identity_center_instance_arn="arn:aws:sso:::instance/ssoins-6656599b102550ba",
        )

        return application

    def create_web_experience(self):
        """Create Q Business web experience with proper SAML configuration"""
        web_experience = qbusiness.CfnWebExperience(
            self,
            "QBusinessWebExperience",
            application_id=self.qbusiness_application.attr_application_id,
            title="Q Business Demo Web Experience",
            subtitle="Demo web interface for Q Business with sample data",
            role_arn=self.web_experience_role.role_arn,
            identity_provider_configuration=qbusiness.CfnWebExperience.IdentityProviderConfigurationProperty(
                saml_configuration=qbusiness.CfnWebExperience.SamlProviderConfigurationProperty(
                    authentication_url=self.identity_center_urls["authentication_url"]
                )
            ),
        )

        return web_experience

    def create_index(self):
         return qbusiness.CfnIndex(
            self,
            "QBusinessIndex",
            application_id=self.qbusiness_application.attr_application_id,
            display_name="sample-data-index",
            description="Index for sample data from S3",
            type="STARTER",
            capacity_configuration=qbusiness.CfnIndex.IndexCapacityConfigurationProperty(
                units=1
            ),
        )

    def create_s3_data_source(self):

        q_retriever = qbusiness.CfnRetriever(
            self,
            "QBusinessRetriever",
            application_id=self.qbusiness_application.attr_application_id,
            display_name="MyRetriever",
            type="NATIVE_INDEX",
            configuration=qbusiness.CfnRetriever.RetrieverConfigurationProperty(
                native_index_configuration=qbusiness.CfnRetriever.NativeIndexConfigurationProperty(
                    index_id=self.index.attr_index_id  # Connect retriever to your index
                )
            ),
        )

        # Create data source
        data_source = qbusiness.CfnDataSource(
            self,
            "S3DataSource",
            application_id=self.qbusiness_application.attr_application_id,
            index_id=self.index.attr_index_id,
            display_name="s3-sample-data-source",
            description="Data source for sample files in S3",           
            configuration={
                "type": "S3V2",
                "connectionConfiguration": {
                    "bucketName": self.sample_data_bucket.bucket_name,
                    "bucketOwnerAccountId" : self.account
                }
            },
            role_arn=self.s3_data_source_role.role_arn,
        )

        return data_source
