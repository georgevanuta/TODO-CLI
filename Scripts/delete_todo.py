#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE,\
                 exit_if, last_number, check_line_number, decr_line,\
                 USAGE_DEL, INVALID_NUMBER


# deletes the todo and decrements 
# the todo's after the one deleted
def delete_line(todo_number):
    with open(TODO_FILE, 'r+') as f:
        lines = f.readlines()
        
        f.seek(0)
        f.truncate(0)
        
        is_before = True
        
        for line in lines:
            if not check_line_number(line, todo_number):
                if is_before:
                    f.write(line)
                else:
                    f.write(decr_line(line))
            else:
                is_before = False


def main():
    exit_if(len(argv) != 2 or not argv[1].isnumeric(), USAGE_DEL)
    
    todo_number = int(argv[1])
    exit_if(todo_number > last_number() or todo_number < 1, INVALID_NUMBER)
    
    delete_line(todo_number)    


if __name__ == '__main__':
    main()
