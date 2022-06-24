#!/usr/bin/env python3

from misc import BOOKS_FILE, BOOKMARKS_FILE, BOOKMARKS_FOUND, TITLE_USAGE,\
                 exit_if

from sys import argv

from os import path,\
               getcwd


def init_bookmarks(title):
    exit_if(path.exists(BOOKMARKS_FILE), BOOKMARKS_FOUND)
    
    with open(BOOKS_FILE, 'a') as f:
        f.write(getcwd() + '/' + ':' + title + '\n')

    with open(BOOKMARKS_FILE, 'x') as f:
        f.write('---------- ' + title + ' ----------\n')
        
    


def main():
    exit_if(len(argv) != 2, TITLE_USAGE)
    
    title = argv[1]
    init_bookmarks(title)


if __name__ == '__main__':
    main()
    