from . import util
from . import listusers
from . import admin
from . import todolist


def checkAdmins(args):

    if not type(args) == list:
        print("ERROR: checkAdmins was passed non list variable")
        return

    users = listusers.getusers()

    for u in args:
        if not u in users:
            print("ERROR: " + u + " is an invalid username")
            return

    if len(args) < 1:
        print("Warning you have selected no users as admins. Should you continue you could be permenatly locked out of admin rights redering the os useless")
        if not util.confirmAction():
            return
    
    for user in users:

        isAdmin = admin.userIsAdmin(user)

        if isAdmin and user in args:
            #print(user + " is already an adminastrator")
            continue

        if not isAdmin and not user in args:
            #print(user + " is already a standard user")
            continue

        if not isAdmin and user in args:
            print(user + " is being promoted to administrator")
            util.makeUserAdmin(user)
            continue

        if isAdmin and not user in args:
            print(user + " is being demoted to standard user")
            util.demoteUser(user) 

    todolist.modifyItem("check admin", True)


def checkUsers(args):

    if not type(args) == list:
        print("ERROR: checkUsers was passed nonlist variable")
        return

    users = listusers.getusers()

    for user in args:
        if not user in users:
            print(user + " is an invalid username")
            if util.confirmAction("Create user account for " + user + " (y/n) "):
                util.addUser(user)
                users.append(user)
            else:
                print("Skipping " + user)
                args.remove(user)



    for user in users:
        if not user in args:
            print(user + " is an invalid user.")
            if not util.confirmAction(message="Confirm delete(y/n) "):
                print("Skipping " + user)
            else:
                util.deleteUser(user)
        else:
            pass

    todolist.modifyItem("illegal users", True)
