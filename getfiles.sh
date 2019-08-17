#!/bin/bash

if [ -z $1 ]
then
    echo "Directory not given"
    exit 1
fi

find ${1} -type f > files.txt
