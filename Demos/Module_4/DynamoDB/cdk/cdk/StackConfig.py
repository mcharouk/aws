import yaml


class StackConfig:

    def __init__(self):
        with open("config.yml", "r") as config_file:
            config = yaml.safe_load(config_file)
            aws = config["aws"]
            dynamoDB = config["demo"]["dynamodb"]
            s3 = config["demo"]["s3"]
            lambdaConfig = config["demo"]["lambda"]

            self.accountId = aws["accountId"]
            self.region = aws["region"]
            self.dynamoDBTableName = dynamoDB["tableName"]
            self.dynamoDBPartitionKey = dynamoDB["partitionKey"]
            self.dynamoDBSortKey = dynamoDB["sortKey"]
            self.dynamoDBSecondaryRegion = dynamoDB["secondaryRegion"]
            self.bucketName = s3["bucketName"]
            self.inputObjectPrefix = s3["inputObjectPrefix"]
            self.generate_lambda = lambdaConfig["generate"]
            self.lambdaName = lambdaConfig["name"]
