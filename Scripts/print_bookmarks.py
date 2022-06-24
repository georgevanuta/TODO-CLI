#!/usr/bin/env python3

from misc import BOOKS_FILE, FLAGS_PRINT, BOOKMARKS_FILE, BOOKMARKS_NOT_FOUND,\
                 HEADER_ALL_BOOKS, HEADER_LEN_SPACES, LINE_TABLE,\
                 exit_if, flag_message

from sys import argv

from os import path


# lists all directories with a bookmarks.bm file
def all_bookmarks():
    print(LINE_TABLE)
    print(HEADER_ALL_BOOKS)
    print(LINE_TABLE)

    with open(BOOKS_FILE, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            path = line.split(':')[0]
            book = line.split(':')[1].rstrip()
            path_spaces_len = HEADER_LEN_SPACES - len(path)
            book_spaces_len = HEADER_LEN_SPACES - len(book)
            
            print('|' + path + path_spaces_len * ' ' + '|' + book + book_spaces_len * ' ' + '|')
            print(LINE_TABLE)
            
            


# lists all bookmarks from current directory
def current_bookmarks():
    exit_if(not path.exists(BOOKMARKS_FILE), BOOKMARKS_NOT_FOUND)
        
    with open(BOOKMARKS_FILE, 'r') as f:
        print(f.read())


def main():
    flags = argv[1:]

    if len(flags) == 0: # print current directory bookmarks
        current_bookmarks()
    else:               # process flags
        for flag in flags:
            exit_if(not FLAGS_PRINT.__contains__(flag), flag_message(flag)) # exit if invalid flag
            
            if flag == '-a' or flag == '--all': # print all bookmarks from all directories
                all_bookmarks()


if __name__ == '__main__':
    main()
    