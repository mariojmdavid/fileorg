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
        print("Missing argument: directory")
        sys.exit(1)

    basedir = arg[1]
    if not os.path.exists(basedir):
        print("Directory does not exist: " + basedir)
        sys.exit(1)

    allfiles = list()
    for rdir, sdirs, files in os.walk(basedir):
        for f in files:
            fpath = os.path.join(rdir, f)
            allfiles.append((rdir, f, 'md5'))
            print(fpath)

        for sd in sdirs:
            for f in files:
                fpath = os.path.join(rdir, f)
                allfiles.append((rdir, f, 'md5'))
                print(fpath)

    with open('flist.txt', 'w') as fd:
         for item in allfiles:
             fd.write("%s,%s,%s\n" % item)
