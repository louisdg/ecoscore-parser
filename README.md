# ecoscore-parser

Ecoscore is a program that scans through a web app directory and analyses files of code.

It judges the app's eco-friendliness by looking at common recommended practices for resource saving.

It will give a score to the app depending on how much it respects these practices.

## Requirements

* `python3`

## Usage

### Synopsis

```
python3 ecoscore.py [OPTION]... DIRECTORY
```

### Description

Analyses and gives a score to the app located in `DIRECTORY`.

Mandatory arguments to long options are mandatory for short options too.

* `-v`, `--verbose`
  print a message for each file analysed

* `--help`
  display help and exit
