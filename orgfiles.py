#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
fileorg is a file organizer, finding duplicate files
it will store in json for further treatment
"""

import sys
import os
import json


if __name__ == "__main__":
    arg = sys.argv
    if len(arg) == 1:
        print("Missing argument: input file")
        sys.exit(1)

    jsin = arg[1]
    if not os.path.exists(jsin):
        print("Input file not found: " + jsin)
        sys.exit(1)

    with open(jsin, 'r') as fd:
        allfiles = json.load(fd)

    for fl in allfiles:
        a = allfiles[fl]
        if len(a) > 5:
            print(len(a), fl, a)
