from .player import Player
from .square import Square, Property, Go
from .constants import *


class Board:
    """
    A Board contains information about the game entities: squares and players.

    :param __square_dict: Contains information about square on the board. The
        dictionary keys are the positional indexes of each square.
    :type __square_dict: dict
    :param __player_dict: Contains information about each player. The
        dictionary keys are the order in which players play, starting
        from 0.
    :type __player_dict: dict
    :param __NUM_SQUARES: The total number of squares on the board
    :type __NUM_SQUARES: int
    :param __NUM_PLAYERS: The total number of players in the game.
    :type __NUM_PLAYERS: int
    :param __winners: Contains the finalised winners of the game.
    :type __winners: list
    """

    def __init__(self, raw_squares, raw_players):
        """Initialises a Board object

        :param raw_squares: Contains a list of dictionaries populated
            with square data
        :type raw_squares: list
        :param raw_players: Contains a list of dictionaries populated
            with player data
        :type raw_players: list
        """
        # Dictionaries containing data for the squares and players
        self.__square_dict = self.__parse_square_list(raw_squares)
        self.__player_dict = self.__parse_player_list(raw_players)

        # Number of squares and players for the board
        self.__NUM_SQUARES = len(self.__square_dict)
        self.__NUM_PLAYERS = len(self.__player_dict)

        # Will store the winners at the end
        self.__winners = list()

    # ------------- Class getters and setters

    def get_players(self):
        """Returns all player data

        :return: A dictionary populated with Player object data
        :rtype: dict
        """
        return self.__player_dict

    def get_squares(self):
        """Returns all squares data

        :return: A dictionary populated with Square object data
        :rtype: dict
        """
        return self.__square_dict

    def get_NUM_PLAYERS(self):
        """Returns the total number of players playing the game

        :return: The total number of players
        :rtype: int
        """
        return self.__NUM_PLAYERS

    def get_NUM_SQUARES(self):
        """Returns the total number of squares on the board

        :return: The total number of squares
        :rtype: int
        """
        return self.__NUM_SQUARES

    def get_end_winners(self):
        """Gets the list of winners at the end of a game

        :return: Final list of winning players
        :rtype: list
        """
        return self.__winners

    # ------------- Class Private Methods
    def __parse_player_list(self, player_list):
        """
        Processes player data from the raw JSON list

        :param player_list: The processed JSON file from the player data file
        :type player_list: list
        :return: Dictionary containing player numbers as keys, and
            Player objects as values
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
        """Processes square data from the raw JSON list

        :param square_list: The processed JSON String from the player data file
        :type square_list: list
        :return: Dictionary containing square positions as keys,
            and Square objects as values
        :rtype: dict
        """
        # Initialising an empty dictionary to put the values into
        squares = dict()
        if len(square_list) == 0:
            # no squares available
            return squares
        # Processing Square object data
        for i in range(len(square_list)):
            data = square_list[i]
            if data["type"] == "property":
                # Property square
                squares[i] = Property(
                    data["name"], data["type"], data["price"], data["colour"]
                )

            if data["type"] == "go":
                # GO square
                squares[i] = Go(data["name"], data["type"])
        return squares

    # ------------- Class Methods
    def add_winner(self, player):
        """Appends the winning player to the winners list

        :param player: The winning player
        :type player: Player
        """
        self.__winners.append(player)

    def simulate(self, rolls):
        """Simulates the board game with the given data and determined dice
        rolls. Will print the board data at the end of the game

        :param rolls: The determined dice rolls for the game
        :type rolls: list
        """
        for i in range(len(rolls)):
            # Number of squares to move
            steps = rolls[i]
            # The next player to move
            player_number = i % self.get_NUM_PLAYERS()
            player = (self.get_players())[player_number]
            # Player is moved
            self.move(player, steps)
            # The game ends when a player is bankrupt
            if player.is_bankrupt():
                break
        self.get_winners()
        Property.reset_class()

    def move(self, player, steps):
        """Moves the player forwards by the the number of 'steps' and performs
        the appropriate action depending on the Square object at the
        new position.

        :param player: Player object to be re-positioned
        :type player: Player
        :param steps: Number of steps to move on the board
        :type steps: int
        """
        curr_position = player.get_position()
        new_position = curr_position + steps
        if new_position >= self.get_NUM_SQUARES():
            # Player passes go
            player.add_amount(GO_AMOUNT)
        new_position = new_position % self.get_NUM_SQUARES()
        # Update player position
        player.set_position(new_position)

        # Player performs action on the square
        squares = self.get_squares()
        squares[new_position].action(player)

    def __str__(self):
        """Prints information about the Board object, including: current
        winners, and all players' amount and position for console output
        """
        board_string = ""
        board_string += "--------------RESULTS:--------------\n"
        board_string += "Who would win each game?\n" + self.get_winners()
        board_string += (
            "\nHow much money does everybody end up with?\n" + self.get_moneys()
        )
        board_string += (
            "\nWhat spaces does everybody finish on?\n" + self.get_positions()
        )
        return board_string

    def get_winners(self):
        """
        Obtains winner(s) with the maximum amount on hand

        :return: Information regarding the winning player(s) for console output
        :rtype: str
        """
        players = self.get_players()
        amounts = list()

        # Adds all the player's amounts to a list
        for num in players.keys():
            player = players[num]
            amounts.append(player.get_amount())

        # Get winner
        winner_empty = False
        if len(self.__winners) == 0:
            winner_empty = True
        max_amount = max(amounts)  # The highest amount
        winner_string = ""  # String will be returned for console output
        for num in players.keys():
            curr_player = players[num]
            player_amount = curr_player.get_amount()
            if player_amount == max_amount:
                # Player is a winner if their amount is the maximum
                if winner_empty:
                    self.add_winner(curr_player)
                winner_string += "Player %d, %s, is a winner with $%d\n" % (
                    num,
                    curr_player.get_name(),
                    curr_player.get_amount(),
                )

        return winner_string

    def get_moneys(self):
        """Obtains the amount on each player's hands

        :return: Information regarding all players' amount on hand for console output
        :rtype: str
        """
        players = self.get_players()
        amount_string = ""
        for num in players.keys():
            curr_player = players[num]
            amount_string += "Player %d, %s, has $%d\n" % (
                num,
                curr_player.get_name(),
                curr_player.get_amount(),
            )
        return amount_string

    def get_positions(self):
        """Obtains the position of each player

        :return: Information regarding all players' position on the board for console output
        :rtype: str
        """
        players = self.get_players()
        position_string = ""
        for num in players.keys():
            curr_player = players[num]
            position_string += "Player %d, %s, is at position %d\n" % (
                num,
                curr_player.get_name(),
                curr_player.get_position(),
            )
        return position_string
