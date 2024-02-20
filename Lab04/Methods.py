#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 4 Excercise 1, Methods

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