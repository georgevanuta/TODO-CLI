#!/usr/bin/env python3

from sys import argv

from misc import COMMANDS, INVALID_COMMAND, USAGE_HELP, exit_if


def main():
    exit_if(len(argv) > 2, USAGE_HELP)
    
    if len(argv) == 1:
        print(COMMANDS)
    
    elif len(argv) == 2:
        command = argv[1]
        
        if command == 'createtodo':
            print('Creates an empty TODO\'s file in the $TODO_FILE path.')
        elif command == 'addtodo':
            print('Takes one argument which is the new TODO description.\n\
Adds an unmarked TODO to the TODO\'s file.')
        elif command == 'marktodo':
            print('Takes one argument which is the number of the TODO you want to mark/unmark.\n\
Toggles the status of the corresponding TODO.')
        elif command == 'deltodo':
            print('Takes one argument which is the number of the TODO you want to delete.\n\
Deletes the coresonding TODO while maintaning an order in the TODO\'s file.')
        elif command == 'replacetodo':
            print('Takes two arguments:\n\
The first one is the TODO number,\n\
The second is the TODO description.\n\
Replaces the line corresponding to the TODO number with the new TODO description provided.')
        elif command == 'helptodo':
            print('Takes zero or one argument:\n\
For 0 arguments lists all possible commands.\n\
For 1 argument prints the description of the command given as an argument.')
        elif command == 'searchtodo':
            print('Takes one argument which is the keyword.\n\
Searches through all lines of the TODO\'s file and prints the lines containins the keyword.')    
        
        else:
            print(INVALID_COMMAND)
          

if __name__ == '__main__':
    main()
    