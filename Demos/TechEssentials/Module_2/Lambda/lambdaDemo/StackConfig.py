import yaml


class StackConfig:

    def __init__(self):
        with open("config.yml", "r") as config_file:
            config = yaml.safe_load(config_file)
            aws = config["aws"]
            dynamoDB = config["demo"]["dynamodb"]
            sqs = config["demo"]["sqs"]
            lambda_prop = config["demo"]["lambda"]

            self.accountId = aws["accountId"]
            self.region = aws["region"]
            self.dynamoDBTableName = dynamoDB["tableName"]
            self.dynamoDBPartitionKey = dynamoDB["partitionKey"]

            self.sqsQueueName = sqs["queueName"]
            self.lambdaName = lambda_prop["name"]
