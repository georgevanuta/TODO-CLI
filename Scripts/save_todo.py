#!/usr/bin/env python3

from misc import TODO_FILE, SAVES, max_save_number, save_path


def main():
    file = save_path(max_save_number() + 1)
    print(file)
        
    with open(TODO_FILE, 'r') as tf, open(file, 'a') as sv:
        for line in tf:
            sv.write(line)


if __name__ == '__main__':
    main()
    