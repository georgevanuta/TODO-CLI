#!/usr/bin/env python3

from misc import BOOKMARKS_FILE, BOOKMARKS_NOT_FOUND, DESCRIPTION_USAGE, PAGE_INT,\
                 exit_if

from sys import argv

from os import path

from datetime import date

# add a bookmark to the current bookmarks.bm file
def add_bm(page, description):
    exit_if(not path.exists(BOOKMARKS_FILE), BOOKMARKS_NOT_FOUND)

    date_created = date.today().strftime('%Y/%m/%d')
    
    with open(BOOKMARKS_FILE, 'a') as f:
        f.write(page + ':' + description + ':' + date_created + '\n')


def main():
    exit_if(len(argv) < 3, DESCRIPTION_USAGE)
    
    page = argv[1]
    exit_if(not page.isnumeric(), PAGE_INT)
    description = argv[2]
    
    add_bm(page, description)


if __name__ == '__main__':
    main()
    