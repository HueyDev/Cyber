from . import util

DATA_FILE_PATH = "/etc/cyber_todo_list.txt"


class Item:

    def __init__(self, text, names, loc):
        self.Text = text
        self.Names = names
        self.status = False
        self.loc = loc

checklist = [
    Item("Update password policies", ["update policies"], 0), # Unimplemented
    Item("Scan for password files", ["scan for password"], 1),
    Item("Check for illegal users", ["illegal users", "check for illegal users"], 2),
    Item("Check admin", ["check admin"], 3),
    Item("Disable guest account", ["disable guest"], 4), # Unimplemented
    Item("Disable root account", ["disable root"], 5), # Unimplemented
    Item("Reset user passwords", ["reset passwords"], 6), # Unimplemented
    Item("Scan for media files", ["scan media"], 7), # Unimplemented
    Item("Scan programs", ["scan programs"], 8), # Unimplemented
    Item("Turn on firewall", ["turn on firewall"], 9), # Not connected
    Item("Reject incoming request", ["reject incoming"], 10), # Unimplemented
    Item("Turn on daily updates", ["daily updates"], 11), # Unimplemented
    Item("Enable firefox privacy settings", ["enable firefox privacy"], 12) # Manual check required
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
        initList()
    
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

    if not util.runAsAdmin():
        print("ERROR: This command must be run as admin")
        return

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
        print("ERROR: NEUTRAL")
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


# To be run on load
if isInit():
    updateList()