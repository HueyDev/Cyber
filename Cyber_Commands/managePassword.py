from . import util
from . import todolist



def checkIfLightdm():
    result = util.runCommand("sudo cat /etc/X11/default-display-manager")

    if result.split("/")[-1] == "lightdm":
        return True
    else:
        return False



def deactiviteGuest():
    if not checkIfLightdm:
        return
    
    util.appendToFile("/etc/lightdm/lightdm.conf", "allow-guest=false")

    todolist.modifyItem("disable guest", True)


