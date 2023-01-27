from .player import Player
from .square import Square, Property, Go
from .constants import *


class Board:
    """
    A Board contains information about the game entities: squares and players
    """

    def __init__(self, raw_squares, raw_players):
        """
        Initialises a Board object

        Args:
            raw_squares (list()): Contains a list of dictionaries populated with square data
            raw_players (list()): Contains a list of dictionaries populated with player data
        """
        """_summary_
        """
        self.__square_dict = self.__parse_square_list(raw_squares)
        self.__player_dict = self.__parse_player_list(raw_players)

        self.__NUM_SQUARES = len(self.__square_dict)
        self.__NUM_PLAYERS = len(self.__player_dict)

        self.__winners = list()

    # Getter methods
    def get_players(self):
        """
        Returns the dictionary of players: __player_dict
        """
        return self.__player_dict

    def get_squares(self):
        """
        Returns the dictionary of squares: __square_dicts
        """
        return self.__square_dict

    def get_NUM_PLAYERS(self):
        """
        Returns the number of players
        """
        return self.__NUM_PLAYERS

    def get_NUM_SQUARES(self):
        """
        Returns the number of squares on the board
        """
        return self.__NUM_SQUARES

    def get_end_winners(self):
        """
        Gets the list of winners at the end of a game

        Returns:
            list(): Final list of winning players
        """
        return self.winners

    # Private methods
    def __parse_player_list(self, player_list):
        """
        Processes player data from the raw JSON list

        :param player_list: The processed JSON String from the player data file
        :type player_list: str
        :return: dictionary containing player numbers as keys and Player objects as values
        :rtype: dict
        """
        new_dict = dict()
        if len(player_list) == 0:
            return new_dict
        for i in range(len(player_list)):
            player = player_list[i]
            new_dict[i] = Player(player["name"], i)
        return new_dict

    def __parse_square_list(self, square_list):
        """
        Processes player data from the raw JSON list

        Args:
            square_list (list()): The processed JSON String from the square data file

        Returns:
            dict(): dictionary containing positions as keys and Square objects as values
        """
        # initialising an empty dictionary to put the values into
        squares = dict()
        if len(square_list) == 0:
            # no squares available
            return squares
        # processing Square object data
        for i in range(len(square_list)):
            data = square_list[i]
            if (data["type"] == "property"):
                # property square
                squares[i] = Property(
                    data["name"], data["type"], data["price"], data["colour"])

            if (data["type"] == "go"):
                # GO square
                squares[i] = Go(data["name"], data["type"])
        return squares

    # Other methods
    def add_winner(self, player):
        """
        Adds the winning player to the 'winners' list

        Args:
            player (Player): A Player object
        """
        self.__winners.append(player)

    def simulate(self, rolls):
        """
        Simulates the board game with the given data and determined dice rolls

        Args:
            rolls (list()): List of numbers that determine the players' movesets
        """
        for i in range(len(rolls)):
            # number of squares to move
            steps = rolls[i]
            # the next player to move
            player_number = i % self.get_NUM_PLAYERS()
            player = (self.get_players())[player_number]
            # player is moved
            self.move(player, steps)
            # the game ends when a player is bankrupt
            if (player.is_bankrupt()):
                break
        self.__str__()

    def move(self, player, steps):
        """
        Moves the player forwards by the the number of 'steps' and performs the appropriate action depending on the new Square

        Args:
            player (Player): Player object to be re-positioned
            steps (int): Number of steps to move on the board
        """
        curr_position = player.get_position()
        new_position = curr_position + steps
        if (new_position >= self.get_NUM_SQUARES()):
            # player passes go
            player.add_amount(GO_AMOUNT)
        new_position = new_position % self.get_NUM_SQUARES()
        # update player position
        player.set_position(new_position)

        # Player performs action on the square
        squares = self.get_squares()
        squares[new_position].action(player)
        print(player)
        print(squares[new_position])
        print()

    def __str__(self):
        """ 
        Prints information about the Board object, including: current winners, and all players' amount and position for console output
        """
        print("--------------RESULTS:--------------")
        print("Who would win each game?\n" + self.get_winners())
        print("\nHow much money does everybody end up with?\n" + self.get_moneys())
        print("\nWhat spaces does everybody finish on?\n" + self.get_positions())

    def get_winners(self):
        """
        Obtains winner(s) with the maximum amount on hand

        Returns:
            str: Information regarding the winning player(s) for console output
        """
        players = self.get_players()
        amounts = list()

        # Adds all the player's amounts to a list
        for num in players.keys():
            player = players[num]
            amounts.append(player.get_amount())

        # Get winner
        max_amount = max(amounts)  # the highest amount
        winner_string = ""  # will be returned for console output
        for num in players.keys():
            curr_player = players[num]
            player_amount = curr_player.get_amount()
            if (player_amount == max_amount):
                # Player is a winner if their amount is the maximum
                self.add_winner(curr_player)
                winner_string += 'Player %d, %s, is a winner with $%d\n' % (
                    num, curr_player.get_name(), curr_player.get_amount())

        return winner_string

    # Returns String that describes each player's current amount
    def get_moneys(self):
        """
        Obtains the amount on each player's hands

        Returns:
            String: Information regarding all players' amount on hand for console output
        """
        players = self.get_players()
        amount_string = ""
        for num in players.keys():
            curr_player = players[num]
            amount_string += 'Player %d, %s, has $%d\n' % (
                num, curr_player.get_name(), curr_player.get_amount())
        return amount_string

    # Returns String that describes each player's current position
    def get_positions(self):
        """
        Obtains the position of each player

        Returns:
            String: Information regarding all players' position on the board for console output
        """
        players = self.get_players()
        position_string = ""
        for num in players.keys():
            curr_player = players[num]
            position_string += 'Player %d, %s, is at position %d\n' % (
                num, curr_player.get_name(), curr_player.get_position())
        return position_string
