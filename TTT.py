import numpy as np


class TTT:
    def __init__(self, size=10, target=10, user=0):
        self.size = size
        self.totalMoves = size**2
        self.target = target
        self.board = np.zeros((size, size), dtype=np.int8)
        print(self.board)
        self.players = ['O', 'X']
        self.user = user

    def emptySpots(self):
        return np.argwhere(self.board == 0)

    def isFull(self):
        return True if np.count_nonzero(self.board) == self.totalMoves else False

    def isEmpty(self):
        return True if np.count_nonzero(self.board) == 0 else False

    def drawBoard(self):
        for row in self.board:
            print("|", end="")
            for i in row:
                if i == 0:
                    i = '-'
                elif i == 1:
                    i = self.players[self.user]
                else:
                    i = self.players[self.user - 1]
                print(i, end="|")
            print()

    def setBoard(self, board, target=-1):
        board = board.split('\n')[:-1]

        # Make the new board according to string
        for i in range(len(self.board)):
            self.board[i] = [*self.board[i]]
            # Make sure available has the new available spots
            for j in range(len(self.board)):
                if self.board[i][j] == '-':
                    self.available.append([i, j])
        # print(self.available)

        print(self.board)
        self.size = len(self.board)
        if target == -1:
            self.target = int(self.size / 2)
        else:
            self.target = target


game = TTT()
print(game.emptySpots())
game.drawBoard()

print(game.isEmpty())
