#!/usr/bin/env python3
# Cuyamaca College CS-119
# Your name here!
# Lab 9 ex.2 Pizza Class Implementation

# from the module you wrote in Lab 6
import Methods as m

class Pizza:
    # these are Class Variables. They are shared by all instances of the class
    # (Note: these are parallel arrays)
    _sizes = ["Small", "Medium", "Large"]
    _prices = [8.00, 10.00, 12.00]

    # custom constructor, (Python) Constructors are named __init__()
    def __init__(self,toppings, size, quantity):
        # set/initialize the attributes
        self._price = 0.0
        self._toppings = toppings
        self._quantity = quantity
        # note: we call set_size() so we can calculate price
        self.set_size(size)

    # getter and setter methods for the various properties
    def get_toppings(self):
        return self._toppings
    
    def set_toppings(self, toppings):
        self._toppings = toppings

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        idx = m.find_string(self._sizes, size)

        # if size is vaild
        if idx >= 0:
            self._size = size
            self._price = self._prices[idx]

        # or, size wasn't found in the list
        else:
            # if the size is not found, default to small. A "better" approach would be to
            # throw an exception. We'll see that in Chapter 10
            self._size = Pizza._sizes[0] # the first entry is "Small"
            self._price = Pizza._prices[0]

    def get_quantity(self):
        return self._quantity
    
    # One reason for having setter methods is to "validate" values. It doesn't make
    # sense to have a negative quantity, so we can check and replace a negative value with 0
    def set_quantity(self, quantity):
        if quantity < 0:
            quantity = 0
        self._quantity = quantity

    # instance methods
    def calculate_price(self):
        return self._price * float(self._quantity)
    
    def to_string(self):
        # calculate an extended price which will be our total
        ext_price = self.calculate_price()
        return "qty: " + str(self._quantity) + " sz: " + self._size + \
            " with " + self._toppings + " Total: ${:.2f}".format(ext_price)
