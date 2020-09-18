from . import util
from . import isAdmin


def printUsers(users):

    for user in users:
        admin = "Standard Account"
        if isAdmin.userIsAdmin(user):
            admin = "Administrator Account"
        print(" - " + user + " : " + admin)


def listusers(args):

    if not type(args) == list:
        print("ERROR: passed non list of args")
        return
    
    if args:
        print("ERROR: Unknown extra arguments after --listusers")
        return

    users = util.runCommand("ls /home", simple=False)
    users = users.strip()
    users = users.split("\n")
    for u in users:
        _ , returncode = util.runCommand("id -u " + u, simple=False, returncode=True)

        if returncode == 1:
            users.remove(u)

    printUsers(users)
        