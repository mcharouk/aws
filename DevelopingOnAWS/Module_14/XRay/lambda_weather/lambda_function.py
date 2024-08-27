import json

import requests
from aws_lambda_powertools import Tracer
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEventV2

MODULES = ["requests"]
tracer = Tracer(patch_modules=MODULES, service="weather-function")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    event = APIGatewayProxyEventV2(event)
    latitude = event.get_query_string_value("latitude")
    longitude = event.get_query_string_value("longitude")

    with tracer.provider.in_subsegment("## get_current_temperature") as subsegment:
        temperature_response = get_current_temperature(latitude, longitude)

    temperature_json = {
        "temperature": temperature_response["temperature"],
        "wind_speed": temperature_response["wind_speed"],
    }

    return {
        "isBase64Encoded": "false",
        "statusCode": 200,
        "body": json.dumps(temperature_json),
    }


def get_current_temperature(latitude, longitude):
    current = "temperature_2m,wind_speed_10m"

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": latitude, "longitude": longitude, "current": current},
    )

    # get current temperature from response
    response_json = response.json()

    return {
        "temperature": response_json["current"]["temperature_2m"],
        "wind_speed": response_json["current"]["wind_speed_10m"],
    }
