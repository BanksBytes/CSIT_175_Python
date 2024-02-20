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

    # you'll add your code below this to test the various other methods


# if this is the main module, then execture main()

if __name__ == "__main__":
    main()