from collections import defaultdict
import constants


class Board:
    def __init__(self, raw_squares, raw_players):
        self.player_dict = self.parse_player_list(raw_squares)
        self.square_list = self.parse_square_list(raw_players)
        print(self.player_dict)
        print(self.square_list)

        self.NUM_PLAYERS = len(self.player_dict)
        self.NUM_SQUARES = len(self.square_list)

    # private method
    def parse_player_list(self, player_list):
        try:
            if len(player_list) == 0:
                return dict()
            player_dict = dict()
            for i in range(len(player_list)):
                player_dict[i] = Player(player_list[i], i)
            return player_dict
        except:
            return
        finally:
            exit(-1)

    # private method
    def parse_square_list(self, square_list):
        try:
            new_list = list()
            if len(square_list) == 0:
                return new_list
            for i in range(len(square_list)):
                data = square_list[i]
                if (data["type"] == "property"):
                    new_list.append(
                        Property(data["name"], data["price"], data["colour"], data["type"]))
                if (data["type"] == "go"):
                    new_list.append(
                        Property(data["name"], data["price"], data["colour"], data["type"]))
            return new_list
        except:
            return
        finally:
            exit(-1)

    def __str__(self):
        print("Who would win each game:")
        print("How much money does everybody end up with:")
        print("What spaces does everybody finish on:")

    def get_winners(self):
        players = get_players()
        amounts = list()
        for player in players:
            amounts.append(player.get)


