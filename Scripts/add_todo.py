#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE, USAGE_ADD, INVALID_FLAG, ADD_FLAGS, exit_if, last_number

# adds a new todo at the end of the file
def add_todo(todo, marked):
    with open(TODO_FILE, 'a') as f:
        num = str(last_number() + 1)
        
        status = ''
        
        if marked:
            status = '[x]'
        else:
            status = '[ ]'
        
        new_todo = num + '. ' + status + ' ' + todo + '\n'
        
        f.write(new_todo)
    

def main():
    todo = argv[1]
    flags = argv[2:]
    
    exit_if(len(argv) < 2, USAGE_ADD)
    
    marked = False
    
    for flag in flags:
        exit_if(not ADD_FLAGS.__contains__(flag), INVALID_FLAG)
        
        if flag == '-m' or flag == '--mark':
            marked = True
    
    add_todo(todo, marked)


if __name__ == '__main__':
    main()
    