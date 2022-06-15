#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE, USAGE_ADD, INVALID_OPTION, exit_if, last_number

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
    options = argv[1:]
    
    if len(argv) == 2:
        add_todo(todo, False)
    
    for option in options:
        if option == '-m' or option == '--mark':
            add_todo(todo, True)
    


if __name__ == '__main__':
    main()
    