#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE, USAGE_SEARCH, exit_if, get_keywords


def contains_keyword(line, keyword):
    return get_keywords(line).__contains__(keyword)


def print_lines_keyword(keyword):
    with open(TODO_FILE, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            if contains_keyword(line, keyword):
                print(line, end=" ")


def main():
    exit_if(len(argv) != 2, USAGE_SEARCH)
    
    keyword = argv[1].lower()
    
    print_lines_keyword(keyword)


if __name__ == '__main__':
    main()
    