#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 2 Excercise 1, Portrait Studio Service Calculator

# import locale for curreny formatting
import locale
locale.setlocale( locale.LC_ALL, "en-us") # for Windows
locale.setlocale(locale.LC_ALL, "en_us") # for Mac

# declare variables and constants
# constants
SURCHARGE_PCT = 1.2
SUNDAY = 1
SATURDAY = 7

# variables
base_price = 0.0
day_of_week = 0
last_name = ""
num_subjects = 0

# input
last_name = input("Enter Last Name: ")
num_subjects = int(input("How many people?: "))
day_of_week = int(input("day of week (enter 1 for Sunday, 2 for Monday..., 7 for Saturday: )"))

# process - calculate price based on number of subjects
if num_subjects == 1:
    base_price = 100
elif num_subjects ==2:
    base_price = 130
elif num_subjects == 3:
    base_price = 150