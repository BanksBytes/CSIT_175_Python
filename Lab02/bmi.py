#!/usr/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 2 Excercise 2, calculate BMI 


# Gather Weight and Height information 
weight = int(input("Enter your weight in Pounds (Lbs): "))
height = int(input("Enter your height in Inches: "))

# Convert  Pounds and Inches to Kilograms and Meters
kilo = int(weight) / 2.2
meters = int(height) / 39.36

# Calculate the BMI and round to the nearest decimal
bmi = round(kilo / ( meters * meters),1)


# Determine what the users BMI is based off the calculated BMI variable "bmi"
if bmi <=18.5:
    print("Your BMI is", bmi, "That is considered Underweight")
elif bmi >=18.6 and bmi <=25:
    print("Your BMI is", bmi, "That is considered Normal Weight")
elif bmi > 25 and bmi <= 30:
    print("Your BMI is", bmi, "That is considered Overweight")
elif bmi > 30 and bmi <=35:
    print("Your BMI is", bmi, "That is considered Obesity (Class 1)")
elif bmi > 35 and bmi <= 40:
    print("Your BMI is", bmi, "That is considered Obesity (Class 2)")
elif bmi > 40:
    print("Your BMI is", bmi, "That is considered Morbid Obesity")