import constants
from collections import defaultdict


class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number
        self.amount = constants.STARTING_AMOUNT
        self.properties_owned = defaultdict([])
        self.position = 0

    def buy_property(self, property):
        self.properties_owned[property.colour].append(property)

    # defining getters and setters
    def get_amount(self):
        return self.amount

    # Only amount and properties are changed, so let's write setter methods for those

    def add_amount(self, num):
        self.set_amount(self.get_amount() + num)

    def set_position(self, num):
        self.position = num

    def is_bankrupt(self):
        if (self.amount < 0):
            return True
        return False
