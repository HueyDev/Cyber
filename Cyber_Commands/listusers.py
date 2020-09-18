from . import util
from . import isAdmin


def printUsers(users):

    for user in users:
        admin = "Standard Account"
        if isAdmin.userIsAdmin(user):
            admin = "Administrator Account"
        print(" - " + user + " : " + admin)


def getusers():
    users = util.runCommand("ls /home", simple=False)
    users = users.strip()
    users = users.split("\n")
    for u in users:
        _ , returncode = util.runCommand("id -u " + u, simple=False, returncode=True)

        if returncode == 1:
            users.remove(u)

    return users


def listusers(args):

    if not type(args) == list:
        print("ERROR: passed non list of args")
        return
    
    if args:
        print("ERROR: Unknown extra arguments after --listusers")
        return
    
    users = getusers()

    users.sort()
    printUsers(users)


def listallusers(args):

    if not type(args) == list:
        print("ERROR: passed non list of args")
        return
    
    if args:
        print("ERROR: Unknown extra arguments after --listallusers")
        return
    
    tusers = util.runCommand("cat /etc/passwd")
    tusers = tusers.split("\n")

    users = []

    for line in tusers:
        if not line:
            continue
        data = line
        data = data.replace("::", ":")
        data = line.split(":")
        users.append(data[0])

    printUsers(users)
