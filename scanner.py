#!/usr/bin/python3

# Lucas Colias
# CECS 444
# Full Scanner

# import the tables
from statetable import *
from actiontable import *
from lookuptable import *
from rwords import *
from codes import *
from tokens import *
from output import *

# Choose the file to scan
try:
    filename = output.open_file()

    #filename = "testcase.txt"
    scanned_file = open(filename).read().strip(' ')  # read in file and strip lead/trail whitespace
except:
    exit(1)

# Here starts the main portion of the program
state = 0
token_status = ""
counter = 0
buffered = 0
id_dict = {}
final_print = ""

while counter < len(scanned_file):
    token = scanned_file[counter]  # token variable is the actual char input

    # compare the various tokens and determine state table value
    current_read = tokens.gettoken(token)

    if (statetable.gettable(state, current_read) != -1) and (actiontable.gettable(state, current_read) == 1):
        token_status = token_status + token  # token_status is the accumulated chars
        state = statetable.gettable(state, current_read)
        buffered = 0
        print(token_status + '\n')

    elif (statetable.gettable(state, current_read) == -1) and (actiontable.gettable(state, current_read) == 2):
        # Halting condition

        buffered = 1
        result = codes.getcode(lookuptable.gettable(state, current_read))
        if result == "id":
            if rwords.check_rword(token_status) == True:
                result = "reservedword"
            else:
                if token_status in id_dict:
                    id_dict[token_status] += 1
                else:
                    id_dict[token_status] = 1

        if result != "space":
            final_print += "Token Discovered is " + result + " -> " + token_status.rstrip() + '\n'
            print("Token Discovered is " + result + " -> " + token_status.rstrip() + '\n')
        state = 0
        token_status = ""  # clear the token buffer

    if buffered != 1:
        counter += 1

    else:
        buffered = 0
    # end while loop

output.output_gui('Tokens Scanned:', 'Scanner', final_print)
output.output_dict('ID Table:', 'Scanner', id_dict)
# end of program