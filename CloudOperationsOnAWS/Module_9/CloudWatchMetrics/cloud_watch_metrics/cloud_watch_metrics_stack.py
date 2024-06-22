from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_cloudwatch as cloudwatch
from constructs import Construct


class CloudWatchMetricsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        namespace = "ExampleCorp-Factory"
        factory_name = "Plant-p76"
        machine_names = ["Hoven-h476483", "Hoven-h904736", "Hoven-284748"]

        using_metrics = {}
        metrics = []
        for machine_name in machine_names:
            metric = cloudwatch.Metric(
                metric_name="Temperature",
                namespace=namespace,
                dimensions_map={
                    "FactoryName": factory_name,
                    "MachineName": machine_name,
                },
                statistic="Average",
            )
            using_metrics[machine_name.lower().replace("-", "")] = metric

        metrics.append(self.create_math_expression("MAX", using_metrics))
        metrics.append(self.create_math_expression("AVG", using_metrics))
        metrics.append(self.create_math_expression("MIN", using_metrics))

        widget = cloudwatch.GraphWidget(
            title="TemperatureAggregates",
            left=metrics,
            set_period_to_time_range=True,
        )

        dashboard = cloudwatch.Dashboard(
            self, "PlantDashboard", dashboard_name="PlantDashboard"
        )

        dashboard.add_widgets(widget)

    def create_math_expression(self, aggOperation, metrics_map):
        return cloudwatch.MathExpression(
            expression=f"{aggOperation}(METRICS())",
            label=f"[{aggOperation} Temperature, avg: ${{AVG}}]",
            using_metrics=metrics_map,
        )
