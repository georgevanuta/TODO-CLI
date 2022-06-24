#!/usr/bin/env python3

from misc import BOOKS_FILE, BOOKMARKS_FILE, BOOKMARKS_NOT_FOUND,\
                 exit_if

from os import path,\
               getcwd, remove


# search for actual file and delete it
def delete_from_directory():
    exit_if(not path.exists(BOOKMARKS_FILE), BOOKMARKS_NOT_FOUND)
    
    remove(BOOKMARKS_FILE)


# search for path in BOOKS_FILE and delete it
def delete_from_books():
    with open(BOOKS_FILE, 'r+') as f:
        file_path = getcwd() + '/'
        
        lines = f.readlines()
        
        f.seek(0)
        f.truncate(0)
        
        for line in lines:
            if line.split(':')[0] != file_path:
                f.write(line)


def main():
    delete_from_books()
    delete_from_directory()


if __name__ == '__main__':
    main()
    