from . import util
from . import todolist
import os

illegalPrograms = ["ipscan", "hashcat", "nmap", "netmap"]


def mediaScan(args):
    startDirectory = "/home"

    if args:
        if not os.path.exists(args[0]):
            print("ERROR: Invalid file path")
            return
        startDirectory = args[0]
    
    util.scanForFileOfName("*.mp3")
    util.scanForFileOfName("*.mp4")
    util.scanForFileOfName("*.jpg")
    util.scanForFileOfName("*.wav")

    todolist.modifyItem("scan media", True)


def passwordScan(args):
    
    startDirectory = "/home"

    if args:
        if not os.path.exists(args[0]):
            print("ERROR: Invalid file path")
            return
        startDirectory = args[0]
    
    util.scanForFileOfName("*password*")

    todolist.modifyItem("scan for password", True)


def programScan(args):
    pass

