######## MAIN .md FILE ##########
# !!   CHANGE THIS ONE TO    !! #
# !! YOUR PREFERRED LOCATION !! #
TODO_FILE = '/preferred/absolute/path/to/todos'

TODO_HEADER = '# TODO\'s\n\n'

########### Error Handlers ###########
def exit_if(bool, message):
    if bool:
        print(message)
        exit(2)


# Need it defined here.
EMPTY_FILE = '[ERROR]: Empty file.'

        
############## Helpers ##############
def last_number():
    with open(TODO_FILE, 'r') as f:
        last_line = f.readlines()[-1]
        
        num = ''
        
        for c in last_line:
            if c == '.':
                break
            if c.isdigit():
                num = num + c
                
        if len(num) == 0:
            return 0
                        
        return int(num)
    

def check_line_number(line, todo_number):
    if len(line) == 0 or not line[0].isdigit():
        return False
    
    number = ''
    
    for digit in line:
        if not digit.isdigit():
            break
        
        number += digit
        
    return int(number) == todo_number     


############ Error Messages ############
USAGE_ADD      = '[USAGE]: addtodo <TODO>.'
USAGE_DEL  	   = '[USAGE]: deltodo <TODO_NUMBER>.'
USAGE_MARK     = '[USAGE]: marktodo <TODO_NUMBER>.'
INVALID_NUMBER = '[ERROR]: Invalid number.'
FILE_EXISTS	   = '[ERROR]: File already exists at ' + TODO_FILE + '.'