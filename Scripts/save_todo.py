#!/usr/bin/env python3

from misc import TODO_FILE, SAVES

from os import path, mkdir
from glob import glob


def get_file_number(file_name):
    start = file_name.find('_') + 1
    end = file_name.find('.')

    return int(file_name[start : end])


def main():
    if not path.exists(SAVES):
        mkdir(SAVES)
        
    files = glob(SAVES + '/*.md')
    
    file = ''
    
    if len(files) == 0:
        file = SAVES + '/save_0.md'
    else:
        max = -1
        
        for fl in files:
            simple_name = fl.split("/")[-1]
            num = get_file_number(simple_name)
            
            if num > max:
                max = num
        
        file = SAVES + '/' + 'save_' + str(max + 1) + '.md'
        print(file)
        
    with open(TODO_FILE, 'r') as tf, open(file, 'a') as sv:
        for line in tf:
            sv.write(line)


if __name__ == '__main__':
    main()
    