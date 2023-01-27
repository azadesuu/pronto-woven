from copy import deepcopy
from classes.board import Board
from classes.square import Property


import unittest
import json


class TestGame(unittest.TestCase):
    """Checks if the winner is Charlotte in all scenarios. The rolls have been
    designed in that way.

    The data is imported from the 'test_data' folder.
    There are two players, Charlotte and Sweedal, and 3 properties with 1 GO.
    That adds up to 4 Squares and 2 Players.
    """

    # Initialising Board and Player values
    board_f = open("test_data\\test_board_1.json")
    board_f_2 = open("test_data\\test_board_2.json")
    player_f = open("test_data\\test_players_1.json")

    t_player_data = json.load(player_f)
    t_board_data = json.load(board_f)
    t_board_data_2 = json.load(board_f_2)

    def test_simulate(self):
        """Simulates the rolls, [1,1], from the test_rolls_1 JSON file, in
        the board game.
        """
        rolls_1_f = open("test_data\\test_rolls_1.json")
        t_rolls_data = json.load(rolls_1_f)
        rolls_1_f.close()

        t_board = Board(self.t_board_data, self.t_player_data)
        t_board.simulate(t_rolls_data)

        self.assertTrue(t_board.get_NUM_PLAYERS() == 2)
        self.assertTrue(t_board.get_NUM_SQUARES() == 4)
        winner_name = ""
        winner_amount = -1
        for winner in t_board.get_end_winners():
            winner_name += winner.get_name()
            winner_amount = winner.get_amount()

        self.assertTrue(winner_name == "Charlotte")
        self.assertTrue(winner_amount == 16)

        Property.reset_class()

    def test_simulate2(self):
        """Simulates the rolls, [1,1,4,4], from the test_rolls_2 JSON file, in
        the board game
        """
        rolls_2_f = open("test_data\\test_rolls_2.json")
        t_rolls_data = json.load(rolls_2_f)
        rolls_2_f.close()

        t_board2 = Board(self.t_board_data, self.t_player_data)
        t_board2.simulate(t_rolls_data)

        self.assertTrue(t_board2.get_NUM_PLAYERS() == 2)
        self.assertTrue(t_board2.get_NUM_SQUARES() == 4)
        winner_name = ""
        winner_amount = -1
        for winner in t_board2.get_end_winners():
            winner_name += winner.get_name()
            winner_amount = winner.get_amount()

        # proves that the property is owned by Charlotte
        self.assertTrue(winner_name == "Charlotte")
        self.assertTrue(winner_amount == 18)

        Property.reset_class()

    def test_double_rent(self):
        """Checks if the rent is doubled if all properties of a colour
        is owned. Simulates the rolls, [1,1], from the test_rolls_1 JSON file,
        in the board game.
        """
        # Processing rolls
        rolls_1_f = open("test_data\\test_rolls_1.json")
        t_rolls_data = json.load(rolls_1_f)
        rolls_1_f.close()

        # Creating new board
        t_board3 = Board(self.t_board_data_2, self.t_player_data)
        t_board3.simulate(t_rolls_data)

        self.assertTrue(t_board3.get_NUM_PLAYERS() == 2)
        self.assertTrue(t_board3.get_NUM_SQUARES() == 3)
        winner_name = ""
        winner_amount = -1
        for winner in t_board3.get_end_winners():
            winner_name += winner.get_name()
            winner_amount = winner.get_amount()
        self.assertTrue(winner_name == "Charlotte")
        self.assertTrue(winner_amount == 17)

        Property.reset_class()

    board_f.close()
    player_f.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
