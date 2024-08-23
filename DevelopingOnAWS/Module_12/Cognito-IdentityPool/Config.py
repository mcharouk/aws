import boto3


class Config:

    def __init__(self):

        cognito_idp = boto3.client("cognito-idp")
        user_pools = cognito_idp.list_user_pools(MaxResults=60)["UserPools"]

        for user_pool in user_pools:
            if user_pool["Name"] == "UserPoolForIdentityPoolDemo":
                self.user_pool_id = user_pool["Id"]

                self.user_pool_client_id = cognito_idp.list_user_pool_clients(
                    UserPoolId=self.user_pool_id
                )["UserPoolClients"][0]["ClientId"]
                # return client secret
                self.user_pool_client_secret = cognito_idp.describe_user_pool_client(
                    UserPoolId=self.user_pool_id, ClientId=self.user_pool_client_id
                )["UserPoolClient"]["ClientSecret"]

        cognito_idp.close()

        # get identity pool id
        cognito_identity = boto3.client("cognito-identity")
        self.identity_pool_id = cognito_identity.list_identity_pools(MaxResults=60)[
            "IdentityPools"
        ][0]["IdentityPoolId"]
        self.region_name = "eu-west-3"
        self.bucket_name = "marc-charouk-identitypool-demo"
        cognito_identity.close()
