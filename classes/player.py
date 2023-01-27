from .constants import *
from collections import defaultdict


class Player:
    def __init__(self, name, player_number):
        """
        Initialises a Player object

        Args:
            name (String): Player name
            player_number (int): Player number (the order that players play in)
        """
        # player's name
        self.__name = name
        # the order that players play in
        self.__player_number = player_number
        # player's starting amount and position
        self.__amount = STARTING_AMOUNT
        self.__position = STARTING_POSITION
        # player's owned properties
        self.__properties_owned = defaultdict(list)

    # Class getters and setters
    def set_amount(self, num):
        """
        Sets the amount of moneys that a Player has

        Args:
            num (int): Amount to set the player's money to
        """
        self.__amount = num

    def get_player_number(self):
        """
        Returns the player number (that is, the order that players play in)

        Returns:
            int: The player number
        """
        return self.__player_number

    def get_name(self):
        """
        Returns the player name

        Returns:
            str: The player's name
        """
        return self.__name

    def get_amount(self):
        """
        Returns the player's money amount

        Returns:
            int: The player's money amount
        """
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
