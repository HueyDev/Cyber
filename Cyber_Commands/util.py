import subprocess
import os
import sys


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
        return False
    else:
        print(user + " promoted to admin")
        return True

def demoteUser(user):
    _, s = runCommand("sudo deluser " + user + " sudo", returncode=True)

    if s == 1:
        print("ERROR: Was unable to demote " + user)
        return False
    else:
        print(user + " was demoted to standard user")
        return True


def confirmAction(message="Please confirm(y/n)"):
    while True:
        i = input(message)
        if i.lower() == "n":
            return False
        elif i.lower() == "y":
            return True
        else:
            print("Invalid input")


def deleteUser(user):
    print("Deleting " + user)
    _, r = runCommand("sudo deluser " + user, returncode=True)
    runCommand("sudo rm -r /home/" + user, simple=True)

    if r == 1:
        print("ERROR: Unable to delete " + user)
        return False
    else:
        print(user + " deleted")
        return True

def addUser(user):
    runCommand("sudo adduser --quiet " + user, simple=True)


def getWord(string, loc=1):
    string.replace('\t', ' ')
    string = string.split(" ")
    return string[loc-1]


def runAsAdmin():
    if os.getuid() == 0:
        return True
    else:
        return False

# File management

def getLinesFromFile(filePath):
    result = runCommand("sudo cat " + filePath)
    result = result.split("\n")
    return result

def appendToFile(filePath, data):
    runCommand("sudo echo " + data + " >> " + filePath, simple=True)