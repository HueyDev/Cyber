from . import util
from . import listusers
from . import isAdmin


def checkAdmins(args):

    if not type(args) == list:
        print("ERROR: checkAdmins was passed non list variable")
        return
    
    users = listusers.getusers()
    
    for user in users:

        admin = isAdmin.userIsAdmin(user)

        if admin and user in args:
            #print(user + " is already an adminastrator")
            continue

        if not admin and not user in args:
            #print(user + " is already a standard user")
            continue

        if not admin and user in args:
            print(user + " is being promoted to administrator")
            util.makeUserAdmin(user)
            continue

        if admin and not user in args:
            print(user + " is being demoted to standard user")
            util.demoteUser(user) 

