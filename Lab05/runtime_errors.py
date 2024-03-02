#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 5 Excercise 2, Runtime error sample code

import random

def add( a, b ):
    return a + b

def multiply(a, b ):
    return a * b

def square( a ):
    return a * a

def main():
    x = 10
# In order for "z" to have a value y cannot equal zero because you cannot divide by 0
#    y = 0
    y = 5
    z = x / y
# Unable to concatenate a string with a number, need to change the value of "z" to a string
#    print("Value of z = " + z)
    print("Value of z = " + str(z))

# "w" was not a defined variable
#    print(f"{w} ---> {x} ---> {y}")
    print(f"{x} ---> {y}")

#    Tried to set an integer to a string value
#    int_value = int("abc")
    int_value = str("abc")


#    print( square(random.getrandom(10) ))
    print( square(random.randint(1 , 10) ))  

# add fucntion needed two values
#   print(add(1))     
    print(add(1, 15))

# square needed one value instead of two
#   x = square( 2, 3 ) 
    x = square(3)
    print( x )
# None can not be used as a variable
   #None = 10
    None_Var = 10

    print("The value of x is: %s" % int_value)

if __name__=="__main__":
    main()