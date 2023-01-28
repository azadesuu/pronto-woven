from classes.board import Board
from classes.player import Player
from classes.square import Square, Go, Property
from classes.constants import *

import unittest
import json


class TestPlayer(unittest.TestCase):
    """A class that contains tests for the Player class
    methods and attributes"""

    # Declaring class variables
    test_player = None
    test_player2 = None

    @classmethod
    def setUpClass(cls):
        cls.test_player = Player("Azadesuu", 0)  # attribute values stay the same
        cls.test_player2 = Player("Azadesuu", 0)  # change attributes

    def test_attributes_private(self):
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

    def test_attributes_default(self):
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

    # ------------- Testing Class Methods
    def test_bankrupt(self):
        """Tests if the class is correctly checking that the
        player is bankrupt
        """
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

    test_go = None
    test_property = None
    test_property2 = None

    @classmethod
    def setUpClass(cls):
        # Resetting the property class dictionary
        Property.reset_class()
        # Go object
        cls.test_go = Go("GO", "go")  # attribute values stay the same
        # Property objects
        cls.test_property = Property(
            "McD", "property", 3, "Yellow"
        )  # attribute values stay the same
        cls.test_property2 = Property("KFC", "property", 6, "Red")  # change attributes

    @classmethod
    def tearDownClass(cls):
        Property.reset_class()

    def test_properties_private_go(self):
        """Asserts that none of the class attributes can be accessed directly
        in the Go object"""
        t_go = self.test_go
        with self.assertRaises(AttributeError):
            t_go.__name
        with self.assertRaises(AttributeError):
            t_go.__square_type

    def test_attributes_private(self):
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

    def test_attributes_default(self):
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

    # ------------- Testing Class Methods
    def test_str(self):
        """Tests the dunder method"""
        t_prop2 = self.test_property2
        t_prop2.set_owner(Player("Azadesuu", 0))
        self.assertTrue(
            t_prop2.__str__()
            == ("Square is a property with price of 6, owned by Azadesuu")
        )

    def test_class_properties(self):
        """Checks if the Property's properties dictionary is correctly
        collecting all the property objects
        """
        self.assertTrue(Property.get_colour_num("Yellow") == 1)
        self.assertTrue(Property.get_colour_num("yellow") == 1)
        self.assertTrue(Property.get_colour_num("Red") == 1)
        self.assertTrue(Property.get_colour_num("red") == 1)
        self.assertTrue(Property.get_colour_num("blue") == 0)

    def test_property_action_doubled(self):
        """Checks if the class object method is correctly doubling the rent if
        the player owns all properties of the same colour
        """
        t_prop2 = self.test_property2
        p0 = Player("Azadesu0", 0)
        p1 = Player("Azadesu1", 1)

        t_prop2.action(p0)
        t_prop2.action(p1)
        doubled_rent = t_prop2.get_price() * 2
        self.assertTrue(p1.get_amount() == (STARTING_AMOUNT - doubled_rent))

    def test_property_action_normal(self):
        """Checks if the class object is correctly collecting rent if a
        player owns the property (but not all properties in the colour)
        """
        t_prop2 = self.test_property2
        p0 = Player("Azadesu0", 0)
        p1 = Player("Azadesu1", 1)

        # doesn't add property to player's "owned" list
        # that's why it's not doubled
        t_prop2.set_owner(p0)
        t_prop2.action(p1)
        rent = t_prop2.get_price()
        self.assertTrue(p1.get_amount() == (STARTING_AMOUNT - rent))


class TestBoard(unittest.TestCase):
    """A class that contains tests for the Board class
    methods and attributes"""

    # Declaring class variables
    # Loaded data
    t_player_data = None
    t_board_data = None
    t_board_data2 = None

    @classmethod
    def setUpClass(cls):
        # Resetting the property class dictionary
        Property.reset_class()
        # Initialising Board and Player values
        # Opening JSON files
        board_f = open("test_data\\test_board_1.json")
        board_f_2 = open("test_data\\test_board_2.json")
        player_f = open("test_data\\test_players_1.json")

        # Processing JSON files
        cls.t_player_data = json.load(player_f)
        cls.t_board_data = json.load(board_f)
        cls.t_board_data_2 = json.load(board_f_2)

    def test_attributes_private(self):
        """Ensures that the board attributes are private"""
        t_board = Board(self.t_board_data, self.t_player_data)
        with self.assertRaises(AttributeError):
            t_board.__square_dict
        with self.assertRaises(AttributeError):
            t_board.__player_dict
        with self.assertRaises(AttributeError):
            t_board.__NUM_SQUARES
        with self.assertRaises(AttributeError):
            t_board.__NUM_PLAYERS
        with self.assertRaises(AttributeError):
            t_board.__winners

    def test_attributes_default(self):
        """Tests the default attributes of the board. Also tests the getter
        methods for the class
        """
        # Creating board
        t_board = Board(self.t_board_data, self.t_player_data)

        # Check if correct number of players and squares
        self.assertTrue(t_board.get_NUM_PLAYERS() == 2)
        self.assertTrue(t_board.get_NUM_SQUARES() == 4)
        # Check if default value is assigned
        self.assertTrue(t_board.get_end_winners() == [])
        # Check if players have been added correctly
        players = list(t_board.get_players().values())
        self.assertTrue((players[0]).get_name() == "Charlotte")
        self.assertTrue((players[1]).get_name() == "Sweedal")
        # Check if squares have been added correctly
        squares = list(t_board.get_squares().values())
        self.assertTrue((squares[0]).get_name() == "GO")
        self.assertTrue((squares[1]).get_name() == "The Burvale")
        self.assertTrue((squares[2]).get_name() == "Fast Kebabs")
        self.assertTrue((squares[3]).get_name() == "The Grand Tofu")

    # ------------- Testing Class Methods
    def test_move(self):
        """Checks that the 'move' method in Board is functioning"""
        # Creating board
        t_board = Board(self.t_board_data, self.t_player_data)
        player1 = list(t_board.get_players().values())[0]

        # Move the player around the board
        t_board.move(player1, t_board.get_NUM_SQUARES())
        self.assertTrue(player1.get_position() == 0)
        # Player gets extra money from passing GO
        self.assertTrue(player1.get_amount() == (STARTING_AMOUNT + GO_AMOUNT))

        # Move the player by 1 step
        t_board.move(player1, 1)
        self.assertTrue(player1.get_position() == 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
