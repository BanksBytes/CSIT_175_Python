#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 7 Exercise 2, Create the student votes text data file

import random
MAGIC_NUMBER = 42
random.seed(MAGIC_NUMBER)

names = ["Alex", "Briana", "Jordan"]

with open("votes.txt", "w") as file:
    for _ in range(MAGIC_NUMBER):
        file.write(f"{names[random.randint(0, len(names)-1)]}\n")