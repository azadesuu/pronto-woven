from classes.board import Board
from classes.player import Player
from classes.square import Square, Go, Property

import unittest
import json


def test_simple(self):
    board_f = open("tests\\test_board_1.json")
    player_f = open("tests\\test_players_1.json")
    rolls_1_f = open("tests\\test_rolls_1.json")

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


class TestPlayer(unittest.TestCase):
    test_player = Player("Azadesuu", 0)

    def test_properties_default(self):
        """Check player object for all default values"""
        t_player = self.test_player
        self.assertTrue(t_player.get_amount() == 0)
        self.assertTrue(t_player.get_player_number() == 0)
        self.assertTrue(t_player.get_position() == 0)
        self.assertTrue(len(self.t_player.get_properties_owned().keys()) == 0)

    def test_properties_change(self):
        t_player = self.test_player
        

if __name__ == "__main__":
    unittest.main()
