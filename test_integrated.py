from classes.board import Board

import unittest
import json


class TestSimple(unittest.TestCase):
    def test_two(self):
        self.assertTrue(2 == 2)

    def test_simple(self):
        board_f = open("test_data\\test_board_1.json")
        player_f = open("test_data\\test_players_1.json")
        rolls_1_f = open("test_data\\test_rolls_1.json")

        # Instantiating
        t_player_data = json.load(player_f)
        t_board_data = json.load(board_f)
        t_rolls_data = json.load(rolls_1_f)

        board = Board(t_board_data, t_player_data)
        self.assertTrue(board.get_NUM_PLAYERS() == 4)
        self.assertTrue(board.get_NUM_SQUARES() == 4)
        board.simulate(t_rolls_data)

        board_f.close()
        player_f.close()
        rolls_1_f.close()


if __name__ == "__main__":
    unittest.main()
