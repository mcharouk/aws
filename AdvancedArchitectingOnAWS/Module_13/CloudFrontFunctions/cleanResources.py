import os

import utils

utils.change_current_directory()

demo_folder = "demo"
# remove all files and folders in demo_folder
# ignore file .gitkeep

for file in os.listdir(demo_folder):
    if file == ".gitkeep":
        print("Ignoring file: " + file)
        continue
    if os.path.isfile(os.path.join(demo_folder, file)):
        print("Removing file: " + file)
        os.remove(os.path.join(demo_folder, file))
    else:
        for sub_file in os.listdir(os.path.join(demo_folder, file)):
            print("Removing file: " + sub_file)
            os.remove(os.path.join(demo_folder, file, sub_file))
        print("Removing folder: " + file)
        os.rmdir(os.path.join(demo_folder, file))
