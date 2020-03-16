#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

appDirectory = ""

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
