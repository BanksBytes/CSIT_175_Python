#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 3 Excercise 2, Future Value

# variables and constant
monthly_amt = 0.0
years = 0
annual_int_rate = 0.0
monthly_int_rate = 0.0
fv = 0.0
months = 0
month_num = 1

# message with python format specifiers
msg = "Month: {0:3d} FV: ${1:.2f} Interest: ${2:.2f}"
interest = 0.0
tot_interest = 0.0

# input - get monthly amt, period and interest rate
monthly_amt = float(input("Enter monthly amount: "))
annual_int_rate = float(input("Enter the Annual interest rate: "))
years = int(input("Enter the amount of years for the investment : "))

# Process
monthly_int_rate = annual_int_rate / 100 / 12
months = years * 12

while month_num <= months:
    fv += monthly_amt  # Add monthly_amt to future value    
    interest = fv * monthly_int_rate # With the new FV * the interest rate we get our interest for that month
    fv += interest  # Add interest to future value
    tot_interest += interest # Get our total interest

    print(msg.format(month_num, fv, round(interest, 2)))
    month_num += 1  




print ("\n\nTotal interest: ${0:.2f}".format(tot_interest))