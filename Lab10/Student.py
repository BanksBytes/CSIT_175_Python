#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.5 Student class implementation
#
from Person import Person

class Student(Person):

    def __init__(self, name, address, age, major, units):
        # Override Person construct 
        super().__init__(name, address, age)
        self.__major = major
        self.__units = units

    # getter and setters
    def get_major(self):
        return self.__major
    
    def set_major(self, major):
        self.__major

    def get_units(self):
        return self.__units
    
    def set_units(self, units):
        self.__units

    # to string
    def to_string(self):
        return super().to_string() + " Major: " + self.__major + \
            " Units: %d" % self.__units
    



