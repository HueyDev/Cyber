from . import util


def listusers(args):

    if not type(args) == list:
        print("ERROR: passed non list of args")
        return
    
    if args:
        print("ERROR: Unknown extra arguments after --listusers")
        return

    print("List")