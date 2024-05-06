#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.2 Baseball Player class implementation

# import the parent class
from Player import Player


# Declare the BaseballPlayer class and extend (inherit from) Player
class BaseballPlayer(Player):
    # custom constructor
    def __init__(self, name, number, position, batting_avg):
        # we are overriding the Player constructor so call the inherited constructor
        super().__init__(name, number)
        self._position = position
        self._batting_avg = batting_avg

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_battingAvg(self):
        return self._batting_avg

    def set_battingAvg(self, batting_avg):
        self._batting_avg = batting_avg

    # instance method
    def to_string(self):
        return super().to_string() + \
               " Position: " + self._position + \
               ", Batting Average: %0.3f" % self._batting_avg
