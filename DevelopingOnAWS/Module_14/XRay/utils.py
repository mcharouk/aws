import os


def change_current_directory():
    # get the current working directory
    current_working_directory = os.getcwd()
    # print output to the console
    print("current directory : " + current_working_directory)

    if current_working_directory.endswith("DevelopingOnAWS"):
        new_wd = "Module_14/XRay"
        print(
            "changing working directory to " + current_working_directory + "/" + new_wd
        )
        os.chdir(new_wd)