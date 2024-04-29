#!/usr/bin/env python3
# Cuyamaca College CS-119
# Your name here!
# Lab 7 ex.2 Pizza class test fixture

from test import CheckingAccount

def main():
    account_number = input("\n\tEnter Account#: ")
    customer_name = input("\tEnter the Name on the account: ")
    customer_address = input("\tEnter the address on the account: ")

    my_checkings = CheckingAccount(account_number, customer_name, customer_address)

    deposit_amount = float(input("\tEnter the amount you want to deposit: "))
    my_checkings.deposit(deposit_amount)

    withdrawal_amount = float(input("\tEnter the amount you want to withdrawal: "))
    my_checkings.withdrawal(withdrawal_amount)

    print("\n\t" + my_checkings.to_string() + "\n")

if __name__ == "__main__":
    main()
