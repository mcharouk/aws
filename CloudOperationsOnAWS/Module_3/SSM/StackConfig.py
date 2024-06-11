import yaml


class StackConfig:

    def __init__(self):
        with open("config.yml", "r") as config_file:
            config = yaml.safe_load(config_file)

            self.sessionLoggingBucketName = config["demo"]["sessionLogging"]["s3"]["bucketName"]
            self.sessionLoggingKeyPrefix = config["demo"]["sessionLogging"]["s3"]["keyPrefix"]
