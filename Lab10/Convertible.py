#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.1 Convertible class implementation



# import from the parent (base) class
from Automobile import Automobile

# The properties below are public by default
# a single underscore _var_name before a variable name makes it protected
# a double underscore __var_name before a variable name makes it private
#


class Convertible(Automobile):
    # custom constructor
    def __init__(self, vin, make, model, color, is_top_up):
        # we are overriding the Automobile constructor so call the inherited constructor
        super().__init__(vin, make, model, color)
        # add any additional code needed for the convertible constructor
        self._is_top_up = is_top_up

    # getter and setter methods for the various proerties
    def get_is_top_up(self):
        return self._is_top_up
    
    def set_is_top_up(self, _is_top_up):
        _is_top_up = _is_top_up

    # public instance method to format the status of the top up/down
    def fmt_top_status(self):
        status = "No" # set "no" by default
        if self._is_top_up == True:
            status = "Yes"
        return status
    
    # instance mthod

    def to_string(self):
        #overriding this method
        return super().to_string() \
            + "\nis top up? " + self.fmt_top_status()