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

    allfiles = dict()
    for rdir, sdirs, files in os.walk(basedir):
        for f in files:
            fpath = os.path.join(rdir, f)
            if f not in allfiles:
                allfiles[f] = [rdir]
            else:
                allfiles[f].append(rdir)

        for sd in sdirs:
            for f in files:
                fpath = os.path.join(rdir, f)
                if f not in allfiles:
                    allfiles[f] = [rdir]
                else:
                    allfiles[f].append(rdir)

    with open('flist.json', 'w') as fd:
        json.dump(allfiles,fd)
