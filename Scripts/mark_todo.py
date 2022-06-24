#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE,\
                 exit_if, last_number, check_line_number,\
                 USAGE_MARK, INVALID_NUMBER


# toggles the status of a line
def mark_line(line):
    todo_status = ''
    
    for i in range(0, len(line)):
        if line[i] == '[':
            if line[i + 1] == ' ':
                return line[:i + 1] + 'x' + line[i + 2:] # mark
            else:
                return line[:i + 1] + ' ' + line[i + 2:] # unmark
                
    return line # unsuccessful


# marks the line with the line number
# given as an argument
def mark(todo_number):
    with open(TODO_FILE, 'r+') as f:
        lines = f.readlines()
        
        f.seek(0)
        f.truncate(0)
        
        
        for line in lines:
            if not check_line_number(line, todo_number):
                f.write(line)
            else:
                f.write(mark_line(line))


def main():
    if len(argv) == 1:
        mark(last_number())
        exit(0)
    
    exit_if(len(argv) != 2 or not argv[1].isnumeric(), USAGE_MARK)
        
    todo_number = int(argv[1])
    exit_if(todo_number > last_number() or todo_number < 1, INVALID_NUMBER)
    
    mark(todo_number)


if __name__ == '__main__':
    main()
    