from collections import defaultdict
from copy import deepcopy
import constants


class Board:
    def __init__(self, raw_squares, raw_players):
        self.player_dict = self.parse_player_list(raw_squares)
        self.square_dict = self.parse_square_list(raw_players)
        print(self.player_dict)
        print(self.square_list)

        self.NUM_PLAYERS = len(self.player_dict)
        self.NUM_SQUARES = len(self.square_dict)

    # defining getters
    def get_players(self):
        return self.player_dict

    def get_squares(self):
        return self.square_list

    # private method
    # processes the data from the raw JSON
    def parse_player_list(self, player_list):
        try:
            new_dict = dict()
            if len(player_list) == 0:
                return new_dict
            for i in range(len(player_list)):
                new_dict[i] = Player(player_list[i], i)
            return new_dict
        except:
            return
        finally:
            exit(-1)

    # private method
    # processes the data from the raw JSON
    def parse_square_list(self, square_list):
        try:
            new_dict = dict
            if len(square_list) == 0:
                return new_dict
            for i in range(len(square_list)):
                data = square_list[i]
                if (data["type"] == "property"):
                    new_dict[i] = Property(
                        data["name"], data["price"], data["colour"], data["type"])
                if (data["type"] == "go"):
                    new_dict[i] = Property(
                        data["name"], data["price"], data["colour"], data["type"])
                    return new_dict
        except:
            return
        finally:
            exit(-1)

    # Dunder method to print information about the board
    def __str__(self):
        print("Who would win each game:\n" + self.get_winners())
        print("How much money does everybody end up with:\n" + self.get_moneys())
        print("What spaces does everybody finish on:\n" + self.get_positions())

    # Returns winner(s) with the maximum amount on hand
    def get_winners(self):
        players = self.get_players()
        amounts = list()
        for player in players:
            amounts.append(player.get)

    # Returns String that describes each player's current amount
    def get_moneys(self):
        players = self.get_players()
        amounts = list()
        for player in players:
            amounts.append(player.get)

    # Returns String that describes each player's current position
    def get_positions(self):
        players = self.get_players()
        amounts = list()
        for player in players:
            amounts.append(player.get)

    def roll(self, player, dice_roll):
        number = dice_roll
        curr_position = player.get_position()
        new_position = (curr_position + number) % self.NUM_SQUARES
        # update player position
        player.set_position(new_position)
        # action on the square
        self.get_square_dict(new_position).action(player)


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


class Square:
    def __init__(self, name, square_type):
        self.name = name
        self.square_type = square_type

    def action(player: Player):
        # empty
        return


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
