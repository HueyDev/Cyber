from . import util
from . import todolist



def turnonfirewall(args):
    util.runCommand("sudo systemctl start ufw", simple=True)
    todolist.modifyItem("turn on firewall", True)


def rejectIncoming(args):
    util.runCommand("sudo ufw default reject incoming")
    todolist.modifyItem("reject incoming", True)


def openFirewallSettings(args):
    util.runCommand("sudo gufw")








