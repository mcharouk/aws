import json
import os
import random

import boto3
from faker import Faker
from lambdaDemo.StackConfig import StackConfig

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("Demos"):
    new_wd = "TechEssentials/Module_2/Lambda"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

stackConfig = StackConfig()

# Initialize Faker
fake = Faker()


# Function to generate synthetic data
def generate_synthetic_data(num_records):
    synthetic_data = []

    industry_categories = [
        "Technology",
        "Healthcare",
        "Manufacturing",
        "Finance and Banking",
        "Retail",
        "Energy and Utilities",
        "Telecommunications",
        "Automotive",
        "Education",
        "Hospitality and Tourism",
    ]

    for i in range(num_records):
        record = {
            "index": i + 1,
            "organization_id": fake.uuid4()[:16],
            "name": fake.company(),
            "website": fake.url(),
            "country": fake.country(),
            "description": fake.catch_phrase(),
            "founded": random.randint(1900, 2023),
            "industry": random.choice(industry_categories),
            "number_of_employees": random.randint(1, 100000),
        }
        synthetic_data.append(record)

    return synthetic_data


# Generate 10 synthetic records
num_records = 100
synthetic_data = generate_synthetic_data(num_records)

sqs_queue_name = stackConfig.sqsQueueName
# send these json in sqs queue
sqs = boto3.resource("sqs")

queue = sqs.get_queue_by_name(QueueName=sqs_queue_name)
for record in synthetic_data:
    print(f"Sending message: {record}")
    response = queue.send_message(MessageBody=json.dumps(record))
    print(f"Message sent to queue: {response['MessageId']}")
