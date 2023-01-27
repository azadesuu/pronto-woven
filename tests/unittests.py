from ..classes.board import Board
from ..classes.player import Player
from ..classes.square import Square, Property, Go
import unittest


class TestBoard():
    def a():
        pass


class TestPlayer():
    def a():
        pass


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
