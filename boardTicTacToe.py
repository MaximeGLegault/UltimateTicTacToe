__author__ = 'Maxime Gagnon-Legault'
__date__ = '2016/01/10'

from caseTicTacToe import Case
from random import randrange


class Board:
    """
    Class for a board of a simple tic tac toe game to be used in a ultimate tic tac toe game

    Parameters:
        parentCoordinates (int, int): the coordinate of the board on a ultimate tictactoe board(between 0 and
                                      numberOf corresponding)
        numberOfLine (int = 3): number of line the board should have.
        numberOfColumn (int = 3): number of column the board should have.

    """


    def __init__(self, parentCoordinates, numberOfLine = 3, numberOfColumn = 3, writable=True):
        assert isinstance(parentCoordinates, tuple)
        assert isinstance(parentCoordinates[0], int)
        assert isinstance(parentCoordinates[1], int)
        assert len(parentCoordinates) == 2
        assert isinstance(numberOfLine, int)
        assert isinstance(numberOfColumn, int)
        assert parentCoordinates[0] in [0, 1, 2]
        assert parentCoordinates[1] in [0, 1, 2]
        assert numberOfLine >= 3
        assert numberOfColumn >= 3
        assert isinstance(writable, bool)
        assert writable in [True, False]

        self.writable = writable
        self.parentCoordinates = parentCoordinates
        self.numberOfLine = numberOfLine
        self.numberOfColumn = numberOfColumn

        self.cases = {}

        self.initializeToEmptyCases()



    def initializeToEmptyCases(self):

        self.cases.clear()

        for iii in range(0, 3):
            for jjj in range(0, 3):
                self.cases[iii, jjj] = Case(" ")



    def getNumberOfLine(self):
        return self.numberOfLine



    def getNumberOfColumn(self):
        return self.numberOfColumn


    #TODO is this useful?
    def isEmpty(self):
        for iii in range(0, 3):
            for jjj in range(0, 3):
                if not(self.cases[(iii, jjj)].isEmpty()):
                    return False
        return True



    def isValidMove(self, caseNumbers):
        assert isinstance(caseNumbers[0], int)
        assert isinstance(caseNumbers[1], int)
        assert len(caseNumbers) == 2
        assert caseNumbers[0] in [0, 1, 2]
        assert caseNumbers[1] in [0, 1, 2]

        return self.cases[caseNumbers[0], caseNumbers[1]].isEmpty()



    def addToken(self, caseNumbers, token):
        assert isinstance(caseNumbers, tuple)
        assert caseNumbers[0] in [0, 1, 2]
        assert caseNumbers[1] in [0, 1, 2]
        assert isinstance(token, str)
        assert token in [" ", "X", "O"]

        self.cases[caseNumbers[0], caseNumbers[1]].setToken(token)



    def isWinning(self, token):
        assert isinstance(token, str)
        assert token in [" ", "X", "O"]

        test = (token, token, token)
        return ((self.cases[0, 0].contenu,self.cases[0, 1].contenu,self.cases[0, 2].contenu) == test or
                (self.cases[1, 0].contenu,self.cases[1, 1].contenu,self.cases[1, 2].contenu) == test or
                (self.cases[2, 0].contenu,self.cases[2, 1].contenu,self.cases[2, 2].contenu) == test or
                (self.cases[0, 0].contenu,self.cases[1, 0].contenu,self.cases[2, 0].contenu) == test or
                (self.cases[0, 1].contenu,self.cases[1, 1].contenu,self.cases[2, 1].contenu) == test or
                (self.cases[0, 2].contenu,self.cases[1, 2].contenu,self.cases[2, 2].contenu) == test or
                (self.cases[0, 0].contenu,self.cases[1, 1].contenu,self.cases[2, 2].contenu) == test or
                (self.cases[2, 0].contenu,self.cases[1, 1].contenu,self.cases[0, 2].contenu) == test)



    def isThereAWinningMoveForToken(self, token):
        assert isinstance(token, str)
        assert token in ["X", "O"]

        for iii in range(0, 3):
            for jjj in range(0, 3):
                if self.isValidMove(iii, jjj):
                    self.addToken(iii, jjj, token)

                    if self.isWinning(token):
                        self.addToken(iii, jjj, " ")
                        return iii, jjj
                    self.addToken(iii, jjj, " ")
        return False



    def decideARandomCorrectMoveForToken(self):
        possibleCorrectMove = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.cases[i,j].isEmpty():
                    possibleCorrectMove += [(i,j)]

        randomCorrectMove = randrange(0, len(possibleCorrectMove))
        return possibleCorrectMove[randomCorrectMove]



    def selectNextMoveForToken(self, token):
        assert isinstance(token, str)
        assert token in ["X", "O"]

        if token == "X":
            opponentToken = "O"
        else:
            opponentToken = "X"

        preferrableMove = self.isThereAWinningMoveForToken(token)
        if preferrableMove:
           return preferrableMove

        preferrableMove = self.isThereAWinningMoveForToken(opponentToken)
        if preferrableMove:
            return preferrableMove

        return self.decideARandomCorrectMoveForToken(token)



    def getBoardNumber(self):
        return self.parentCoordinates



    def setWritable(self, writable):
        assert isinstance(writable, bool)
        assert writable in [True, False]

        self.writable = writable



    def isWritable(self):
        return self.writable
