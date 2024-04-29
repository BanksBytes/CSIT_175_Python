#!/usr/bin/env python3
# Cuyamaca College CS-119
# Your name here!
# Lab 9 ex.1 Magazine class implementation


# The properties below are public by default.
# A single underscore_var_name before a variable name makes it protected.
# A double underscore_var_name before a variable name makes it private.
class Magazine:
    # Custom constructor. (Python) Constructors are named __init__()
    def __init__(self, subscriber_name, magazine_title, months_remaining):
        # Set the attributes.
        # Note the double underscore before the variable name makes them private.
        self._subscriber_name = subscriber_name
        self._magazine_title = magazine_title
        self._months_remaining = months_remaining
    
    # Getter and setter methods for the various properties.
    def get_subscriber_name(self):
        return self._subscriber_name
    
    def set_subscriber_name(self, subscriber_name):
        self._subscriber_name = subscriber_name
    
    def get_magazine_title(self):
        return self._magazine_title
    
    def set_magazine_title(self, magazine_title):
        self._magazine_title = magazine_title
    
    def get_months_remaining(self):
        return self._months_remaining
    
    def set_months_remaining(self, months_remaining):
        self._months_remaining = months_remaining
    
    # to_string() method is a commonly used method used to convert an
    # object or data type into a string representation.
    def to_string(self):
        return f"Subscriber name: {self._subscriber_name}, Title: {self._magazine_title}, {self._months_remaining} months remaining"
