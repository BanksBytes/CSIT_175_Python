#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.2 Player class test fixtures

# import the BaseballPlayer class
from BaseballPlayer import BaseballPlayer
from BasketballPlayer import BasketballPlayer

print("\nBaseball:")
name = input("Enter name: ")
number = int(input("Enter number: "))
position = input("Enter position: ")
average = float(input("Enter batting average: "))

# create an instance of a baseball player
my_baseball_player = BaseballPlayer(name, number, position, average)

# invoke the to_string() method to display object detail
print(my_baseball_player.to_string())


print("\nBasketball:")

name = input("Enter name: ")
number = int(input("Enter number: "))
position = input("Enter position: ")
free_throw_percentage = float(input("Enter Free Throw Percentage: "))

# create an instance of a basketball player
my_basketball_player = BasketballPlayer(name, number, position, free_throw_percentage)

# invoke the to_string() method to display object detail
print(my_basketball_player.to_string())