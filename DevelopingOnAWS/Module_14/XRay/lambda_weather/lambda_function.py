import json
import os
import time

import requests
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEventV2
from aws_lambda_powertools.utilities.typing import LambdaContext

MODULES = ["requests"]
tracer = Tracer(patch_modules=MODULES, service="weather-function")
logger = Logger(service="weather-function", log_uncaught_exceptions=True)

os.environ["TZ"] = "Europe/Paris"
time.tzset()


@tracer.capture_lambda_handler
@logger.inject_lambda_context
def lambda_handler(event, context):
    event = APIGatewayProxyEventV2(event)
    latitude = event.get_query_string_value("latitude")
    longitude = event.get_query_string_value("longitude")
    logger.append_keys(latitude=latitude, longitude=longitude)

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
    logger.info(f"Getting temperature for latitude: {latitude}, longitude: {longitude}")
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": latitude, "longitude": longitude, "current": current},
    )

    # get current temperature from response
    response_json = response.json()

    temperature = ""
    wind_speed = ""
    if "current" in response_json:
        temperature = response_json["current"]["temperature_2m"]
        wind_speed = response_json["current"]["wind_speed_10m"]
        logger.info(f"found temperature: {temperature}, wind_speed: {wind_speed}")
    else:
        logger.info("no current state in api response")

    return {
        "temperature": temperature,
        "wind_speed": wind_speed,
    }
