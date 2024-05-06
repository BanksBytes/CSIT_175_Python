#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.2 Basketball Player class implementation

# import the parent class
from Player import Player


# Declare the BaseballPlayer class and extend (inherit from) Player
class BasketballPlayer(Player):
    # custom constructor
    def __init__(self, name, number, position, free_throw_percentage):
        # we are overriding the Player constructor so call the inherited constructor
        super().__init__(name, number)
        self._position = position
        self._free_throw_percentage = free_throw_percentage

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_free_throw_percentage(self):
        return self._free_throw_percentage

    def set_free_throw_percentage(self, free_throw_percentage):
        self._free_throw_percentage = free_throw_percentage

    # instance method
    def to_string(self):
        return super().to_string() + \
               " Position: " + self._position + \
               ", Free Throw Percentage: %0.1f" % self._free_throw_percentage + "%"
