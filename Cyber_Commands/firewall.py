from . import util




def turnonfirewall(args):
    util.runCommand("sudo systemctl start ufw", simple=True)


def openFirewallSettings(args):
    util.runCommand("sudo gufw")








