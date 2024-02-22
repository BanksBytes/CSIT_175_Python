#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 4 Excercise 2, Unit conversion utility functions

# constants
MI_PER_KM = 0.62 # Constant supplied in project specification. Do not change.
LBS_PER_KG = 2.2 # Constant supplied in project specification. Do not change.

# convert miles to kilometers

def mi_to_km(mi):
    is_num = False
    str_val = input("Enter a float numer: ")
    while is_num == False:
        try:
            value = float(str_val)
            is_num = True
        except:
            print(str_val + " is not a float!")
            str_val = input(mi) 





