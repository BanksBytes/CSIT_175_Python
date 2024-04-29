#!/usr/bin/env python3
# Cuyamaca College CS-119
# Your name here!
# Lab 9 ex.1 Magazine class test fixture

# Import the Magazine class
from Magazine import Magazine

subscriber_name = input("Enter subscriber name: ")
magazine_title = input("Enter magazine title: ")
months_remaining = int(input("Enter months remaining: "))

# Create an instance of a Magazine subscription
my_magazine = Magazine(subscriber_name, magazine_title, months_remaining)

# Invoke the to_string() method and display the contents of the object
print(my_magazine.to_string())
