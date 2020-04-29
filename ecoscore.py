#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
from nltk.tokenize import RegexpTokenizer

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
    grey = '\033[90m'
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    purple = '\033[95m'
    cyan = '\033[96m'

# Impact
#
# Represents ecological impact of practices
class Impact:
    low = "low"
    medium = "medium"
    high = "high"

scoreForImpact = {}
scoreForImpact[Impact.low] = 1
scoreForImpact[Impact.medium] = 2
scoreForImpact[Impact.high] = 3

perfectScore = 0
appScore = 0

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
        sys.exit()
    else:
        # look at arguments
        for i in range(1, len(sys.argv)):
            arg = sys.argv[i]

            if arg == "--help":
                # show detailed help
                ShowHelp(True)
                sys.exit()
            elif arg == "-v" or arg == "--verbose":
                # activate verbose mode
                global verbose
                verbose = True
            # if the directory's path is not in last position
            elif(i != len(sys.argv) - 1):
                # show help
                ShowHelp(False)
                sys.exit()
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
    fileLists["html"] = list()
    fileLists["css"] = list()

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
            # HTML files
            elif filePath.endswith(".html"):
                fileLists["html"].append(filePath)
            # CSS files
            elif filePath.endswith(".css"):
                fileLists["css"].append(filePath)
            # Add more file types here if needed
    return fileLists

# PrintImpact
#
# prints given impact to the console with the right colours
def PrintImpact(impact):
    color = Color.end
    if impact == Impact.low:
        color = Color.green
    elif impact == Impact.medium:
        color = Color.yellow
    elif impact == Impact.high:
        color = Color.red
    print(Color.end + "\t\tImpact: " + color + impact + Color.end)

# CheckPractice34
#
# Checks if there are no try ... catch ... finally
def CheckPractice34(filePath, text):
    global verbose
    global perfectScore
    global appScore

    # impact of this practice
    impact = Impact.low

    # increase the perfect score in any case
    perfectScore += scoreForImpact[impact]

    # use regex to find try ... catch ... finally
    tokenizer = RegexpTokenizer('try\s*{[^}]*}\s*(catch\s*\([\w\s]+\)\s*{[^}]*}\s*|finally\s*{[^}]*}\s*)')
    matches = tokenizer.tokenize(text)

    if len(matches) == 0:
        # there are no matches, practice is respected
        # we increase the score of the app
        appScore += scoreForImpact[impact]
        if verbose:
            print("\tPractice 34: " + Color.green + "YES" + Color.end)
    else:
        # practice isn't respected
        if verbose:
            print("\tPractice 34: " + Color.red + "NO" + Color.end + "\n\t\tThere are " + Color.bold + str(len(matches)) + Color.end + " infringements to correct:")
            # show infringements and the impact of this practice
            print(Color.grey)
            for match in matches:
                print(match + "\n")
            PrintImpact(impact)

# CheckPractice41
#
# Checks if there are no for ... in
def CheckPractice41(filePath, text):
    global verbose
    global perfectScore
    global appScore

    # impact of this practice
    impact = Impact.medium

    # increase the perfect score in any case
    perfectScore += scoreForImpact[impact]

    # use regex to find for ... in
    tokenizer = RegexpTokenizer('for\s*\([^)]* +in +[^)]*\)')
    matches = tokenizer.tokenize(text)

    if len(matches) == 0:
        # there are no matches, practice is respected
        # we increase the score of the app
        appScore += scoreForImpact[impact]
        if verbose:
            print("\tPractice 41: " + Color.green + "YES" + Color.end)
    else:
        # practice isn't respected
        if verbose:
            print("\tPractice 41: " + Color.red + "NO" + Color.end + "\n\t\tThere are " + Color.bold + str(len(matches)) + Color.end + " infringements to correct:")
            # show infringements and the impact of this practice
            print(Color.grey)
            for match in matches:
                print(match + "\n")
            PrintImpact(impact)

# CheckPracticesPHP
#
# Checks if the file at the given path respects recommended practices for server code
def CheckPracticesPHP(filePath):
    pass

# CheckPracticesJS
#
# Checks if the file at the given path respects recommended practices for client code
def CheckPracticesJS(filePath):
    global verbose
    with open(filePath, "r") as file:
        if verbose:
            print(Color.cyan + filePath + Color.end + ":")
        content = file.read()
        CheckPractice34(filePath, content)
        CheckPractice41(filePath, content)

# CheckPracticesHTML
#
# Checks if the file at the given path respects recommended practices for HTML
def CheckPracticesHTML(filePath):
    pass

# CheckPracticesCSS
#
# Checks if the file at the given path respects recommended practices for CSS
def CheckPracticesCSS(filePath):
    pass

# CheckPractices
#
# Checks practices for all files in a dictionary
def CheckPractices(fileLists):
    for lang, filePaths in files.items():
        # depending on file type, we don't check for the same practices
        if lang == "php":
            for filePath in filePaths:
                CheckPracticesPHP(filePath)
                CheckPracticesHTML(filePath) # php files can also contain html
        elif lang == "js":
            for filePath in filePaths:
                CheckPracticesJS(filePath)
        elif lang == "html":
            for filePath in filePaths:
                CheckPracticesHTML(filePath)
        elif lang == "css":
            for filePath in filePaths:
                CheckPracticesCSS(filePath)

# ShowScore
#
# Shows the perfect score (if every practice is respected) and the score the app got
def ShowScore():
    global perfectScore
    global appScore

    print("Your application got a total score of " + Color.green + str(appScore) + Color.end + " out of a possible " + Color.bold + str(perfectScore) + Color.end + ".")
    print("Percentage: " + "%.2f" % (appScore / perfectScore * 100) + "%")

ParseArguments()

files = ListFiles(appDirectory)
nPhp = len(files["php"])
nJs = len(files["js"])
nHtml = len(files["html"])
nCss = len(files["css"])
print("Found " + str(nPhp) + " PHP files, " + str(nJs) + " JS files, " + str(nHtml) + " HTML files and " + str(nCss) + " CSS files, for a total of " + str(nPhp + nJs + nHtml + nCss) + " files.")

CheckPractices(files)

ShowScore()
