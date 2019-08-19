#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
fileorg is a file organizer, finding duplicate files
it will store in json for further treatment
"""

import sys
import os
import pprint


if __name__ == "__main__":
    arg = sys.argv
    if len(arg) == 1:
        print("Missing argument: input file")
        sys.exit()

    fin = arg[1]
    if not os.path.exists(fin):
        print("Input file not found: " + fin)
        sys.exit()

    allfiles = dict()
    with open(fin, 'r') as fd:
        for l in fd:
            dir, file = os.path.split(l.rstrip())
            if file not in allfiles:
                allfiles[file] = [dir]
            else:
                allfiles[file].append(dir)

    #pprint.pprint(allfiles)
    for fout in allfiles:
        fullpath = os.path.join(allfiles[fout][0], fout)
        print(fullpath)
