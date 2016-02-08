__author__ = 'Maxime Gangon-Legault'
__date__ = "2016/01/10"


class Player:

    def __init__(self, name, type, token):
        """
        Class for a player of a simple tic tac toe game

        Attributes:
            name (str): the name of the player
            type (str): the type of the player (either human or computer)
            token (str): the type of token the player has (either X or O)
        """
        assert isinstance(name, str)
        assert isinstance(type, str)
        assert type in ["human", "computer"]
        assert isinstance(token, str)
        assert token in [" ", "X", "O"]

        self.name = name
        self.type = type
        self.token = token

    def getToken(self):
        return self.token

    def setToken(self, token):
        assert token in [' ', 'X', 'O']

        self.token = token

    def __str__(self):
        return self.name + " " + self.type + " " + self.token

