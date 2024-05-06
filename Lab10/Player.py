#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.2 Player class implementation

# The properties below are public by default
# a single underscore _var_name before a variable name makes it protected
# a double underscore __var_name before a variable name makes it private
#
class Player:

    # custom constructor. Constructors are named __init__()
    def __init__(self, name, number):
        # set the attributes
        # Note the double underscore __ before the variable name makes them private
        self._name = name
        self.set_number(number) # note: call the setter method here

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name

    def get_number(self):
        return self._number
    
    def set_number(self, number):
        MIN_NUMBER = 1
        MAX_NUMBER = 999
        if number >= MIN_NUMBER and number <= MAX_NUMBER:
            self._number = number
        else:
            self._number = MIN_NUMBER

    # instance method

    def to_string(self):
        return "({0}) {1}".format(self._number, self._name)