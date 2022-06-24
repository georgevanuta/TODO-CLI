#!/usr/bin/env python3


from misc import BOOKS_FILE, GOTO_USAGE, GOTO_USAGE, TITLE_NOT_FOUND,\
                 exit_if


from sys import argv

from os import system


def get_path(title):
    with open(BOOKS_FILE, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            path     = line.split(':')[0]
            it_title = line.split(':')[1].rstrip()
            
            if it_title == title:
                return path
            
    exit_if(True, TITLE_NOT_FOUND)



# given a title, goes to the directory where the bookmark is stored
def main():
    exit_if(len(argv) != 2, GOTO_USAGE)
    
    title = argv[1]
    print(get_path(title))


if __name__ == '__main__':
    main()
    

