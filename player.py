from sys import exit

class Player(object):

    def __init__(self):
        pass

    def getTurn(self, board) :
        try :
            play = int(input())
            while (play < 1 or play > 9) :
                print("Please give a number between 1 and 9.")
                play = int(input())
            return play
        except KeyboardInterrupt:
            print("You just quit. :'(")
            exit(0)
        except ValueError:
            print("Please give a number between 1 and 9.")
            return self.getTurn(board)