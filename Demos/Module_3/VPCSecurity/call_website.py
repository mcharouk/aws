adress = "http://ec2-52-47-79-41.eu-west-3.compute.amazonaws.com/"

# recusively call api

from time import sleep

import requests


def get_data(url):
    response = requests.get(url)
    return response.content


while True:
    print(get_data(adress))
    sleep(5)
