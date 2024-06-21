import yaml


class StackConfig:

    def __init__(self):
        with open("config.yml", "r") as config_file:
            config = yaml.safe_load(config_file)
            aws = config["aws"]
            logs = aws["logs"]
            self.logs_group_name = logs["groupName"]
            self.logs_stream_name = logs["streamName"]
            self.logs_wait_time = logs["waitTime"]
