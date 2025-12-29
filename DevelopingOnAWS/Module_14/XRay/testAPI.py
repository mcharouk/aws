import boto3
import pandas as pd
import requests
import utils

# get ssm parameter named /xraydemo/city-url
ssm = boto3.client("ssm")

api_url_param = ssm.get_parameter(Name="/xraydemo/city-url")
api_url = api_url_param["Parameter"]["Value"]
print(f"api url is {api_url}")

utils.change_current_directory()

# get csv file in decompressed_file/cities.csv
# get only columns city_ascii and iso2
# pick randomly 30 cities from csv file


def get_random_cities():
    cities = pd.read_csv(
        "./decompressed_file/cities.csv", usecols=["city_ascii", "iso2"]
    )
    cities = cities.sample(n=30)
    return cities.to_dict("records")


# print random cities
random_cities = get_random_cities()
for city in random_cities:
    api_full_url = f"{api_url}?city={city['city_ascii']}&country={city['iso2']}"
    print("calling api for city:", api_full_url)
    response = requests.get(api_full_url)
    print(response.json())


ssm.close()
