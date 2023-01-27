from classes.board import Board
from classes.player import Player
from classes.square import Square, Go, Property
from classes.constants import *

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
    """A class that contains tests for the Player class
    methods and attributes"""

    test_player = Player("Azadesuu", 0)  # attribute values stay the same
    test_player2 = Player("Azadesuu", 0)  # change attributes

    def test_properties_private(self):
        """Asserts that none of the class attributes can be accessed directly"""
        t_player = self.test_player
        with self.assertRaises(AttributeError):
            t_player.__player_number
        with self.assertRaises(AttributeError):
            t_player.__name
        with self.assertRaises(AttributeError):
            t_player.__amount
        with self.assertRaises(AttributeError):
            t_player.__properties_owned
        with self.assertRaises(AttributeError):
            t_player.__position

    def test_properties_default(self):
        """Asserts player attributes are the default values
        Also tests the getter methods for the class"""
        t_player = self.test_player
        self.assertTrue(t_player.get_player_number() == 0)
        self.assertTrue(t_player.get_name() == "Azadesuu")
        self.assertTrue(len(t_player.get_properties_owned().keys()) == 0)

        # the starting amount and position is based on the
        # classes/constants.py file
        self.assertTrue(t_player.get_amount() == STARTING_AMOUNT)
        self.assertTrue(t_player.get_position() == STARTING_POSITION)

    def test_setter(self):
        """Asserts that the class setters are working"""
        t_player2 = self.test_player2
        # test setters first
        t_player2.set_amount(10)
        self.assertTrue(t_player2.get_amount() == 10)

    def test_bankrupt(self):
        t_player2 = self.test_player2
        t_player2.set_amount(10)
        self.assertTrue(t_player2.is_bankrupt() == False)
        t_player2.set_amount(-1)
        self.assertTrue(t_player2.is_bankrupt())

    def test_str(self):
        t_player = self.test_player
        self.assertTrue(t_player.__str__() == "Player Azadesuu is at 0 with $16")


class TestSquare(unittest.TestCase):
    """A class that contains tests for the Player class
    methods and attributes"""

    test_player = Player("Azadesuu", 0)  # attribute values stay the same
    test_player2 = Player("Azadesuu", 0)  # change attributes

    def test_properties_private(self):
        """Asserts that none of the class attributes can be accessed directly"""
        t_player = self.test_player
        with self.assertRaises(AttributeError):
            t_player.__player_number
        with self.assertRaises(AttributeError):
            t_player.__name
        with self.assertRaises(AttributeError):
            t_player.__amount
        with self.assertRaises(AttributeError):
            t_player.__properties_owned
        with self.assertRaises(AttributeError):
            t_player.__position

    def test_properties_default(self):
        """Asserts player attributes are the default values
        Also tests the getter methods for the class"""
        t_player = self.test_player
        self.assertTrue(t_player.get_player_number() == 0)
        self.assertTrue(t_player.get_name() == "Azadesuu")
        self.assertTrue(len(t_player.get_properties_owned().keys()) == 0)

        # the starting amount and position is based on the
        # classes/constants.py file
        self.assertTrue(t_player.get_amount() == STARTING_AMOUNT)
        self.assertTrue(t_player.get_position() == STARTING_POSITION)

    def test_setter(self):
        """Asserts that the class setters are working"""
        t_player2 = self.test_player2
        # test setters first
        t_player2.set_amount(10)
        self.assertTrue(t_player2.get_amount() == 10)

    def test_bankrupt(self):
        t_player2 = self.test_player2
        t_player2.set_amount(10)
        self.assertTrue(t_player2.is_bankrupt() == False)
        t_player2.set_amount(-1)
        self.assertTrue(t_player2.is_bankrupt())

    def test_str(self):
        t_player = self.test_player
        self.assertTrue(t_player.__str__() == "Player Azadesuu is at 0 with $16")


if __name__ == "__main__":
    unittest.main(verbosity=2)
