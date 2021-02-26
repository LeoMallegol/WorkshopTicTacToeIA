from random import randint
from player import Player
from ia import IA

class Game(object):
    def __init__(self):
        self._board = [0] * 9
        self._end = 0
        self._turn = 0 # default value, 0 for player, 1 for IA
        self.defineWhosFirst()
        self._player = Player()
        self._ia = IA()

    def defineWhosFirst(self) :
        self._turn = randint(0,1)
        print("The " + ("IA", "Player")[self._turn == 0] + " will be the first to play this game.")

    def getSymbol(self, number) :
        return (("X", "O")[self._board[number] == 1], " ")[self._board[number] == 0]

    def printBoard(self) :
        print(" %s | %s | %s" %(self.getSymbol(0), self.getSymbol(1), self.getSymbol(2)))
        print("-----------")
        print(" %s | %s | %s" %(self.getSymbol(3), self.getSymbol(4), self.getSymbol(5)))
        print("-----------")
        print(" %s | %s | %s" %(self.getSymbol(6), self.getSymbol(7), self.getSymbol(8)))

    def playerTurn(self) :
        self.printBoard()
        print("It's your turn to play. Select a number between 1 and 9 which is available")
        play = self._player.getTurn(self._board)
        while (self._board[play - 1] != 0) :
            print("Please select an available number.")
            play = self._player.getTurn(self._board)
        print("You have play at the case %i" %play)
        self._board[play - 1] = self._turn + 1

    def IATurn(self) :
        play = self._ia.getTurn(self._board)
        print("The IA plays at the case %i" %play)
        self._board[play - 1] = self._turn + 1

    def endGame(self) :
        if (self._board[0] == self._board[1] == self._board[2]) :
            self._end = self._board[0]
        elif (self._board[3] == self._board[4] == self._board[5]) :
            self._end = self._board[3]
        elif (self._board[6] == self._board[7] == self._board[8]) :
            self._end = self._board[6]
        elif (self._board[0] == self._board[3] == self._board[6]) :
            self._end = self._board[0]
        elif (self._board[1] == self._board[4] == self._board[7]) :
            self._end = self._board[1]
        elif (self._board[2] == self._board[5] == self._board[8]) :
            self._end = self._board[8]
        elif (self._board[0] == self._board[4] == self._board[8]) :
            self._end = self._board[4]
        elif (self._board[2] == self._board[4] == self._board[6]) :
            self._end = self._board[4]
        elif (self._board.count(0) == 0) :
            self._end = 3

    def printWinner(self) :
        if self._end == 1 :
            print("You win the game. Congratulations.")
        elif self._end == 2 :
            print("The IA wins the game.")
        elif self._end == 3 :
            print("It's a tie.")

    def run(self) :
        while(self._end == 0 ):
            if self._turn == 0 :
                self.playerTurn()
            elif self._turn == 1 :
                self.IATurn()
            self._turn = (self._turn + 1) % 2
            self.endGame()
        self.printBoard()
        self.printWinner()