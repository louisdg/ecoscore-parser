#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

appDirectory = ""
verbose = False

# Color
#
# Enables text formatting in outputs
class Color:
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    darkcyan = '\033[36m'
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    purple = '\033[95m'
    cyan = '\033[96m'

# ShowHelp(detailed)
#
# Shows detailed help if detailed is set to true, shows brief help otherwise
def ShowHelp(detailed):
    if(detailed):
        print("ecoscore.py")
        print("\n" + Color.bold + "SYNOPSIS" + Color.end)
        print("\n\t" + Color.bold + "python3 ecoscore.py" + Color.end + " [" + Color.underline + "OPTION" + Color.end + "]... " + Color.underline + "DIRECTORY" + Color.end)
        print("\n" + Color.bold + "DESCRIPTION" + Color.end)
        print("\n\tAnalyses and gives a score to the app located in DIRECTORY.")
        print("\n\tMandatory arguments to long options are mandatory for short options too.")
        print("\n\t" + Color.bold + "-v" + Color.end + ", " + Color.bold + "--verbose" + Color.end, "\t\tprint a message for each file analysed", sep="\n")
        print("\n\t" + Color.bold + "--help" + Color.end, "\t\tdisplay help and exit", sep="\n")
    else:
        print(Color.bold + "SYNOPSIS" + Color.end)
        print("\n\t" + Color.bold + "python3 ecoscore.py" + Color.end + " [" + Color.underline + "OPTION" + Color.end + "]... " + Color.underline + "DIRECTORY" + Color.end)
        print("\n\tUse option " + Color.bold + "--help" + Color.end + " for detailed help.")

# ParseArguments()
#
# Parses the arguments and sets different variables, and shows help if necessary
def ParseArguments():
    # if the program is called without any arguments
    if len(sys.argv) <= 1:
        # show help
        ShowHelp(False)
    else:
        # look at arguments
        for i in range(1, len(sys.argv)):
            arg = sys.argv[i]

            if arg == "--help":
                # show detailed help
                ShowHelp(True)
            elif arg == "-v" or arg == "--verbose":
                # activate verbose mode
                global verbose
                verbose = True
            # if the directory's path is not in last position
            elif(i != len(sys.argv) - 1):
                # show help
                ShowHelp(False)
            # this is the directory's path
            else:
                global appDirectory
                appDirectory = arg

# ScanFiles
#
# Iterates over all files and subdirectories located in dirPath
def ListFiles(dirPath):
    fileLists = {}
    fileLists["php"] = list()
    fileLists["js"] = list()

    for subdir, dirs, files in os.walk(dirPath):
        for file in files:
            #print os.path.join(subdir, file)
            filePath = subdir + os.sep + file

            # PHP files
            if filePath.endswith(".php"):
                fileLists["php"].append(filePath)
            # JavaScript files
            elif filePath.endswith(".js"):
                fileLists["js"].append(filePath)
    return fileLists

ParseArguments()

files = ListFiles(appDirectory)
print("Found " + str(len(files["php"])) + " PHP files and " + str(len(files["js"])) + " JS files, for a total of " + str(len(files["php"]) + len(files["js"])) + " files.")
if verbose:
    for lang, filePaths in files.items():
        print(lang + ":")
        for filePath in filePaths:
            print("\t" + filePath)
