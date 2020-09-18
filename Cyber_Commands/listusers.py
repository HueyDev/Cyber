from . import util


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
        util.runCommand("id -u " + u, simple=True)
        result = util.runCommand("echo $?", simple=False)
        if result == "1":
            users.remove(u)
    print(users)