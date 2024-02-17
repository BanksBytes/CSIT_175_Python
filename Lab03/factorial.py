#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 3 Excercise 1, Factorial test

# variables
factorial = 0
i = 1
result = 1

# input: get factorial
factorial = int(input("Enter a number: "))

# just for fun, we'll do this with a for loop
for i in range(1, factorial + 1, 1):
    result = result * i


# output - display result
print("The result is " + str(result))
