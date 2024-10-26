json_file = "myjson-file.json"


import json

with open(json_file, "r") as f:
    data = json.load(f)

    # extract me the distinct first level keys and print the count
    first_level_keys = list(data.keys())
    print(f"First level keys number: {first_level_keys}")
