#!/usr/bin/env python3

from sys import argv

from misc import TODO_FILE,\
                 exit_if, last_number, check_line_number, get_keywords,\
                 INVALID_NUMBER, USAGE_HL


def higlight_word(word, keyword):
    start = word.lower().find(keyword)
    end = len(word) - word[::-1].lower().find(keyword[::-1])

    new_word = word[:end] + '**' + word[end:]
    new_word = new_word[:start] + '**' + new_word[start:]
    
    return new_word


# highlights a given keyword in a line
def highlight_line(line, keyword):
    if get_keywords(line.lower()).__contains__(keyword):
        return line
    
    words = line.split()
    
    newline = ''
    
    n = len(words)
    
    for i in range(0, n - 1):
        if words[i].lower().__contains__(keyword):
            newline += higlight_word(words[i], keyword) + ' '
        else:
            newline += words[i] + ' '

    if (words[n - 1].lower().__contains__(keyword)):
        newline += higlight_word(words[n - 1], keyword)
    else:
        newline += words[n - 1]
        
    return newline + '\n'


def highlight(todo_number, keyword):
    with open(TODO_FILE, 'r+') as f:
        lines = f.readlines()
        
        f.seek(0)
        f.truncate(0)
        
        for line in lines:
            if check_line_number(line, todo_number):
                f.write(highlight_line(line, keyword))
            else:
                f.write(line)


def main():
    exit_if(len(argv) != 3 or not argv[1].isnumeric(), USAGE_HL)
    
    todo_number = int(argv[1])
    exit_if(todo_number > last_number() or todo_number < 1, INVALID_NUMBER)
    
    keyword = argv[2].lower()
    
    highlight(todo_number, keyword)


if __name__ == '__main__':
    main()
    