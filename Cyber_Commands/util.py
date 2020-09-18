import subprocess
import os


def runCommand(command, simple=False):

    if not type(command) == str:
        print("ERROR: run command passed non string type")
        return

    if simple:
        os.system(command)
        return
    
    command = command.split(" ")

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()

    if stdout:
        return stdout
    else:
        return stderr