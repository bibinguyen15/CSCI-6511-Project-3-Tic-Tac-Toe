import numpy as np


class Board:
    def __init__(self, size=10, target=10, user=0):
        self.size = size
        self.totalMoves = size**2
        self.target = target
        self.board = np.zeros((size, size), dtype=np.int8)
        self.players = ['O', 'X']
        self.user = user
        self.over = False

    def gameOver(self):
        return self.over

    def emptySpots(self):
        return np.argwhere(self.board == 0)

    def isFull(self):
        return True if np.count_nonzero(self.board) == self.totalMoves else False

    def isEmpty(self):
        return True if np.count_nonzero(self.board) == 0 else False

    def printBoard(self):
        print(self.board)

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

    def add(self, move, player):
        if player == self.user:
            self.board[move[0]][move[1]] = 1
            turn = 1
        else:
            self.board[move[0]][move[1]] = -1
            turn = -1

        self.over = self.checkGameOver(move, turn)

    def remove(self, move):
        self.board[move[0]][move[1]] = 0

    def setUser(self, user):
        self.user = user

    def switchUser(self, user):
        if user != self.user:
            self.user = user

            moves = np.argwhere(self.board != 0)

            for move in moves:
                if self.board[move[0]][move[1]] == 1:
                    self.board[move[0]][move[1]] = -1
                elif self.board[move[0]][move[1]] == -1:
                    self.board[move[0]][move[1]] = 1

    def setBoard(self, board, target=-1, user=0):
        board = board.split('\n')[:-1]

        self.user = user
        player = self.players[self.user]
        other = self.players[self.user - 1]

        for i in range(len(board)):
            row = []
            for pos in board[i]:
                if pos == '-':
                    row.append(0)
                elif pos == player:
                    row.append(1)
                else:
                    row.append(-1)
            board[i] = row

        self.board = np.array(board)

        self.size = len(board)

        if target == -1:
            self.target = int(self.size / 2)
        else:
            self.target = target

    def checkGameOver(self, move, turn):

        x, y = move
        count = 0

        # Check row
        for j in range(self.size):
            if self.board[x][j] == turn:
                count += 1
            else:
                count = 0

        if count == self.target:
            return True

        # Check column
        count = 0
        for i in range(self.size):
            if self.board[i][y] == turn:
                count += 1
            else:
                count = 0

        if count == self.target:
            return True

        # Check diagonal
        count = 0

        return False
