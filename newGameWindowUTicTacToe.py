__author__ = 'Maxime Gagnon-Legault'
__date__ = '2015/01/10'


from tkinter import *
import tkinter.messagebox
from gameUTicTacToe import Game
from playerTicTacToe import Player

class StartNewGameWindow():

    def __init__(self, parent, game):

        self.game = game
        self.parent = parent
        self.namePlayer1 = StringVar()
        self.namePlayer2 = StringVar()
        self.tokenPlayer1 = StringVar()
        self.tokenPlayer2 = StringVar()
        self.typePlayer1 = StringVar()
        self.typePlayer2 = StringVar()
        self.goAhead = False


        self.newGameOptionWindow = Toplevel(self.parent)
        self.newGameOptionWindow.grab_set()
        self.newGameOptionWindow.title("New Game Options")
        self.newGameOptionWindow.resizable(width=False, height=False)

        Label(self.newGameOptionWindow, text="1st player").grid(row=0, column=0, padx=5, pady=5)
        Label(self.newGameOptionWindow, text="2nd player").grid(row=2, column=0, padx=5, pady =5)

        self.namePlayer1.set("Human")
        self.namePlayer2.set("Computer")
        Label(self.newGameOptionWindow, text="1st Player").grid(row=0, column=0, padx=5, pady=5)
        Label(self.newGameOptionWindow, text="2nd Player").grid(row=2, column=0, padx=5, pady =5)
        self.entryPlayer1 = Entry(self.newGameOptionWindow, textvariable=self.namePlayer1, width=14)
        self.entryPlayer2 = Entry(self.newGameOptionWindow, textvariable=self.namePlayer2, width=14)

        self.tokenPlayer1.set("X")
        self.tokenPlayer2.set("O")
        Label(self.newGameOptionWindow, text="Token:").grid(row=0, column=1, padx=5)
        self.tokenButtonPlayer1 = Button(self.newGameOptionWindow, textvariable=self.tokenPlayer1, height=2, width=2, command=self.switchPlayerToken)
        self.tokenButtonPlayer2 = Button(self.newGameOptionWindow, textvariable=self.tokenPlayer2, height=2, width=2, command=self.switchPlayerToken)

        self.typePlayer1.set("human")
        Label(self.newGameOptionWindow, text="Type:").grid(row=0, column=2, padx=5)
        self.typePlayerFrame1 = Frame(self.newGameOptionWindow)
        self.typeRadioButtonPlayerHuman1 = Radiobutton(self.typePlayerFrame1, text="Human", variable=self.typePlayer1, value="human")
        self.typeRadioButtonPlayerComputer1 = Radiobutton(self.typePlayerFrame1, text="Computer", variable=self.typePlayer1, value="computer")
        self.typePlayer2.set("computer")
        self.typePlayerFrame2 = Frame(self.newGameOptionWindow)
        self.typeRadioButtonPlayerHuman2 = Radiobutton(self.typePlayerFrame2, text="Human", variable=self.typePlayer2, value="human")
        self.typeRadioButtonPlayerComputer2 = Radiobutton(self.typePlayerFrame2, text="Computer", variable=self.typePlayer2, value="computer")

        self.acceptButton = Button(self.newGameOptionWindow, text="Accept", height=2, width=6, command=self.acceptOptionAndStartReturn)
        self.cancelButton = Button(self.newGameOptionWindow, text="Cancel", height=2, width=6, command=self.newGameOptionWindow.destroy)


        self.entryPlayer1.grid(row=1, column=0, padx=5)
        self.entryPlayer2.grid(row=3, column=0, padx=5)
        self.tokenButtonPlayer1.grid(row=1, column=1, padx=5)
        self.tokenButtonPlayer2.grid(row=3, column=1, padx=5)
        self.typePlayerFrame1.grid(row=1, column=2, padx=5)
        self.typeRadioButtonPlayerHuman1.grid(row=0, column=0, padx=5)
        self.typeRadioButtonPlayerComputer1.grid(row=1, column=0, padx=5)
        self.typePlayerFrame2.grid(row=3, column=2, padx=5)
        self.typeRadioButtonPlayerHuman2.grid(row=0, column=0, padx=5)
        self.typeRadioButtonPlayerComputer2.grid(row=1, column=0, padx=5)
        self.acceptButton.grid(row=1, column=3, padx=5)
        self.cancelButton.grid(row=3, column=3, padx=5)
        self.newGameOptionWindow.protocol("WM_DELETE_WINDOW", self.on_closing)



    def switchPlayerToken(self):
        if self.tokenPlayer1.get() == "X":
            self.tokenPlayer1.set("O")
            self.tokenPlayer2.set("X")
        else:
            self.tokenPlayer1.set("X")
            self.tokenPlayer2.set("O")

    def acceptOptionAndStartReturn(self):
        if self.typePlayer1.get() == "computer" and self.typePlayer2.get() == "computer":
            tkinter.messagebox.showinfo("Error", "Please have at least one human player.")
            return
        if self.namePlayer1.get() == self.namePlayer2.get():
            tkinter.messagebox.showinfo("Error", "Please have two different name for the players.")
            return
        self.player1 = Player(self.namePlayer1.get(), self.typePlayer1.get(), self.tokenPlayer1.get())
        self.player2 = Player(self.namePlayer2.get(), self.typePlayer2.get(), self.tokenPlayer2.get())
        self.game = Game()
        self.game.addPlayer(self.player1)
        self.game.addPlayer(self.player2)
        self.game.setStarterPlayer()
        self.goAhead = True
        self.show()

    def show(self):
        if not self.goAhead:
            self.newGameOptionWindow.wait_window()
        else:
            self.newGameOptionWindow.destroy()
        return self.game

    def on_closing(self):
        self.goAhead = True
        self.show()

