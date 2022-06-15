#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE, INVALID_OPTION, get_status, decr_line
import save_todo


def decr_line_n(line, n):
    new_line = line

    for i in range(0, n):
        new_line = decr_line(new_line)

    return new_line


def del_marked():
    with open(TODO_FILE, 'r+') as f:
        lines = f.readlines()

        f.seek(0)
        f.truncate(0)
        
        decr_counter = 0
        
        for line in lines:
            status = get_status(line)
            if status == ' ':
                f.write(decr_line_n(line, decr_counter))
            elif status == 'x':
                decr_counter += 1
            else:
                f.write(line)


def main():
    options = argv[1:]

    for option in options:
        if option == '-s' or option == '--save':
            save_todo.main()
        else:
            print(INVALID_OPTION)
            exit(2)

    del_marked()


if __name__ == '__main__':
    main()
