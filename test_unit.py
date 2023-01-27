from classes.board import Board
from classes.player import Player
from classes.square import Square, Go, Property
from classes.constants import *

import unittest
import json


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
        """Asserts that player attributes are the default values.
        Also tests the getter methods for the class"""
        t_player = self.test_player
        self.assertTrue(t_player.get_player_number() == 0)
        self.assertTrue(t_player.get_name() == "Azadesuu")
        self.assertTrue(len(t_player.get_properties_owned().keys()) == 0)

        # The starting amount and position is based on classes/constants.py
        self.assertTrue(t_player.get_amount() == STARTING_AMOUNT)
        self.assertTrue(t_player.get_position() == STARTING_POSITION)

    def test_setter(self):
        """Asserts that the class setters are working"""
        t_player2 = self.test_player2
        # Sets the player's amount on hand to 10
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
    """A class that contains tests for the Square class
    methods and attributes"""

    test_go = Go("GO", "go")  # attribute values stay the same
    test_property = Property(
        "McD", "property", 3, "Yellow"
    )  # attribute values stay the same
    test_property2 = Property("KFC", "property", 6, "Red")  # change attributes

    def test_properties_private_go(self):
        """Asserts that none of the class attributes can be accessed directly
        in the Go object"""
        t_go = self.test_go
        with self.assertRaises(AttributeError):
            t_go.__name
        with self.assertRaises(AttributeError):
            t_go.__square_type

    def test_properties_private_go(self):
        """Asserts that none of the class attributes can be accessed directly
        in the Property object"""
        t_prop = self.test_property
        with self.assertRaises(AttributeError):
            t_prop.__name
        with self.assertRaises(AttributeError):
            t_prop.__square_type
        with self.assertRaises(AttributeError):
            t_prop.__price
        with self.assertRaises(AttributeError):
            t_prop.__colour
        with self.assertRaises(AttributeError):
            t_prop.__owner
        with self.assertRaises(AttributeError):
            Property.__property_dict

    def test_properties_default(self):
        """Asserts that the object attributes are the default values.
        Also tests the getter methods for the class"""

        t_go = self.test_go
        t_prop = self.test_property
        self.assertTrue(t_go.get_name() == "GO")
        self.assertTrue(t_go.get_square_type() == "go")

        self.assertTrue(t_prop.get_name() == "McD")
        self.assertTrue(t_prop.get_square_type() == "property")
        self.assertTrue(t_prop.get_price() == 3)
        self.assertTrue(t_prop.get_owner() == None)
        self.assertTrue(t_prop.get_colour() == "Yellow")

    def test_setter(self):
        """Asserts that the class setters are working"""
        t_prop2 = self.test_property2
        t_prop2.set_owner(Player("Azadesuu", 0))
        self.assertTrue(t_prop2.get_owner().get_name() == "Azadesuu")

    def test_str(self):
        """Tests the dunder method"""
        t_prop2 = self.test_property2
        t_prop2.set_owner(Player("Azadesuu", 0))
        self.assertTrue(
            t_prop2.__str__()
            == ("Square is a property with price of 6, owned by Azadesuu")
        )

    def test_class_properties(self):
        self.assertTrue(Property.get_colour_num("Yellow") == 1)
        self.assertTrue(Property.get_colour_num("yellow") == 1)
        self.assertTrue(Property.get_colour_num("Red") == 1)
        self.assertTrue(Property.get_colour_num("red") == 1)
        self.assertTrue(Property.get_colour_num("blue") == 0)

    def test_property_action_doubled(self):
        t_prop2 = self.test_property2
        p0 = Player("Azadesu0", 0)
        p1 = Player("Azadesu1", 1)

        t_prop2.action(p0)
        t_prop2.action(p1)
        doubled_rent = t_prop2.get_price() * 2
        self.assertTrue(p1.get_amount() == (STARTING_AMOUNT - doubled_rent))

    def test_property_action_normal(self):
        t_prop2 = self.test_property2
        p0 = Player("Azadesu0", 0)
        p1 = Player("Azadesu1", 1)

        # doesn't add property to player's "owned" list
        # that's why it's not doubled
        t_prop2.set_owner(p0)
        t_prop2.action(p1)
        rent = t_prop2.get_price()
        self.assertTrue(p1.get_amount() == (STARTING_AMOUNT - rent))


class TestGame(unittest.TestCase):
    """Checks if the winner is Charlotte in all scenarios. The rolls have been
    designed in that way.

    The data is imported from the 'test_data' folder.
    There are two players, Charlotte and Sweedal, and 3 properties with 1 GO.
    That adds up to 4 Squares and 2 Players.
    """

    # Resetting the property dictionary
    Property.reset_class()
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

    board_f.close()
    player_f.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
