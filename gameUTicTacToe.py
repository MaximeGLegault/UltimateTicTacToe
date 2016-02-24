__author__ = 'Maxime Gagnon-Legault'
__date__ = "2015/01/10"


from boardTicTacToe import Board


class Game:

    def __init__(self):

        self.boards = {}
        self.players = []
        self.currentPlayer = None
        #TODO do i need this
        self.numberOfDraw = 0
        self.movesHistory = []
        self.continuePlay = True

        self.initialize()

    def initialize(self):
        #*********************
        self.boards.clear()
        self.movesHistory.clear()
        #TODO is this still valid up

        for iii in range(0, 3):
            for jjj in range(0, 3):
                self.boards[iii, jjj] = Board((iii, jjj))

    #TODO is this used?
    def getBoard(self, i, j):
        return self.boards[i, j]

    def addMoveInHistory(self, boardNumbers, caseNumbers, token):
        self.movesHistory.append(((boardNumbers, caseNumbers), token))

    def deleteLastMoveHistory(self):
        self.movesHistory = self.movesHistory[0:-2]

    def addPlayer(self, player):
        self.players.append(player)

    def setStarterPlayer(self):
        #TODO see if this still old
        assert len(self.players) == 2

        if self.players[0].getToken() == "X":
            self.currentPlayer = self.players[0]
        else:
            self.currentPlayer = self.players[1]

    def changeCurrentPlayer(self):
        if self.currentPlayer == self.players[0]:
            self.currentPlayer = self.players[1]
        elif self.currentPlayer == self.players[1]:
            self.currentPlayer = self.players[0]

    def isWinning(self):
        token = self.currentPlayer.token
        winner = ((self.boards[0, 0].isWinning(token) and self.boards[0, 1].isWinning(token) and
                   self.boards[0, 2].isWinning(token)) or
                  (self.boards[1, 0].isWinning(token) and self.boards[1, 1].isWinning(token) and
                   self.boards[1, 2].isWinning(token)) or
                  (self.boards[2, 0].isWinning(token) and self.boards[2, 1].isWinning(token) and
                   self.boards[2, 2].isWinning(token)) or
                  (self.boards[0, 0].isWinning(token) and self.boards[1, 0].isWinning(token) and
                   self.boards[2, 0].isWinning(token)) or
                  (self.boards[0, 1].isWinning(token) and self.boards[1, 1].isWinning(token) and
                   self.boards[2, 1].isWinning(token)) or
                  (self.boards[0, 2].isWinning(token) and self.boards[1, 2].isWinning(token) and
                   self.boards[2, 2].isWinning(token)) or
                  (self.boards[0, 0].isWinning(token) and self.boards[1, 1].isWinning(token) and
                   self.boards[2, 2].isWinning(token)) or
                  (self.boards[0, 2].isWinning(token) and self.boards[1, 1].isWinning(token) and
                   self.boards[2, 0].isWinning(token)))
        return winner

    def __str__(self):
        return self.players[0].__str__()

    def setWritableOfBoard(self, boardNumbers, writable):
        assert writable in [True, False]

        self.boards[boardNumbers[0], boardNumbers[1]].setWritable(writable)

    def getWritableOfBoard(self, boardNumbers,):
        assert isinstance(boardNumbers, tuple)
        assert isinstance(boardNumbers[0], int)
        assert isinstance(boardNumbers[1], int)
        assert len(boardNumbers) == 2

        return self.boards[boardNumbers[0], boardNumbers[1]].isWritable()

    def getWritableOfCase(self, boardNumbers, caseNumbers):
        return self.boards[boardNumbers[0], boardNumbers[1]].isValidMove(caseNumbers)

    def addToken(self, boardNumbers, caseNumbers, token):
        assert isinstance(boardNumbers, tuple)
        assert isinstance(boardNumbers[0], int)
        assert isinstance(boardNumbers[1], int)
        assert len(boardNumbers) == 2
        assert boardNumbers[0] in [0, 1, 2]
        assert boardNumbers[1] in [0, 1, 2]
        assert isinstance(caseNumbers, tuple)
        assert isinstance(caseNumbers[0], int)
        assert isinstance(caseNumbers[1], int)
        assert len(caseNumbers) == 2
        assert caseNumbers[0] in [0, 1, 2]
        assert caseNumbers[1] in [0, 1, 2]
        assert isinstance(token, str)
        assert token in [' ', 'X', 'O']

        if self.getWritableOfBoard(boardNumbers):
            if self.getWritableOfCase(boardNumbers, caseNumbers):
                self.boards[boardNumbers[0], boardNumbers[1]].addToken(caseNumbers, token)
                self.addMoveInHistory(boardNumbers, caseNumbers, token)

                if self.boards[boardNumbers[0], boardNumbers[1]].isWinning(token):



    def changeWritableForNextMove(self, caseNumbers):
        for boardNumbers in self.boards:
            if boardNumbers != caseNumbers:
                self.setWritableOfBoard(boardNumbers, False)
        self.setWritableOfBoard(caseNumbers, True)

    def getLastMoveFromHistory(self):
        if len(self.movesHistory) >= 1:
            return self.movesHistory[-1]

    def getCurrentPlayerToken(self):
        return self.game.currentPlayer.getToken()
