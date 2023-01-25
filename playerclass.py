import constants

class Player:
  def __init__(self, name, player_number ):
    self.name = name
    self.player_number = player_number 
    self.amount = constants.STARTING_AMOUNT
    self.properties = {}

  # defining getters and setters

  # Only amount and properties are changed, so let's write setter methods for those
  


class Square:
    def __init__(self, name, price,colour, square_type):
        self.name = name
        self.price = price
        self.colour = colour
        self.square_type= square_type
    
    
    # defining getters
    # setters not allowed as properties do not change in the game
    
        