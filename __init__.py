import json
from classes.board import Board
from classes.board import Board


def __main__():
    # Opening all the relevant files
    board_f = open("data\\board.json")
    player_f = open("data\\players.json")
    rolls_1_f = open("data\\rolls_1.json")
    rolls_2_f = open("data\\rolls_2.json")

    # Processing data from the JSON objects
    player_data = json.load(player_f)
    board_data = json.load(board_f)
    rolls_1_data = json.load(rolls_1_f)
    rolls_2_data = json.load(rolls_2_f)

    # Close all the relevant files
    board_f.close()
    player_f.close()
    rolls_1_f.close()
    rolls_2_f.close()

    board = Board(board_data, player_data)
    board.simulate(rolls_1_data)
    print(board)
    board.simulate(rolls_2_data)
    print(board)


__main__()
