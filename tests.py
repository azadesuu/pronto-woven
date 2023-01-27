from classes.board import Board

import unittest
import json


class TestSimple(unittest.TestCase):
    def test_two(self):
        self.assertTrue(2 == 2)

    def test_simple(self):
        board_f = open('tests\\test_board_1.json')
        player_f = open('tests\\test_players_1.json')
        rolls_1_f = open('tests\\test_rolls_1.json')

        # Instantiating
        player_data = json.load(player_f)
        board_data = json.load(board_f)
        rolls_1_data = json.load(rolls_1_f)

        board = Board(board_data, player_data)
        self.assertTrue(board.get_NUM_PLAYERS() == 4)
        self.assertTrue(board.get_NUM_SQUARES() == 4)
        board.simulate(rolls_1_data)

        board_f.close()
        player_f.close()
        rolls_1_f.close()


if __name__ == '__main__':
    unittest.main()