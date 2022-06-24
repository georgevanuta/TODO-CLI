#!/usr/bin/env python3

from sys import argv

from misc import exit_if,\
                 COMMANDS, INVALID_COMMAND, USAGE_HELP


def main():
    exit_if(len(argv) > 2, USAGE_HELP)
    
    if len(argv) == 1:
        print(COMMANDS)
    
    elif len(argv) == 2:
        command = argv[1]
        if command == 'todo':
            print('\
    ----todo----\n\n\
Prints all TODO\'s in mdless format.\n\n\
Has the foolowing flags:\n\
    -c or -cat == Prints in cat format.(Recommended if mdless is not installed.)')
        
        elif command == 'createtodo':
            print('\
    ----createtodo----\n\n\
Creates an empty TODO\'s file in the $TODO_FILE path.')

        elif command == 'addtodo':
            print('\
    ----addtodo----\n\n\
Takes one argument which is the new TODO description.\n\
Adds an unmarked TODO to the TODO\'s file.\n\n\
Has the following flags:\n\
    -m or --mark == Adds a TODO that is already marked.')

        elif command == 'marktodo':
            print('\
    ----marktodo----\n\n\
Takes one argument which is the number of the TODO you want to mark/unmark.\n\
If given zero arguments marks/unmarks the last TODO.\n\
Toggles the status of the corresponding TODO.')

        elif command == 'deltodo':
            print('\
    ----deltodo----\n\n\
Takes one argument which is the number of the TODO you want to delete.\n\
Deletes the coresonding TODO while maintaning an order in the TODO\'s file.')

        elif command == 'replacetodo':
            print('\
    ----replacetodo----\n\n\
Takes two arguments:\n\
The first one is the TODO number,\n\
The second is the TODO description.\n\
Replaces the line corresponding to the TODO number with the new TODO description provided.')

        elif command == 'helptodo':
            print('\
    ----helptodo----\n\n\
Takes zero or one argument:\n\
For 0 arguments lists all possible commands.\n\
For 1 argument prints the description of the command given as an argument.')

        elif command == 'searchtodo':
            print('\
    ----searchtodo----\n\n\
Takes one argument which is the keyword.\n\
Searches through all lines of the TODO\'s file and prints the lines containins the keyword.\n\
Has the following flags:\n\
    -md or --mdless   == uses mdless instead of cat for showing.\n\
    -m  or --marked   == only shows the marked TODO\'s\n\
    -u  or --unmarked == only shows the unmarked TODO\'s')    

        elif command == 'hltodo':
            print('\
    ----hltodo----\n\n\
Takes two arguments.\n\
The first one is the number of the line you want.\n\
The second one is the word you want to highlight on that line.')

        elif command == 'savetodo':
            print('\
    ----savetodo----\n\n\
Saves a snapshot in the $SAVES directory of the current TODO\'s file')

        elif command == 'cleartodo':
            print('\
    ----cleartodo----\n\n\
Deletes all marked TODO\'s.\n\n\
Has the following flags:\n\
    -s or --save == saves a current snapshot of the TODO\'s (similar to savetodo) before deleting.')

        elif command == 'loadtodo':
            print('\
    ----loadtodo----\n\n\
Loads a previous save in the current TODO\'s file.\n\n\
Has the following flags:\n\
    -s or --save == saves a current snapshot of the TODO\'s (similar to savetodo) before\n\
changing to the previous save.')
        else:
            print(INVALID_COMMAND)
          

if __name__ == '__main__':
    main()
    