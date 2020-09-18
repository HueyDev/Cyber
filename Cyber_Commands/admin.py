from . import util

# Global Variables
sudoGroupId = None
rootAccounts = []

def userIsAdmin(user):
    
    global sudoGroupId

    if user in rootAccounts:
        return True

    groups = util.runCommand("id -G " + user)

    groups = groups.split(" ")

    for group in groups:
        group = group.strip()

        if group == sudoGroupId:

            return True

    return False


def isAdmin(args):
    if userIsAdmin(args[0]):
        print(args[0] + " is an ADMINISTRATOR")
    else:
        print(args[0] + " is a STANDARD USER")

sudoGroupId = util.runCommand("getent group 27")
sudoGroupId = sudoGroupId.split(":")
sudoGroupId = sudoGroupId[2]
sudoGroupId = sudoGroupId.strip()

sudoersFile = util.runCommand("sudo cat /etc/sudoers")

sudoersFile = sudoersFile.split("\n")

for line in sudoersFile:
    line.strip()

    if not line:
        continue

    line.replace("    ", '\t')

    if line[0] == "#" or line[0] == "%":
        continue
    
    if line[0:7] == "Default":
        continue
    
    line = line.split("\t")

    if line[0] == "Default":
        continue

    rootAccounts.append(line[0])

