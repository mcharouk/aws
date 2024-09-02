import json
import os
import random
import time

import boto3
import requests
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEventV2
from aws_lambda_powertools.utilities.typing import LambdaContext

tracer = Tracer(service="weather-function")
dynamodb = boto3.resource("dynamodb")
weather_url = parameters.get_parameter("/xraydemo/weather-url")
logger = Logger(service="city-function")

os.environ["TZ"] = "Europe/Paris"
time.tzset()


@tracer.capture_lambda_handler
@logger.inject_lambda_context
def lambda_handler(event, context: LambdaContext):
    event = APIGatewayProxyEventV2(event)
    country = event.get_query_string_value("country")
    city = event.get_query_string_value("city")

    logger.append_keys(city=city, country=country)

    # list = [1, 2, 3, 4, 5]
    # if random.choice(list) == 4:
    #    raise Exception("Unlucky guy, you encounter a random exception")

    # get item from table cities with partition key as city and sort key as country

    with tracer.provider.in_subsegment("## get_cities_info") as subsegment:
        subsegment.put_annotation(key="City", value=city)
        subsegment.put_annotation(key="Country", value=country)
        item = get_from_dynamo_db(city, country)

    capital = get_item_attribute(item, "capital")
    population = get_item_attribute(item, "population")
    city = get_item_attribute(item, "city_ascii")
    latitude = get_item_attribute(item, "lat")
    longitude = get_item_attribute(item, "lng")
    iso2 = get_item_attribute(item, "iso2")
    iso3 = get_item_attribute(item, "iso3")

    with tracer.provider.in_subsegment("## get_weather") as subsegment:
        weather_response = get_weather(latitude, longitude)

    response_json = {
        "capital": capital,
        "population": population,
        "city": city,
        "iso2": iso2,
        "iso3": iso3,
        "temperature": weather_response["temperature"],
        "wind_speed": weather_response["wind_speed"],
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response_json),
    }


def get_from_dynamo_db(city, country):
    table = dynamodb.Table("cities")

    logger.info(f"Getting item from DynamoDB: {city}, {country}")
    response = table.get_item(Key={"city_ascii": city, "iso2": country})
    return response["Item"]


def get_weather(latitude, longitude):
    fields = {"latitude": latitude, "longitude": longitude}
    logger.info(f"Getting weather for {latitude}, {longitude}", extra=fields)

    response = requests.get(f"{weather_url}?latitude={latitude}&longitude={longitude}")
    return response.json()


def get_item_attribute(item, attribute_name):
    if attribute_name in item:
        return item[attribute_name]
    else:
        return None
