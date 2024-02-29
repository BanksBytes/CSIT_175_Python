#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 5 Excercise 1, Fix the syntax errors in the sample code

# Function should be terminated with a colon ":"
#def main()
def main():
    print("This is a sample program with syntax errors");
# Indentation was incorrect here    
#     x = 10
    x = 10
# Indentation in correct here
#     y = 5
    y = 5
# Indentation in correct here
#      z = 0.0
    z = 0.0

# Incorrect way to comment in Python, should lead with a "#"   
#    /* compare the two values */
#    compare the two values

# If statement should be terminated with a colon ":"
#    if x > y
    if x > y:
            print("x is the greater than y")
# Else statement should be terminated with a colon ":"
#    else
    else:
        print("y is greater than x")
# for statement should be terminated with a colon ":"    
#    for i in range(5)
    for i in range(5):
        print(i)

    input = "what's your favorite season of the year?"
# Incorrect Indentation here
#            season = input
    season = input
# Incorrect Indentation here
#            print(season)
    print(season)

# if statement should be terminated with a colon ":", also should be using a comparison operator "==" instead of the assignment operator "="        
#if __name__="__main__"
if __name__ == "__main__":
    main()