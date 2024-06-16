import yaml


class StackConfig:

    def __init__(self):
        with open("config-private.yml", "r") as config_file:
            config = yaml.safe_load(config_file)
            sns = config["sns"]

            self.sns_mail = sns["mail"]

        with open("config.yml", "r") as config_file:
            config = yaml.safe_load(config_file)
            aws = config["aws"]
            s3 = aws["s3"]
            self.aws_accountId = aws["accountId"]
            self.s3_cloudTrailBucketName = s3["cloudTrailBucketName"]
