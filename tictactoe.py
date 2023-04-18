import numpy as np


class Board:
    def __init__(self, size=10, target=5, user=0):
        self.size = size
        self.totalMoves = size**2
        self.target = target
        self.board = np.zeros((size, size), dtype=np.int8)
        self.players = ['O', 'X']
        self.user = user
        self.other = 0 if user == 1 else 1
        self.win = False
        self.winner = -1

    def getSize(self):
        return self.size

    def getTarget(self):
        return self.target

    def getUser(self):
        return self.user

    def getOther(self):
        return self.other

    def getPlayer(self, player):
        return self.players[player]

    def continueGame(self):
        self.winner = -1
        self.win = False

    def gameOver(self):
        return self.win

    def getWinner(self):
        return self.winner

    def available(self):
        return np.argwhere(self.board == 0)

    def isFull(self):
        return True if np.count_nonzero(self.board) == self.totalMoves else False

    def isEmpty(self):
        return True if np.count_nonzero(self.board) == 0 else False

    def printBoard(self):
        print(self.board)

    def getBoard(self):
        return self.board

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

        self.win = self.checkWin(move, turn)
        if self.win:
            self.winner = turn

    def remove(self, move):
        self.board[move[0]][move[1]] = 0

    def setUser(self, user):
        self.user = user
        self.other = 0 if user == 1 else 1

    def switchUser(self, user):
        if user != self.user:
            self.user = user
            self.other = 0 if user == 1 else 1

            moves = np.argwhere(self.board != 0)

            for move in moves:
                if self.board[move[0]][move[1]] == 1:
                    self.board[move[0]][move[1]] = -1
                elif self.board[move[0]][move[1]] == -1:
                    self.board[move[0]][move[1]] = 1

    def setBoard(self, boardStr, target=-1, user=-1):
        boardStr = boardStr.split('\n')[:-1]

        if user != -1:
            self.user = user

        player = self.players[self.user]
        other = self.players[self.user - 1]

        for i in range(len(boardStr)):
            row = []
            for pos in boardStr[i]:
                if pos == '-':
                    row.append(0)
                elif pos == player:
                    row.append(1)
                else:
                    row.append(-1)
            boardStr[i] = row

        self.board = np.array(boardStr)

        self.size = len(boardStr)

        if target == -1:
            self.target = int(self.size / 2)
        else:
            self.target = target

    def checkWin(self, move, turn):

        x, y = move
        count = 0

        # Check row
        for j in range(self.size):
            if self.board[x][j] == turn:
                count += 1
                if count == self.target:
                    return True
            else:
                count = 0

        # Check column
        count = 0
        for i in range(self.size):
            if self.board[i][y] == turn:
                count += 1
                if count == self.target:
                    return True
            else:
                count = 0

        # Check diagonal
        # Top left diagonal
        count = 0
        left = np.diagonal(self.board, y - x)

        if len(left) >= self.target:
            for i in range(len(left)):
                if left[i] == turn:
                    count += 1
                    if count == self.target:
                        return True
                else:
                    count = 0

        # Top right diagonal
        count = 0

        flip = np.fliplr(self.board)

        right = np.fliplr(self.board).diagonal(self.size - 1 - y - x)

        if len(right) >= self.target:
            for i in range(len(right)):
                if right[i] == turn:
                    count += 1
                    if count == self.target:
                        return True
                else:
                    count = 0

        return False

    def print(self):
        print("Board status:\n", self.board)
        print("User is:", self.user)
        print("Other player is:", self.other)
        print("Win?", self.win, "- Winner?", self.winner)

#board = Board()


boardSize = 5
target = 4
user = 0

game = Board(boardSize, target, user)
print(user, game.getUser())

#game.setBoard("XXX--\n-----\nOOO--\n-----\n-----\n", 4)
#game.setBoard("XXO--\nXOO--\nX-O--\n-----\n-----\n", 4)
game.setBoard(
    "OXXXX-O\nO------\n-------\n-------\n-------\n-------\nO-----O\n", 5)

game.drawBoard()
game.add([0, 5], 1)
game.printBoard()
print(game.gameOver(), game.getWinner())
