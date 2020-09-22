from . import util
import os


def mediaScan(args):
    pass


def passwordScan(args):
    
    startDirectory = "/home"

    if args:
        if not os.path.exists(args[0]):
            print("ERROR: Invalid file path")
            return
        startDirectory = args[0]
    
    util.scanForFileOfName("*password*")


def programScan(args):
    pass

