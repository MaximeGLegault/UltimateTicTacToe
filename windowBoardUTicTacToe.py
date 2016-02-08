__author__ = 'Maxime Gagnon-Legault'
__date__ = '2016/01/10'


from tkinter import Canvas


class WindowBoard(Canvas):

    def __init__(self, parent, board, game, caseSize=60):
        self.board = board
        self.caseSize = caseSize
        self.caseRectangle = {}

        #**************************
        self.game = game


        super().__init__(parent, width=(self.board.getNumberOfLine()*self.caseSize),
                         height=(self.board.getNumberOfColumn() * self.caseSize))

        self.drawWindowBoard()

    def drawWindowBoard(self):
        for iii in range(self.board.getNumberOfLine()):
            for jjj in range(self.board.getNumberOfColumn()):
                startLine = iii * self.caseSize
                endLine = startLine + self.caseSize
                startColumn = jjj * self.caseSize
                endColumn = startColumn + self.caseSize

                self.caseRectangle[iii, jjj] = self.create_rectangle(startColumn, startLine, endColumn, endLine,
                                                                     fill='#e1e1e1', width=2, outline='white',
                                                                     tags='Rect')
    def getCaseSize(self):
        return self.caseSize

    def getBoardNumber(self):
        return self.board.parentCoordinates
