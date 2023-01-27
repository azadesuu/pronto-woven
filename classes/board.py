from .player import Player
from .square import Square, Property, Go

"""
A Board contains two dictionaries:
1. square_dict: contains indexes as keys and Square objects as values
2. Players: contains indexes as keys and Player objects as values
"""


class Board:
    def __init__(self, raw_squares, raw_players):
        self.__player_dict = self.__parse_player_list(raw_players)
        self.__square_dict = self.__parse_square_list(raw_squares)

        self.NUM_PLAYERS = len(self.__player_dict)
        self.NUM_SQUARES = len(self.__square_dict)

    # defining getters
    def get_players(self):
        return self.__player_dict

    def get_squares(self):
        return self.__square_list

    def get_NUM_PLAYERS(self):
        return self.NUM_PLAYERS

    def get_NUM_SQUARES(self):
        return self.NUM_SQUARES

    # private method
    # processes the data from the raw JSON
    def __parse_player_list(self, player_list):
        new_dict = dict()
        if len(player_list) == 0:
            return new_dict
        for i in range(len(player_list)):
            player = player_list[i]
            new_dict[i] = Player(player["name"], i)
        return new_dict

    # private method
    # processes the data from the raw JSON
    def __parse_square_list(self, square_list):
        squares = dict()
        print(square_list)
        if len(square_list) == 0:
            return squares
        for i in range(len(square_list)):
            data = square_list[i]
            if (data["type"] == "property"):
                created_property = Property(
                    data["name"], data["price"], data["colour"], data["type"])
                squares[i] = created_property
            if (data["type"] == "go"):
                squares[i] = Go(
                    data["name"], data["type"])
        return squares

    # simulate the game using determined rolls
    def simulate(self, rolls):
        for i in range(len(rolls)):
            steps = rolls[i]
            player_number = i % self.NUM_PLAYERS
            player = (self.get_player_dict())[player_number]

            self.roll(player, steps)

            if (player.is_bankrupt()):
                break

        self.__str__()

    # Dunder method to print information about the board
    def __str__(self):
        print("--------------RESULTS:--------------")
        print("Who would win each game?\n" + self.get_winners())
        print("\nHow much money does everybody end up with?\n" + self.get_moneys())
        print("\nWhat spaces does everybody finish on?\n" + self.get_positions())

    # Returns winner(s) with the maximum amount on hand
    def get_winners(self):
        players = self.get_players()
        amounts = list()
        for player in players:
            amounts.append(player.get_amount())

        # get winner
        max_amount = max(amounts)
        winner_string = ""
        for i in range(len(players.keys())):
            curr_player = players[i]
            player_amount = curr_player.get_amount()
            # if the player amount is the maximum
            if (player_amount == max_amount):
                winner_string += 'Player %d, %s, is a winner with $%d\n' % (
                    i, curr_player.get_name(), curr_player.get_amount())

    # Returns String that describes each player's current amount
    def get_moneys(self):
        players = self.get_players()
        amount_string = ""
        for i in range(len(players.keys)):
            curr_player = players[i]
            amount_string += 'Player %d, %s, has $%d\n' % (
                i, curr_player.get_name(), curr_player.get_amount())

    # Returns String that describes each player's current position
    def get_positions(self):
        players = self.get_players()
        position_string = ""
        for i in range(len(players.keys)):
            curr_player = players[i]
            position_string += 'Player %d, %s, is at position $%d\n' % (
                i, curr_player.get_name(), curr_player.get_position())

    def roll(self, player, steps):
        curr_position = player.get_position()
        new_position = (curr_position + steps) % self.NUM_SQUARES
        # update player position
        player.set_position(steps)
        # Player performs action on the square
        squares = self.get_square_dict().values()
        squares[new_position].action(player)
