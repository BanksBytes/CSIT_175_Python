#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.1 Automobile class implementation



# The properties below are public by default
# a single underscore _var_name before a variable name makes it protected
# a double underscore __var_name before a variable name makes it private
#
class Automobile:
    # custom constructor. Constructors are name __init__()
    def __init__(self, vin, make, model, color):
        # set the attributes
        # Note the double underscore __ before the variable name makes them private
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__color = color

    # getter and setter methods for the various properties
    def get_vin(self):
        return self.__vin
    
    def set_vin(self, vin):
        self.__vin = vin

    def get_make(self):
        return self.__make
    
    def set_vin(self, make):
        self.__make = make

    def get_model(self):
        return self.__model
    
    def set_vin(self, model):
        self.__vin = model

    def get_color(self):
        return self.__color
    
    def set_vin(self, color):
        self.__vin = color

    # instance method
    def to_string(self):
        return "VIN: " + self.__vin + " make: " \
            + self.__make + " model: " + self.__model \
            + " color: " + self.__color
