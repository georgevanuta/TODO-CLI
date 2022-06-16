######## MAIN .md FILE ##########
# !!   CHANGE THIS ONES TO    !! #
# !! YOUR PREFERRED LOCATION !! #
TODO_FILE = ''
SAVES     = ''
SCRIPTS   = '' # This is the directory of this file

if len(TODO_FILE) == 0 or len(SAVES) == 0 or len(SCRIPTS) == 0:
    print('Please assign a path to the TODO_FILE, SAVES, SCRIPTS variables from --misc.py--.')


#### Header ####
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


def get_keywords(line):
    keywords = []
    
    i = 0
    
    while i < len(line):
        if i < len(line) - 2 and line[i : i + 2] == '**':
            
            i += 2
            keyword = ''
            
            while i < len(line) - 2 and not line[i : i + 2] == '**':

                keyword += line[i]
                i += 1

            i += 2
            
            if not len(keyword) == 0:
                keywords.append(keyword.lower())
                
        i += 1
            
    return keywords


def decr_line(line):
    number = ''
    
    for digit in line:
        if not digit.isdigit():
            break
        
        number += digit
        
    if len(number) == 0:
        return line
    
    
    new_number = str(int(number) - 1)
    
    return new_number + line[len(number):]



############ Error Messages ############
USAGE_ADD       = '[USAGE]: addtodo <TODO>.'
USAGE_DEL  	    = '[USAGE]: deltodo <TODO_NUMBER>.'
USAGE_MARK      = '[USAGE]: marktodo <TODO_NUMBER>.'
USAGE_REPLACE   = '[USAGE]: replacetodo <TODO_NUMBER> <NEW_TODO>.'
USAGE_HELP      = '[USAGE]: helptodo | helptodo <TODO_COMMAND>'
USAGE_SEARCH    = '[USAGE]: searchtodo <KEYWORD>.'
USAGE_HL        = '[USAGE]: hltodo <TODO_NUMBER> <KEYWORD>.'

INVALID_NUMBER  = '[ERROR]: Invalid number.'
INVALID_COMMAND = '[ERROR]: Invalid command.'
INVALID_OPTION  = '[ERROR]: Invalid option.'
FILE_EXISTS	    = '[ERROR]: File already exists at ' + TODO_FILE + '.'

### OPTIONS ###
SEARCH_FLAGS = ['-md', '--mdless',\
                '-m', '--marked',\
                '-u', '--unmarked']

ADD_FLAGS    = ['-m', '--mark']

CLEAR_FLAGS  = ['-s', '--save']


AUX_FILE = SCRIPTS + '/aux_search.md'

TODO = '[TODO]: Not yet completed.'

##### Commands descriptions #####
COMMANDS = '\
    ----TODO Commands----\n\n\
-createtodo\n\
-addtodo\n\
-marktodo\n\
-deltodo\n\
-replacetodo\n\
-searchtodo\n\
-helptodo\n\
-hltodo\n\
-savetodo\n\
-cleartodo'
