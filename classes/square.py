from collections import defaultdict
from copy import copy, deepcopy
from .player import Player


class Square:
    """A Square is a position on the Board. Players will perform different
    actions based on the current type and properties of the Square object.

    :param name: The name of the Square
    :type name: str
    :param square_type: The type of Square, which determines the
        player actions
    :type square_type: str
    """

    def __init__(self, name, square_type):
        """Initialises a Square object

        :param __name: The name of the Square
        :type __name: str
        :param __square_type: The type of Square, which determines the
            player actions
        :type __square_type: str
        """
        self.__name = name
        self.__square_type = square_type

    # ------------- Class getters and setters
    def get_name(self):
        """Returns the square's name

        :return: The square's name
        :rtype: str
        """
        return self.__name

    def get_square_type(self):
        """Returns the square's type

        :return: The square's type
        :rtype: str
        """
        return self.__square_type

    # ------------- Class Interface
    def action(self, player: Player):
        """The action the player performs when it lands on the Square

        :param player: The current performing player
        :type player: Player
        """
        pass


class Go(Square):
    """Go is a subclass of Square. It inherits state and behavior from
    the Square class. It is initialised the same way as a Square, with
    __square_type as "go" for this simulation

    :param Square: Parent class
    :type Square: Square
    """

    def __str__(self):
        """A dunder method that provides information about the class object
        with a String

        :return: Information about the class object (type)
        :rtype: str
        """
        return "a %s" % (self.get_square_type())


class Property(Square):
    """Property is a subclass of Square. It inherits state and behavior from
    the Square class. It is initialised differently from its ancestor class,
    with __square_type as "property" for this simulation

    :param Square: Parent class
    :type Square: Square

    :param __property_dict: Contains information about all the properties
        of the game. The properties are sorted by colour. That is, for each key
        or colour in the dictionary, the value associated with that colour
        will be the list of properties with the given colour.
    :type name: dict

    :param __name: The name of the Square
    :type __name: str
    :param __square_type: The type of Square, which determines the
        player actions
    :type __square_type: str

    :param __price: The price of the property/rent
    :type __price: str
    :param __colour: The colour of the property
    :type __colour: str
    :param __owner: The current owner of the property. Defaults to None.
    :type __owner: str
    """

    # Class attribute
    __property_dict = defaultdict(list)

    def __init__(self, name, square_type, price, colour):
        super().__init__(name, square_type)
        self.__price = price
        self.__colour = colour
        self.__owner = None
        # Private method
        self.__add_property(self)

    # ------------- Class getters and setters
    def get_price(self):
        """Returns the property price/rent

        :return: The property price/rent
        :rtype: int
        """
        return self.__price

    def get_colour(self):
        """Returns the property colour

        :return: The property colour
        :rtype: str
        """
        return self.__colour

    def get_owner(self):
        """Returns the property owner

        :return: The property owner
        :rtype: Player, optional
        """
        return self.__owner

    def set_owner(self, player):
        """Sets the given Player object as the owner of the Property object

        :param player: The player to own the property
        :type player: Player
        """
        self.__owner = player

    # ------------- Class Methods
    @classmethod
    def __add_property(cls, prop):
        """Adds the property to the property dictionary that contains all
        property data in the Property class.

        :param property: A new property object
        :type property: Property
        """
        # Adding properties to dictionary by colour
        colour = prop.get_colour()
        (cls.__property_dict[colour]).append(copy(prop))

    @classmethod
    def get_colour_num(cls, colour):
        """Get the number of properties of the given colour from the
        property dictionary

        :param colour: _description_
        :type colour: _type_
        :return: _description_
        :rtype: _type_
        """

        c_colour = colour.capitalize()
        return len(cls.__property_dict[c_colour])

    def action(self, player):
        """The action the player performs when it lands on the Square.

        :param player: The current performing player
        :type player: Player
        """
        # Get the current property owner
        property_owner = self.get_owner()
        if property_owner == None:
            # Player must buy the property if its not owned.
            # Assume that the player will own the property even if they-
            # -cannot afford it, and go into debt
            player.buy_property(self)
            self.set_owner(player)
            return
        # The player must pay rent
        rent = self.get_price()
        property_colour = self.get_colour()
        owner_properties = property_owner.get_properties_owned()
        if len(owner_properties[property_colour]) == self.get_colour_num(
            property_colour
        ):
            # If the current owner owns all the properties in the same colour-
            # -the rent is doubled
            rent *= 2

        # Making the assumption that if the player cannot pay rent,-
        # -they will empty their wallets to the owner and game ends
        player_wallet = player.get_amount()
        if player_wallet < rent:
            property_owner.add_amount(player_wallet)
            player.subtract_amount(player_wallet)
        else:
            # Add the rent to the property owner
            property_owner.add_amount(rent)
            # Subtract the rent from the current player
            player.subtract_amount(rent)

    def __str__(self):
        """A dunder method that provides information about the class object
        with a String

        :return: Information about the class object (type, price, owner)
        :rtype: str
        """
        if self.get_owner() == None:
            return "a %s %s, %s, with price of %d, owned by %s" % (
                self.get_colour(),
                self.get_square_type(),
                self.get_name(),
                self.get_price(),
                "None",
            )
        return "a %s %s, %s, with price of %d, owned by %s" % (
            self.get_colour(),
            self.get_square_type(),
            self.get_name(),
            self.get_price(),
            self.get_owner().get_name(),
        )

    @classmethod
    def reset_class(cls):
        """Clears information regarding board properties from the class"""
        cls.__property_dict.clear()
        cls.__property_dict = defaultdict(list)
