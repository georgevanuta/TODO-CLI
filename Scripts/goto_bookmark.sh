#!/bin/bash

DIRECTORY=`eval "./goto_bookmark.py \"$1\""`
echo $DIRECTORY
cd $DIRECTORY
$SHELL