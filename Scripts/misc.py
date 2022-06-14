######## MAIN .md FILE ##########
# !!   CHANGE THIS ONE TO    !! #
# !! YOUR PREFERRED LOCATION !! #
TODO_FILE = '/preferred/absolute/path'

TODO_HEADER = '# TODO\'s\n\n'

########### Error Handlers ###########
def exit_if(bool, message):
    if bool:
        print(message)
        exit(2)


# Need it defined here.
EMPTY_FILE = '[ERROR]: Empty file.'

        
############## Helpers ##############
def get_number(line):
    number = ''
    
    for ch in line:
        if ch == '.':
            break
        
        if ch.isdigit:
            number += ch
        
        
    if len(number) == 0:
        return 0
    
    return int(number)

def get_status(line):
    for i in range(0, len(line)):
        if line[i] == '[' and i < len(line) - 1:
            return line[i + 1]
        
    return 'none'


def last_number():
    with open(TODO_FILE, 'r') as f:
        last_line = f.readlines()[-1]
                        
        return get_number(last_line)
    

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
USAGE_ADD       = '[USAGE]: addtodo <TODO>.'
USAGE_DEL  	    = '[USAGE]: deltodo <TODO_NUMBER>.'
USAGE_MARK      = '[USAGE]: marktodo <TODO_NUMBER>.'
USAGE_REPLACE   = '[USAGE]: replacetodo <TODO_NUMBER> <NEW_TODO>.'
USAGE_HELP      = '[USAGE]: helptodo | helptodo <TODO_COMMAND>'
INVALID_NUMBER  = '[ERROR]: Invalid number.'
INVALID_COMMAND = '[ERROR]: Invalid command.'
FILE_EXISTS	    = '[ERROR]: File already exists at ' + TODO_FILE + '.'

##### Commands descriptions #####
COMMANDS = '\
TODO Commands:\n\
-createtodo\n\
-addtodo\n\
-marktodo\n\
-deltodo\n\
-replacetodo\n\
-helptodo'
