#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE, USAGE_REPLACE, INVALID_NUMBER, exit_if, last_number, check_line_number, get_number, get_status


def replace(todo_number, new_todo):
    with open(TODO_FILE, 'r+') as f:
        lines = f.readlines()
        
        f.seek(0)
        f.truncate(0)
        
        for line in lines:
            if check_line_number(line, todo_number):
                f.write(str(get_number(line)) + '. ' + '[' + get_status(line) + '] ' + new_todo + '\n')
            else:
                f.write(line)


def main():
    exit_if(len(argv) != 3, USAGE_REPLACE)

    todo_number = int(argv[1])
    exit_if(todo_number > last_number() or todo_number < 1, INVALID_NUMBER)
    
    new_todo = argv[2]
    
    replace(todo_number, new_todo)


if __name__ == '__main__':
    main()
    