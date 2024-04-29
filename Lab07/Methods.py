#!/usr/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 7 methods file

# methods module: custom utility functions

# Create a user-defined method to get a float value. Includes exception handling.
# Uses a try/except block to validate input. Stays in loop until valid float value
# is found

def get_float_val(prompt):
    is_num = False
    str_val = input(prompt)
    while is_num == False:
        try:
            value = float(str_val)
            is_num = True
        except:
            print(str_val + " is not a float!")
            str_val = input(prompt) # try again!
    # end while
            
    return value

# end get_float_val()


# Create a user-defined method to get an Integer value. Includes exception handling.
# Uses a try/except block to validate input. Stays in loop until valid Integer value
# is found
def get_int_val(prompt):
    is_num = False
    str_val = input(prompt)
    while is_num == False:
        try:
            value = int(str_val)
            is_num = True
        except:
            print(str_val + " is not an integer!")
            str_val = input(prompt) # try again!
    # end while
            
    return value
# end get_int_val()


# user-defined function to test if an input value is a float.

def is_float(value):
    try:
        num = float(value)
        return True # if we make it here, the conversion is successful
    except:
        return False # conversion to float failed so return false
# end is_float
    

# user-defined function to test if an input value is an Integer.

def is_int(value):
    try:
        num = int(value)
        return True # if we make it here, the conversion is successful
    except:
        return False # conversion to float failed so return false
# end is_int
    
# user-defined function that is used as a search 
def find_string(the_list, find_val):
    list_len = len(the_list)
    found = False
    index = 0
    while index < list_len and found == False:
        # convert both strings to upper case for the comparison
        if find_val.upper() == the_list[index].upper():
            return index
        index += 1
    return -1
# end find_string

# user-defined function to search for an integer

def find_int(int_list, find_val):
    list_len = len(int_list)
    found = False
    index = 0
    while index < list_len and found == False:
        if find_val() == int_list[index]:
            return index
        index += 1
    return -1


def max_value(list):
    max = list[0]
    for nextValue in list:
        if nextValue > max:
            max = nextValue
        return max