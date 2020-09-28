from . import util
from . import managePassword

DATA_FILE_PATH = "/etc/cyber_todo_list.txt"


class Item:

    def __init__(self, text, names, loc):
        self.Text = text
        self.Names = names
        self.status = False
        self.loc = loc

checklist = [
    Item("Update password policies        : --setpasswordpolicies", ["update policies"], 0),
    Item("Scan for password files         : --scanforpassword", ["scan for password"], 1),
    Item("Check for illegal users         : --checkusers", ["illegal users", "check for illegal users"], 2),
    Item("Check admin                     : --checkadmin", ["check admin"], 3),
    Item("Disable guest account           : --disableguest", ["disable guest"], 4),
    Item("Disable root account            : manual (--settodoitem 5)", ["disable root"], 5), # Unimplemented
    Item("Reset user passwords            : --resetpasswords", ["reset passwords"], 6),
    Item("Scan for media files            : --scanmedia", ["scan media"], 7),
    Item("Scan programs                   : --scanprograms", ["scan programs"], 8),
    Item("Turn on firewall                : --turnonfirewall", ["turn on firewall"], 9),
    Item("Reject incoming request         : --rejectincoming", ["reject incoming"], 10),
    Item("Turn on daily updates           : --setautoupdates", ["daily updates"], 11),
    Item("Enable firefox privacy settings : manual (--settodoitem 12)", ["enable firefox privacy"], 12), # Manual check required
    Item("Scan for password files         : --scanforpassword", ["scan for password"], 13)
]

def isInit():
    if util.os.path.exists(DATA_FILE_PATH):
        return True
    else:
        return False

def initList(args):
    if isInit():
        print("TODO list already initilized")
        return
    
    util.runCommand("sudo touch " + DATA_FILE_PATH, simple=True)

def printList(args):
    if not isInit():
        print("Initializing TODO LIST")
        initList("Arg")
    
    for item in checklist:
        if item.status:
            print(str(item.loc) + "  " + item.Text + ": " + u'\u2713')
        else:
            print(str(item.loc) + "  " + item.Text + ": " + u'\u2717')


def manualOveride(args):
    if not isInit():
        print("ERROR: Todo list is not initilized to initilize type \"cyber --inittodolist\"")
    if len(args) > 2:
        print("ERROR: Too many arguments passed to manual overide")

    status = args[1].lower().strip()

    if status == "yes" or status == "true" or status == "check":
        print("Setting " + getItem(args[0]).Text + " to true")
        modifyItem(args[0], True)
    elif status == "no" or status == "false" or status == "uncheck":
        modifyItem(args[0], False)
    else:
        print("ERROR: Unknown status " + status)
        return


def modifyItem(item, status):

    

    item = getItem(item)
    if not item:
        print("ERROR: Unknown item")
        return
    
    if status:
        status = "TRUE"
    else:
        status = "FALSE"

    util.appendToFile(DATA_FILE_PATH, str(item.loc) + " : " + status)

    
def getItem(item):
    try:
        i = checklist[ int(item) ]

        return i
    except:
        pass

    for i in checklist:
        for name in i.Names:
            if item.lower() == name:
                return i
    
    print(item + " is not an item on the todo list")
    return False

def updateList():
    lines = util.getLinesFromFile(DATA_FILE_PATH)

    for line in lines:
        itemId = util.getWord(line)

        if not line:
            continue

        if int(itemId.strip()) > len(checklist):
            continue

        status = None

        if util.getWord(line, 3).lower() == "true":
            status = True
        elif util.getWord(line, 3).lower() == "false":
            status = False

        if not status:
            print("ERROR: Unknown symbol result in todo list data file")
            continue

        getItem(itemId).status = status

    if not managePassword.checkIfLightdm():
        modifyItem("disable guest", True)



# To be run on load
if isInit():
    updateList()
