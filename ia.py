class IA(object):

    def __init__(self):
        pass

    def endGame(self, board) :
        if (board[0] == board[1] == board[2] and board[0] != 0) :
            return 1
        elif (board[3] == board[4] == board[5] and board[3] != 0) :
            return 1
        elif (board[6] == board[7] == board[8] and board[6] != 0) :
            return 1
        elif (board[0] == board[3] == board[6] and board[0] != 0) :
            return 1
        elif (board[1] == board[4] == board[7] and board[1] != 0) :
            return 1
        elif (board[2] == board[5] == board[8] and board[2] != 0) :
            return 1
        elif (board[0] == board[4] == board[8] and board[0] != 0) :
            return 1
        elif (board[2] == board[4] == board[6] and board[2] != 0) :
            return 1
        elif (board.count(0) == 0) :
            return 1
        return 0

    def evaluateBoard(self, board) :
        if (board[0] == board[1] == board[2] and board[0] != 0) :
            return (-1, 1)[board[0] == 2]
        elif (board[3] == board[4] == board[5] and board[3] != 0) :
            return (-1, 1)[board[3] == 2]
        elif (board[6] == board[7] == board[8] and board[6] != 0) :
            return (-1, 1)[board[6] == 2]
        elif (board[0] == board[3] == board[6] and board[0] != 0) :
            return (-1, 1)[board[0] == 2]
        elif (board[1] == board[4] == board[7] and board[1] != 0) :
            return (-1, 1)[board[1] == 2]
        elif (board[2] == board[5] == board[8] and board[2] != 0) :
            return (-1, 1)[board[2] == 2]
        elif (board[0] == board[4] == board[8] and board[0] != 0) :
            return (-1, 1)[board[0] == 2]
        elif (board[2] == board[4] == board[6] and board[2] != 0) :
            return (-1, 1)[board[2] == 2]
        elif (board.count(0) == 0) :
            return 0

    def giveEmptyCases(self, board) :
        return [i for i in range(len(board)) if board[i] == 0]

    def Minimax(self, board, isIA) :
        if self.endGame(board) :
            return (self.evaluateBoard(board), 1)
        elif isIA :
            value = float("-inf")
            bestCase = 0
            emptyCases = self.giveEmptyCases(board)
            for i in emptyCases :
                board[i] = 2
                tmpValue = self.Minimax(board, False)[0]
                if (value < tmpValue) :
                    value = tmpValue
                    bestCase = i
                board[i] = 0
            return value, bestCase
        else :
            value = float("inf")
            worstCase = 0
            emptyCases = self.giveEmptyCases(board)
            for i in emptyCases :
                board[i] = 1
                tmpValue = self.Minimax(board, True)[0]
                if (value > tmpValue) :
                    value = tmpValue
                    worstCase = i
                board[i] = 0
            return value, worstCase

    def getTurn(self, board) :
        return self.Minimax(board, True)[1]