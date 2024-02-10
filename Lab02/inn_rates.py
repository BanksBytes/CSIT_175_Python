#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 2 Excercise 3, Determining total cost by month of stay and nights per stay

# Gather the month the user is staying and how many nights
user_month = int(input("Enter the month you are staying: "))
user_nights = int(input("Enter the number of nights you are staying: "))

# This variable will determine the cost per night based of the Conditions below
nightly_cost = 0

# Conditions to determine the cost per night based off the month the user is staying

if user_month >= 1 and user_month <=3:
    nightly_cost += 80
elif user_month >= 4 and user_month <=6:
    nightly_cost += 90
elif user_month >= 7 and user_month <= 9:
    nightly_cost += 120
elif user_month>=10 and user_month <= 12:
    nightly_cost += 100

# Calculate the total cost based on month user is staying and how many nights
total_cost = nightly_cost * user_nights


# Output for the total cost
print ("Your total cost for", user_nights, "nights is $" + str(total_cost))