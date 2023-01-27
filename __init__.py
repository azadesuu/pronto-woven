import json
from classes.board import Board


def __main__():
    board_f = open('board.json')
    player_f = open('players.json')
    rolls_1_f = open('rolls_1.json')
    rolls_2_f = open('rolls_2.json')

    # Instantiating
    player_data = json.load(player_f)
    board_data = json.load(board_f)
    rolls_1_data = json.load(rolls_1_f)
    rolls_2_data = json.load(rolls_2_f)

    board = Board(board_data, player_data)
    board.simulate(rolls_1_data)

    # board.simulate(rolls_2_data)


__main__()
