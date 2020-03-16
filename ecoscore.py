#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

appDirectory = ""
verbose = False

# ShowHelp(detailed)
#
# Shows detailed help if detailed is set to true, shows brief help otherwise
def ShowHelp(detailed):
    if(detailed):
        print("\necoscore.py")
        print("\nSynopsis")
        print("\n\tpython3 ecoscore.py [OPTION]... APP_DIRECTORY")
        print("\nDescription")
        print("\n\tAnalyses and gives a score to the app located in the directory `APP_DIRECTORY`.")
        print("\n\tMandatory arguments to long options are mandatory for short options too.")
        print("\n\t`-v`, `--verbose`", "\t\tprint a message for each file analysed", sep="\n")
        print("\n\t`--help`", "\t\tdisplay help and exit", sep="\n")
    else:
        print("\nUsage")
        print("\n\tpython3 ecoscore.py [OPTION]... APP_DIRECTORY")
        print("\n\tUse option --help for detailed help.")

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
                verbose = True
            # if the directory's path is not in last position
            elif(i != len(sys.argv) - 1):
                # show help
                ShowHelp(False)
            # this is the directory's path
            else:
                appDirectory = arg

ParseArguments()
