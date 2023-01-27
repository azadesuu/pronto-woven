from .constants import *
from collections import defaultdict


class Player:
    def __init__(self, name, player_number):
        self.__name = name
        self.__player_number = player_number
        self.__amount = STARTING_AMOUNT
        self.__properties_owned = defaultdict(list)
        self.__position = 0

    # defining getters and setters

    def set_amount(self, num):
        self.__amount = num

    def get_player_number(self):
        return self.__player_number

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_properties_owned(self):
        return self.__properties_owned

    def get_position(self):
        return self.__position

    # Only amount and properties are changed, so let's write setter methods for those
    def add_amount(self, num):
        self.set_amount(self.get_amount() + num)

    def subtract_amount(self, num):
        self.set_amount(self.get_amount() - num)

    def set_position(self, num):
        self.__position = num

    def buy_property(self, property):
        # assumes that the property is owned even if the player is bankrupt
        self.subtract_amount(property.get_price())
        self.__properties_owned[property.colour].append(property)

    def is_bankrupt(self):
        if (self.get_amount() < 0):
            return True
        return False

    def __str__(self):
        return "Player %s is at %d with $%d" % (self.get_name(), self.get_position(), self.get_amount())
