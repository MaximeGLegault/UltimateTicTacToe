__author__ = 'Maxime Gagnon-Legault'
__date__ = '2016/01/10'


class Case:
    """
    Class for a case of a simple tic tac toe table.

    Attributes:
        contents (str): What is contained inside the case(either " ", "X" or "O").
    """

    def __init__(self, contents):
        assert isinstance(contents, str)
        assert contents in [" ", "X", "O"]

        self.contained = contents

    def isEmpty(self):
        return self.contained == " "

    def isToken(self, tokenToIdentify):
        assert isinstance(tokenToIdentify, str)
        assert tokenToIdentify in [" ", "X", "O"]

        return self.contained == tokenToIdentify

    def setToken(self, token):
        assert isinstance(token, str)
        assert token in [" ", "X", "O"]

        self.contained = token