#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.1 Convertible class implementation



# import from the parent (base) class
from Automobile import Automobile

# The properties below are public by default
# a single underscore _var_name before a variable name makes it protected
# a double underscore __var_name before a variable name makes it private
#


class Racecar(Automobile):
    # custom constructor
    def __init__(self, vin, make, model, color, horse_power):
        # we are overriding the Automobile constructor so call the inherited constructor
        super().__init__(vin, make, model, color)
        # add any additional code needed for the convertible constructor
        self._horse_power = horse_power

    # getter and setter methods for the various proerties
    def get_horse_power(self):
        return int(self._horse_power)
    
    def set_horse_power(self, _horse_power):
        _horse_power = int(_horse_power)

    # # public instance method to format the status of the top up/down
    # def fmt_top_status(self):
    #     status = "No" # set "no" by default
    #     if self._horse_power == True:
    #         status = "Yes"
    #     return status
    
    # instance method

    def to_string(self):
        #overriding this method
        return super().to_string() \
            + "\nHorse Power: " + self._horse_power