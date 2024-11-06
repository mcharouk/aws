import utils
import os

utils.change_current_directory()
# remove file invokeDevAPI.ps1if it exists


def remove_file_if_exists(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File {file_name} removed")
    else:
        print(f"File {file_name} does not exist")


remove_file_if_exists("invokeDevAPI.ps1")
remove_file_if_exists("invokeProdAPI.ps1")
