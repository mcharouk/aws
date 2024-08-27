import os
import shutil

import utils

utils.change_current_directory()

# delete folder layer-package if it exists
folder_path = "layer-package"

if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    print("The folder has been deleted successfully.")
else:
    print("The folder does not exist.")
