import json
from classes.board import Board

board_f = open('board.json')
rolls_1_f = open('rolls_1.json')
rolls_2_f = open('rolls_2.json')


# Instantiating
board_data = json.load(board_f)
rolls_1_data = json.load(rolls_1_f)
rolls_2_data = json.load(rolls_2_f)


board = Board()
board.simulate(rolls_1_data)
board.simulate(rolls_2_data)
