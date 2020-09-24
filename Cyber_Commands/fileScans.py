from . import util
from . import todolist
import os

illegalPrograms = [
 "ipscan",
 "hashcat",
 "nmap",
 "netmap",
 "pure-ftpd",
 "vsftp",
 "proftpd",
 "glftpd"
]


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
    programs = util.runCommand("sudo apt list --installed")
    programs = programs.strip()
    programs = programs.split("\n")

    for line in programs:
        program = line.split("/")[0]
        if program in illegalPrograms:
            print("Found program " + program + " at " + line)
            if util.confirmAction("Delete program?(y/n)"):
                print("Removing")
                util.runCommand("sudo apt -y remove " + program)
                print("Purging")
                util.runCommand("sudo apt -y purge " + program)
                print("Auto removing")
                util.runCommand("sudo apt -y autoremove")
                print(program + " deleted")
    
    todolist.modifyItem("scan programs", True)

