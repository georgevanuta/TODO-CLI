#!/usr/bin/env python3

from os.path import exists

from misc import TODO_FILE,\
                 exit_if,\
                 FILE_EXISTS, TODO_HEADER


def main():
    exit_if(exists(TODO_FILE), FILE_EXISTS)

    open(TODO_FILE, 'x') # create file
    
    with open(TODO_FILE, 'w') as f:
        f.write(TODO_HEADER)


if __name__ == '__main__':
    main()
