import os
import signal
import subprocess
import time

import psutil


def generate_logs(wait_time):
    command = "python generate.py --truncate apache-config.yaml"
    print(f"running command : [{command}]")
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    print("process pid : " + str(process.pid))

    print(f"sleeping during {wait_time}")
    time.sleep(wait_time)

    parent = psutil.Process(process.pid)
    for child in parent.children(recursive=True):
        print(f"killing child process : {child.pid}")
        os.kill(child.pid, signal.SIGINT)

    print(f"killing parent process : {parent.pid}")
    os.kill(parent.pid, signal.SIGINT)
