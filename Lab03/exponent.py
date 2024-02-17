#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 3 Excercise 1, While loop demo definite loop with a fixed number of iterations

# variables and constants

number = 0
exponent = 0

# input - get number and exponent
number = int(input("Enter a number: "))
exponent = int(input("Enter the exponent: "))
i = 0
result = 1

# Make sure the loop body code is intended 4 spaces!
# Also, note the colon (:)
# The Ctrl c key combination will break you out of an endless loop
# Print to the console

while i < exponent:
    result = result * number 
    i += 1 # Be sure to change the loop control variable

print("The result is " + str(result))
