from copy import deepcopy
from player import Player


class Square:
    def __init__(self, name, square_type):
        self.name = name
        self.square_type = square_type

    def action(player: Player):
        # empty
        pass


class Go(Square):
    # def __init__(self, name, square_type):
    #     super.__init__(name, square_type)

    def action(player: Player):
        player.add_amount(1)


class Property(Square):
    def __init__(self, name, square_type, price, colour):
        super.__init__(name, square_type)
        self.price = price
        self.colour = colour
        self.owner = -1

    # defining getters
    # setters not allowed as properties do not change in the game
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_colour(self):
        return self.colour

    def get_square_type(self):
        return self.square_type

    def get_owner(self):
        return self.square_type

    def set_owner(self, owner_name):
        self.owner = owner_name

    def action(self, player):
        if self.owner == "":
            player.buy_property()
            self.set_owner(deepcopy(player))
        return
