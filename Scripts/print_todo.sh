#!/bin/bash

TODO_FILE="/mnt/e/Programming/ideas.md"

while getopts "c" flag
do
    case "${flag}" in
        c) cat $TODO_FILE
           exit 1;;
        *) echo "$1 is an invalid flag."
           exit 1;;
    esac
done

# mdless format

mdless $TODO_FILE