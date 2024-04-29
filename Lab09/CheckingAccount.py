#!/usr/bin/env python3
# Cuyamaca College CS-119
# Your name here!
# Lab 9 ex.3 Checking Account Class Implementation

class CheckingAccount:
 
    # Constructor
    def __init__(self, account_number, customer_name, customer_address, account_balance=0.0):
        self._account_number = account_number
        self._customer_name = customer_name
        self._customer_address = customer_address
        self._account_balance = account_balance

    # Getter and setter methods
    def get_account_number(self):
        return self._account_number
    
    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_customer_name(self):
        return self._customer_name
    
    def set_customer_name(self, customer_name):
        self._customer_name = customer_name

    def get_customer_address(self):
        return self._customer_address
    
    def set_customer_address(self, customer_address):
        self._customer_address = customer_address

    def get_account_balance(self):
        return self._account_balance
    
    def set_account_balance(self, account_balance):
        self._account_balance = account_balance

    # Methods 
    def deposit(self, amount):
        self._account_balance += amount


    def withdrawal(self, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
        else:
            print("Insufficient funds")


    def to_string(self):
        return f"Account #: {self._account_number}\n\tCustomer Name: {self._customer_name}\n\tCustomer Address: {self._customer_address}\n\tAccount Balance: ${self._account_balance:.2f}"