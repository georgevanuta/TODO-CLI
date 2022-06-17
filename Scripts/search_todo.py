#!/usr/bin/env python3

from sys import argv
from os import system

from misc import TODO_FILE, AUX_FILE,\
                 exit_if, get_keywords, get_status,\
                 USAGE_SEARCH, SEARCH_FLAGS, INVALID_FLAG


def contains_keyword(line, keyword):
    return get_keywords(line).__contains__(keyword)


def print_lines_keyword(keyword, format_md, status):
    with open(TODO_FILE, 'r') as f:
        lines = f.readlines()
        
        with open(AUX_FILE, 'x') as g:
            if status == '':
                for line in lines:
                    if contains_keyword(line, keyword):
                        g.write(line)
            else:
                for line in lines:
                    if contains_keyword(line, keyword) and get_status(line) == status:
                        g.write(line)

    if format_md:
        system('mdless ' + AUX_FILE)
    else:
        system('cat ' + AUX_FILE)

    system('rm ' + AUX_FILE)


def main():
    exit_if(len(argv) < 2, USAGE_SEARCH)
    
    flags = argv[2:]
    
    keyword = argv[1].lower()
    
    format_md = False
    status = ''
    
    for flag in flags:
        exit_if(not SEARCH_FLAGS.__contains__(flag), INVALID_FLAG)
        
        if flag == '-md' or flag == '--mdless':
            format_md = True
        elif flag == '-m' or flag == '--marked':
            status = 'x'
        elif flag == '-u' or flag == '--unmarked':
            status = ' '
            
    print_lines_keyword(keyword, format_md, status)

if __name__ == '__main__':
    main()
