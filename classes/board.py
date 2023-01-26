from player import Player
from square import Square, Property, Go

"""
A Board contains two dictionaries:
1. square_dict: contains indexes as keys and Square objects as values
2. Players: contains indexes as keys and Player objects as values
"""


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

    def get_NUM_PLAYERS(self):
        return self.NUM_PLAYERS

    def get_NUM_SQUARES(self):
        return self.NUM_SQUARES

    # private method
    # processes the data from the raw JSON
    def parse_player_list(self, player_list):
        new_dict = dict()
        if len(player_list) == 0:
            return new_dict
        for i in range(len(player_list)):
            new_dict[i] = Player(player_list[i], i)
        return new_dict

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
