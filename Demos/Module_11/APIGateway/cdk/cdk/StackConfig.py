import yaml


class StackConfig:

    def __init__(self):
        with open("config.yml", "r") as config_file:
            config = yaml.safe_load(config_file)
            self.generate_api_gateway = config["demo"]["apigateway"]["generate"]
            self.lambda_name = config["demo"]["lambda"]["name"]
            self.api_gateway_rest_api_name = config["demo"]["apigateway"]["restapiname"]
