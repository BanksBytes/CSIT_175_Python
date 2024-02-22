#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 4 Excercise 1, Method test fixture

# import the methods file. Make sure this matches the name of your file EXACTLY!
import Methods as m

# define a main() method
def main():
    # test the get_float_val() method
    float_val = m.get_float_val("Enter a floating point number: ")
    print("Float value " + str(float_val) + " was entered.")

    # test the int_float_val() method
    int_val = m.get_int_val("Enter Integer: ")
    print("Integer value " + str(int_val) + " was entered.")

    # test is_float()
    str_val = input("Enter a float:" )
    result = m.is_float(str_val)
    if result == True:
        print(str_val + " is a float.")
    else:
        print( str_val + " is NOT a float.")



    # test is_int()
    str_val = input("Enter an Integer:" )
    result = m.is_int(str_val)
    if result == True:
        print(str_val + " is an Integer.")
    else:
        print( str_val + " is NOT an Integer.")


    # test find_string()
    # Create a list of random stuff. Let's vary the letter case to test
    # note the list is in square brackets. Strings are in quotes and
    # separated by commas
    
    my_list = ["goat", "ZEBRA", "HorsE", "foX", "dog", "Cat"]
    value = input("Enter a value to find: ")
    i = m.find_string(my_list, value)
    # did we find what we are looking for
    if i >= 0:
        print("Found " + value + " at index: " + str(i) )
    else:
        print( value + " NOT FOUND!")

    # test find_string()
    # Create a list of random stuff. Let's vary the letter case to test
    # note the list is in square brackets. Strings are in quotes and
    # separated by commas
    
    my_list = [56, 6, 54, 789, 3, 99]
    value = int(input("Enter an Integer to find: "))
    i = m.find_int(my_list, value)
    # did we find what we are looking for
    if i >= 0:
        print("Found " + str(value) + " at index: " + str(i) )
    else:
        print( str(value) + " NOT FOUND!")




if __name__ == "__main__":
    main()