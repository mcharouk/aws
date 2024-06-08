import yaml


class StackConfig:

    def __init__(self):
        with open("config.yml", "r") as config_file:
            config = yaml.safe_load(config_file)
            aws = config["aws"]

            self.accountId = aws["accountId"]
