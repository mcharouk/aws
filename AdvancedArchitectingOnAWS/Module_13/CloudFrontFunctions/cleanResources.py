import os

import utils

utils.change_current_directory()

demo_folder = "demo"
# remove all files and folders in demo_folder
print(f"cleaning folder {demo_folder}")
for file in os.listdir(demo_folder):
    if os.path.isdir(f"{demo_folder}/{file}"):
        for sub_file in os.listdir(f"{demo_folder}/{file}"):
            os.remove(f"{demo_folder}/{file}/{sub_file}")
        os.rmdir(f"{demo_folder}/{file}")
        print(f"Removed folder: {demo_folder}/{file}")
    else:
        os.remove(f"{demo_folder}/{file}")
        print(f"Removed file: {demo_folder}/{file}")
