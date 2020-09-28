from . import util
from . import todolist
from . import listusers


def checkIfLightdm():
    result = util.runCommand("sudo cat /etc/X11/default-display-manager")

    if result.split("/")[-1] == "lightdm":
        return True
    else:
        return False


def deactiviteGuest(args):
    if not checkIfLightdm:
        return
    
    util.appendToFile("/etc/lightdm/lightdm.conf", "allow-guest=false")

    todolist.modifyItem("disable guest", True)


def resetPasswords(args):
    password = "Cyberpatriot2020!"

    skipUser = None

    if len(args) > 0:
        skipUser = args[0]
    
    if len(args) > 1:
        password = args[1]
    
    if len(args) > 2:
        print("ERROR: reset passwords passed to many arguments")
        return

    users = listusers.getusers()

    for user in users:
        if user == skipUser:
            continue
        util.runCommand("echo " + user + ":" + password + " | sudo chpasswd", simple=True)
        util.runCommand("echo " + user + ":" + password, simple=True)

    todolist.modifyItem("reset passwords", True)


def setPasswordPolicies(args):
    util.runCommand("sudo apt install -y libpam-cracklib")
    util.runCommand("sudo cat /bin/Config_Files/common-password > /etc/pam.d/common-password", simple=True)
    util.runCommand("sudo cat /bin/Config_Files/login.defs > /etc/login.defs", simple=True)
    todolist.modifyItem("update policies", True)

