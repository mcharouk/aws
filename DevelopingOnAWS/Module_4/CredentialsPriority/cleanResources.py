# delete file aws-config-result.txt and aws-credentials-result.txt
import os

config_file_path = "config.json"
# check if file exists and remove it if so

if os.path.exists(config_file_path):
    os.remove(config_file_path)
    print(f"{config_file_path} has been deleted successfully")
else:
    print(f"{config_file_path} does not exist")
