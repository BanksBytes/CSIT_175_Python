#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.5 Person class implementation
#
class Person:

    # Constructor
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    # getter and setter
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name 

    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address

    def get_age(self):
        return int(self.__age)
    
    def set_age(self, age):
        self.__age

    def to_string(self):
        return "Name: " + self.__name + " Address: " + self.__address + \
            " Age: %d" % self.__age

