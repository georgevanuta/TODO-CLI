#!/bin/bash

if [ $# -eq 0 ] 
then
    echo "[USAGE]: gotobm <TITLE>."
    exit 2
fi

DIRECTORY=`eval "./goto_bookmark.py \"$1\""`

if [ "$DIRECTORY" == "[ERROR]: Title not found in the books table." ]
then
    echo $DIRECTORY
    exit 2
fi

echo $DIRECTORY
cd $DIRECTORY
$SHELL
