__author__ = 'Maxime Gagnon-Legault'
__date__ = "2016/01/10"


from tkinter import *
from windowBoardUTicTacToe import WindowBoard
from gameUTicTacToe import Game
from newGameWindowUTicTacToe import StartNewGameWindow
from playerTicTacToe import Player


class Window(Tk):

    def __init__(self):
        super().__init__()
        self.title("Ultimate Tic-Tac-Toe")
        self.resizable(width=False, height=False)

        #change game opener
        self.startNewDefaultGame()



        self.windowBoard = {}
        self.createWindowLayout()
        self.createWindowBoard()
        self.showWritableBoards()

    def createWindowLayout(self):
        self.frm_button = Frame(self, padx=5, pady=5)
        self.frm_button.grid(row=0, column=0, sticky=W, columnspan=2)
        self.btn_newgame = Button(self.frm_button, text="New Game", command=self.newGame)
        self.btn_newgame.grid(row=0, column=0, sticky=W, padx=5)
        self.btn_opengame = Button(self.frm_button, text="Open Game", command=self.openGame)
        self.btn_opengame.grid(row=0, column=1, sticky=W, padx=5)
        self.btn_savegame = Button(self.frm_button, text="Save Game", command=self.saveGame)
        self.btn_savegame.grid(row=0, column=2, sticky=W, padx=5)
        self.btn_rules = Button(self.frm_button, text="Rules", command=self.rules)
        self.btn_rules.grid(row=0, column=3, sticky=W, padx=5)

        self.frm_historique = Frame(self, padx=5, pady=5)
        self.frm_historique.grid(row=2, column=4, rowspan=3)

        self.scr_historique = Scrollbar(self.frm_historique, orient=VERTICAL)
        self.lst_historique = Listbox(self.frm_historique, height=25, width=25, yscrollcommand=self.scr_historique.set)
        self.scr_historique.config(command=self.lst_historique.yview)
        self.scr_historique.grid(row=1, column=1, sticky=N+S)
        self.lst_historique.grid(row=1, column=0, sticky=N+S+E+W)

        self.messages = Label(self)
        self.messages.grid(columnspan=3)

    def createWindowBoard(self):
        for i in range(0, 3):
            for j in range(0, 3):
                frame = Frame(self, borderwidth=5, relief=GROOVE)
                frame.grid(row=i+2, column=j, pady=5)
                self.windowBoard[i, j] = WindowBoard(frame, self.game.getBoard(i, j), self.game)
                self.windowBoard[i, j].grid()
                self.windowBoard[i, j].bind('<Button-1>', self.selectMove)
        """TODO check this
        messages = Label(self)
        messages.grid(columnspan=3)
        """

    def newGame(self):
        self.game = StartNewGameWindow(self, self.game).show()

    def startNewDefaultGame(self):
        self.game = Game()
        self.game.addPlayer(Player("John", "human", "X"))
        self.game.addPlayer(Player("Ass", "human", "O"))
        self.game.setStarterPlayer()

    def openGame(self):
        pass

    def saveGame(self):
        pass

    def rules(self):
        pass

    def selectMove(self, event):
        """
        Function that process a click on the board.
        :param event tkinter event that spawned the funtion calls:
        :return:
        """
        lineOfTheSelectedCase = event.y // event.widget.getCaseSize()
        columnOfTheSelectedCase = event.x // event.widget.getCaseSize()
        caseNumbers = (lineOfTheSelectedCase, columnOfTheSelectedCase)
        boardNumbers = event.widget.getBoardNumber()

        if self.writeMove(boardNumbers, caseNumbers, event):
            print("ok")


        self.messages.config(foreground='black')
        self.messages.config(text="Plateau: {} {}  Case: {} {}".format(event.widget.getBoardNumber()[0],
                                                                       event.widget.getBoardNumber()[1],
                                                                       lineOfTheSelectedCase, columnOfTheSelectedCase))
    def checkForValidBoard(self, boardNumbers):
        """

        :param boardNumbers:
        :return (bool)True or False, the writable state of the board:
        """
        return self.game.getWritableOfBoard(boardNumbers)

    def checkForValidCase(self, boardNumbers, caseNumbers):
        """

        :param boardNumbers:
        :param caseNumbers:
        :return (bool)True or False, the writable state of the case:
        """
        return self.game.getWritableOfCase(boardNumbers, caseNumbers)

    def writeMove(self, boardNumbers, caseNumbers, event):
        """

        :param boardNumbers:
        :param caseNumbers:
        :param event:
        :return:
        """
        if self.checkForValidBoard(boardNumbers):
            if self.checkForValidCase(boardNumbers, caseNumbers):
                self.addToken(boardNumbers, caseNumbers, event)
                return True
        return False

    def addToken(self, boardNumbers, caseNumbers, event):

        self.game.addToken(boardNumbers, caseNumbers, self.game.players[0].token)
        coordonnee_y = caseNumbers[0] * event.widget.getCaseSize() + event.widget.getCaseSize() // 2
        coordonnee_x = caseNumbers[1] * event.widget.getCaseSize() + event.widget.getCaseSize() // 2
        #TODO change this
        event.widget.create_text(coordonnee_x, coordonnee_y, text=self.game.players[0].token,
                                 font=('Helvetica', event.widget.getCaseSize()//2), tags='pion')

    def showWritableBoards(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.game.getWritableOfBoard((i, j)) == True:
                    self.windowBoard[i, j].itemconfig("Rect", fill='light green')
