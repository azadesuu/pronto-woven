from collections import defaultdict
from copy import deepcopy
from .player import Player


class Square:
    def __init__(self, name, square_type):
        self.name = name
        self.square_type = square_type

    # interface
    def action(self, player: Player):
        pass

    def get_name(self):
        return self.name

    def get_square_type(self):
        return self.square_type


class Go(Square):
    def __str__(self):
        return "Square is a %s" % (self.get_square_type())


class Property(Square):
    # class/static attribute
    property_dict = defaultdict(list)

    def __init__(self, name, square_type, price, colour):
        super().__init__(name, square_type)
        self.price = price
        self.colour = colour
        self.owner = None
        print(name, colour, price)
        self.__add_property(self)

    # defining getters
    # setters not allowed as properties do not change in the game
    def get_price(self):
        return self.price

    def get_colour(self):
        return self.colour

    def get_owner(self):
        return self.owner

    def set_owner(self, player):
        self.owner = player

    @classmethod
    def __add_property(cls, property):
        # adding properties to list
        colour = property.get_colour()
        (cls.property_dict[colour]).append(property)

    # get the length of properties based on colour in the dictionary
    def __get_colour_num(cls, colour):
        c_colour = colour.capitalize()
        return len(cls.property_dict[c_colour])

    def action(self, player):
        property_owner = self.get_owner()
        if property_owner == None:
            player.buy_property(self)
            self.set_owner(player)
            print("buy")
            return
        print("pay")
        rent = self.get_price()
        property_colour = self.get_colour()
        owner_properties = property_owner.get_properties_owned()
        if (len(owner_properties[property_colour]) == self.__get_colour_num(property_colour)):
            rent *= 2
        player.subtract_amount(rent)
        property_owner.add_amount(rent)
        return

    def __str__(self):
        return "Square is a %s with price of %d, owned by %s" % (self.get_square_type(), self.get_price(), self.get_owner().get_name())
