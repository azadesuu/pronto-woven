from .player import Player
from .square import Square, Property, Go
from .constants import *


class Board:
    """
    A Board contains information about the game entities: squares and players

    A Board contains two attributes:
    1. __square_dict: a private dict() containing indexes as keys and Square objects as values
    2. __player_dict: a private dict() containing indexes as keys and Player objects as values

    """

    def __init__(self, raw_squares, raw_players):
        self.__player_dict = self.__parse_player_list(raw_players)
        self.__square_dict = self.__parse_square_list(raw_squares)

        self.NUM_PLAYERS = len(self.__player_dict)
        self.NUM_SQUARES = len(self.__square_dict)

    # defining getters
    def get_players(self):
        """
        Returns the dictionary of players: __player_dict
        """
        return self.__player_dict

    def get_squares(self):
        """
        Returns the dictionary of players: __player_dict
        """
        return self.__square_dict

    def get_NUM_PLAYERS(self):
        """
        Returns the number of players
        """
        return self.NUM_PLAYERS

    def get_NUM_SQUARES(self):
        """
        Returns the number of squares on the board
        """
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

    def __parse_square_list(self, square_list):
        # initialising an empty dictionary to put the values into
        squares = dict()
        if len(square_list) == 0:
            # no squares available
            return squares
        for i in range(len(square_list)):
            data = square_list[i]
            if (data["type"] == "property"):
                # property square
                created_property = Property(
                    data["name"], data["type"], data["price"], data["colour"])
                squares[i] = created_property
            if (data["type"] == "go"):
                # GO square
                squares[i] = Go(
                    data["name"], data["type"])
        return squares

    def simulate(self, rolls):
        """
        Simulates the board game with the given data and determined dice rolls
        """
        for i in range(len(rolls)):
            steps = rolls[i]
            player_number = i % self.NUM_PLAYERS
            player = (self.get_players())[player_number]

            self.move(player, steps)

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
        for num in players.keys():
            player = players[num]
            amounts.append(player.get_amount())

        # get winner
        max_amount = max(amounts)
        winner_string = ""
        for num in players.keys():
            curr_player = players[num]
            player_amount = curr_player.get_amount()
            # if the player amount is the maximum
            if (player_amount == max_amount):
                winner_string += 'Player %d, %s, is a winner with $%d\n' % (
                    num, curr_player.get_name(), curr_player.get_amount())
        return winner_string

    # Returns String that describes each player's current amount
    def get_moneys(self):
        players = self.get_players()
        amount_string = ""
        for num in players.keys():
            curr_player = players[num]
            amount_string += 'Player %d, %s, has $%d\n' % (
                num, curr_player.get_name(), curr_player.get_amount())

        return amount_string

    # Returns String that describes each player's current position
    def get_positions(self):
        players = self.get_players()
        position_string = ""
        for num in players.keys():
            curr_player = players[num]
            position_string += 'Player %d, %s, is at position %d\n' % (
                num, curr_player.get_name(), curr_player.get_position())
        return position_string

    def move(self, player, steps):
        curr_position = player.get_position()
        new_position = curr_position + steps
        if (new_position >= self.get_NUM_SQUARES()):
            # player passes go
            player.add_amount(GO_AMOUNT)
        new_position = new_position % self.NUM_SQUARES
        # update player position
        player.set_position(new_position)

        # Player performs action on the square
        squares = self.get_squares()
        squares[new_position].action(player)
        print(player)
        print(squares[new_position])
        print()
