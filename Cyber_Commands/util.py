import subprocess
import os


def runCommand(command, simple=False, returncode=False):


    if not type(command) == str:
        print("ERROR: run command passed non string type")
        return

    if simple:
        os.system(command)
        return
    
    command = command.split(" ")

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout = process.communicate()[0]
    rc = process.returncode

    if returncode:
        return (stdout, rc)
    else:
        return stdout


def makeUserAdmin(user):
    _, s = runCommand("sudo adduser " + user + " sudo", returncode=True)
    if s == 1:
        print("ERROR: Was unable to promote " + user + " to admin")
    else:
        print(user + " promoted to admin")

def demoteUser(user):
    _, s = runCommand("sudo deluser " + user + " sudo", returncode=True)

    if s == 1:
        print("ERROR: Was unable to demote " + user)
    else:
        print(user + " was demoted to standard user")

