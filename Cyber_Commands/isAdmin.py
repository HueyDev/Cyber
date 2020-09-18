from . import util

def userIsAdmin(user):
    
    global sudoGroupId

    groups = util.runCommand("id -G " + user)
    groups = groups.split(" ")

    for group in groups:
        if group == sudoGroupId:
            return True
    
    return False


sudoGroupId = util.runCommand("getent group 27")
sudoGroupId = sudoGroupId.split(":")
sudoGroupId = sudoGroupId[2]