#!/usr/bin/env python3
# Cuyamaca College CS-119
# Your name here!
# Lab 7 ex.2 Pizza class test fixture

from Pizza import Pizza

toppings = input("\n\tEnter toppings: ")
sz = input("\tEnter size (Small, Medium, Large): ")
qty = input("\tEnter quantity: ")

# Create an instance of the Pizza class
my_pizza = Pizza(toppings, sz, qty)
print("\n\t" + my_pizza.to_string() + "\n")
