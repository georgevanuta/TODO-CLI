#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE, USAGE_ADD, exit_if, last_number

# adds a new todo at the end of the file
def add_todo(todo):
    with open(TODO_FILE, 'a') as f:
        num = str(last_number() + 1)
        new_todo = num + '. [ ] ' + todo + '\n'
        
        f.write(new_todo)
    

def main():
    exit_if(len(argv) != 2, USAGE_ADD)
        
    todo = argv[1]
    add_todo(todo)


if __name__ == '__main__':
    main()
    