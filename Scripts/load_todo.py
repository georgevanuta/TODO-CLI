#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE,\
                 max_save_number, exit_if, save_path,\
                 USAGE_LOAD, INVALID_FLAG, LOAD_FLAGS, INVALID_NUMBER

import save_todo


def load_save(save_number, should_save):
    if should_save:
        save_todo.main()
        
    save = save_path(save_number)
        
    with open(save, 'r') as sv, open(TODO_FILE, 'r+') as td:
        lines = sv.readlines()
        
        td.seek(0)
        td.truncate(0)
        
        for line in lines:
            td.write(line)


def main():
    exit_if(len(argv) < 2, USAGE_LOAD)
    
    save_number = int(argv[1])
    exit_if(save_number < 0 or save_number > max_save_number(), INVALID_NUMBER)
    
    flags = argv[2:]
    
    should_save = False
    
    for flag in flags:
        exit_if(not LOAD_FLAGS.__contains__(flag), INVALID_FLAG)
        
        if flag == '-s' or flag == '--save':
            should_save = True
            
    load_save(save_number, should_save)


if __name__ == '__main__':
    main()
    