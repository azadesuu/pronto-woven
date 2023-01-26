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


class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number
        self.amount = constants.STARTING_AMOUNT
        self.properties_owned = defaultdict([])

    def buy_property(self, property):
        self.properties_owned[property.colour].append(property)

    # defining getters and setters

    def get_amount(self):
        return self.amount

    # Only amount and properties are changed, so let's write setter methods for those

    def add_amount(self, num):
        self.set_amount(self.get_amount() + num)


class Square:
    def __init__(self, name, square_type):
        self.name = name
        self.square_type = square_type

    def is_bankrupt(player):
        if (player.amount < 0):
            return True
        return False

    def action(player: Player):
        # empty
        return


class Go(Square):
    def action(player: Player):
        player.add_amount(1)


class Property(Square):
    def __init__(self, name, square_type, price, colour):
        super(name, square_type)
        self.price = price
        self.colour = colour
        self.owner = -1

    # defining getters
    # setters not allowed as properties do not change in the game
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_colour(self):
        return self.colour

    def get_square_type(self):
        return self.square_type

    def get_owner(self):
        return self.square_type

    def set_owner(self, owner_name):
        self.owner = owner_name

    def action(self, player: Player):
        if self.owner == "":
            player.buy_property()
            self.set_owner(player.player_number)
        return
