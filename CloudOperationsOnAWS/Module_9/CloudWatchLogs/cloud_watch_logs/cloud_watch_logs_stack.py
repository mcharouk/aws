import boto3
from aws_cdk import RemovalPolicy, Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_logs as logs
from constructs import Construct


class CloudWatchLogsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        log_group_name = "logs_demo"
        self.create_log_group(log_group_name)

        log_stream_name = "webServer-i87465854"

        # create cloud watch log stream
        logs.LogStream(
            self,
            "webServerLogStream",
            log_group=logs.LogGroup.from_log_group_name(
                self, "webServerLogGroup", log_group_name
            ),
            log_stream_name=log_stream_name,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # create QueryDefinition

        queryDefinitionName = "1_pattern_tab"
        queryString = logs.QueryString(
            filter_statements=[f'@logStream = "{log_stream_name}"'],
            fields=["@message"],
        )

        logs.QueryDefinition(
            self,
            queryDefinitionName,
            query_definition_name=queryDefinitionName,
            query_string=queryString,
        )

        queryDefinitionName = "2_extract_structured_from_plain_text"
        queryString = logs.QueryString(
            parse_statements=[
                '@message "* - - [* +0000] \\"* * HTTP/1.1\\" * *" as log_ip, log_time, log_method, log_path, log_status, log_bytes'
            ],
            filter_statements=[
                f'@logStream = "{log_stream_name}"',
                'log_method in ["GET", "POST"]',
            ],
            sort="log_status",
            display="log_ip, log_time, log_method, log_path, log_status",
            limit=25,
        )

        logs.QueryDefinition(
            self,
            queryDefinitionName,
            query_definition_name=queryDefinitionName,
            query_string=queryString,
        )

        queryDefinitionName = "3_count_per_log_status_and_hour"
        queryString = logs.QueryString(
            parse_statements=[
                '@message "* - - [* +0000] \\"* * HTTP/1.1\\" * *" as log_ip, log_time, log_method, log_path, log_status, log_bytes'
            ],
            filter_statements=[
                f'@logStream = "{log_stream_name}"',
            ],
            stats="count(*) by log_status, bin(1h)",
        )

        logs.QueryDefinition(
            self,
            queryDefinitionName,
            query_definition_name=queryDefinitionName,
            query_string=queryString,
        )

    def create_log_group(self, log_group_name):
        # return log group if existss
        cloudwatch_client = boto3.client("logs")
        log_groups = cloudwatch_client.describe_log_groups(
            logGroupNamePattern=log_group_name
        )
        if len(log_groups["logGroups"]) > 0:
            print(f"log group {log_group_name} already created")
        else:
            log_group = cloudwatch_client.create_log_group(logGroupName=log_group_name)
            print(f"Log group '{log_group_name}' created successfully")
