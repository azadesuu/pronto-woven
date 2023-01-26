import json
import playerclass

board_f = open('board.json')
rolls_1_f = open('rolls_1.json')
rolls_2_f = open('rolls_2.json')


# Instantiating
board = json.load(board_f)
rolls_1 = json.load(rolls_1_f)
rolls_2 = json.load(rolls_2_f)
