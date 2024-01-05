import json
import random


def lambda_handler(event, context):
    # generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    return {"quantity": random_number}
