from . import util
from . import todolist


def autoUpdate(args):
    util.runCommand("sudo cat /bin/Config_Files/50unattended-upgrades > /etc/apt/apt.conf.d/50unattended-upgrades")
    util.runCommand("sudo cat /bin/Config_Files/20auto-upgrades > /etc/apt/apt.conf.d/20auto-upgrades")

    todolist.modifyItem("daily updates", True)
