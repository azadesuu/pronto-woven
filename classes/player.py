from .constants import *
from collections import defaultdict


class Player:
    """
    A Player is a participant in the Woven Monopoly simulation

    :param __name: The player's name. May include spaces
    :type __name: str
    :param __player_number: The player's number (the other that players play
        in). Starts from 0
    :type __player_number: int
    :param __amount: The player's amount/money on hand. The default amount can
        be set in constants.py, but cannot be equal or less than 0 else
        the game will end immediately
    :type __amount: int
    :param __position: The player's current position. The default position can
        be set in constants.py, but cannot be equal or more
        than the number of Squares
    :type __position: int
    :param __properties_owned: The properties that the player currently owns
    :type __properties_owned: dict
    """

    def __init__(self, name, player_number):
        """Initialises a Player object

        : param name: Player name
        : type name: str
        : param player_number: Player number (the order that players play in )
        : type player_number: int
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

    # ------------- Class getters and setters
    def get_player_number(self):
        """Returns the player number (that is , the order that players play in )

        :return: The player number
        :rtype: int
        """
        return self.__player_number

    def get_name(self):
        """Returns the player name

        :return: The player's name
        :rtype: str
        """
        return self.__name

    def get_amount(self):
        """Returns the player's money amount

        :return: The player's money amount
        :rtype: int
        """
        return self.__amount

    def get_properties_owned(self):
        """Information about the player's owned properties

        :return: The player's owned properties
        :rtype: dict
        """
        return self.__properties_owned

    def get_position(self):
        """The player's current position on the board

        :return: The player's position
        :rtype: int
        """
        return self.__position

    def set_amount(self, num):
        """
        Sets the amount of moneys that a Player has

        :param num: Amount to set the player's money to
        :type num: int
        """
        self.__amount = num

    # ------------- Class methods
    def add_amount(self, num):
        """
        Adds the given amount to the player's money

        :param num: The amount to add to the player's money
        :type num: int
        """
        self.set_amount(self.get_amount() + num)

    def subtract_amount(self, num):
        """Subtracts the given amount from the player's money

        :param num: The amount to subtract from the player's money
        :type num: int
        """
        self.set_amount(self.get_amount() - num)

    def set_position(self, num):
        """Sets the position of the player to the given number

        :param num: The player's new position
        :type num: int
        """
        self.__position = num

    def buy_property(self, property):
        """Called when the property is to be owned by the player

        :param property: An unowned property object
        :type property: Property
        """
        # assumes that the property is owned even if the player is bankrupt
        self.subtract_amount(property.get_price())
        self.__properties_owned[property.get_colour()].append(property)

    def is_bankrupt(self):
        """Returns true if the player has less than or equal to bankruptcy
        amount

        :return: True if the player has 0 dollars or less, else False.
        :rtype: bool
        """
        if self.get_amount() <= BANKRUPTCY_AMOUNT:
            return True
        return False

    def __str__(self):
        """A dunder method that provides information about the class object
        with a String

        :return: Information about the class object (name, position, amount)
        :rtype: str
        """
        return "Player %s is at %d with $%d" % (
            self.get_name(),
            self.get_position(),
            self.get_amount(),
        )
