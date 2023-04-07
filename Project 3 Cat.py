class TTT:
    def __init__(self, boardSize, target):
        self.boardSize = boardSize
        self.target = target
        self.players = ['O', 'X']
        self.board = [['-'] * boardSize] * boardSize
        self.available = []
        for x in range(boardSize):
            for y in range(boardSize):
                self.available.append([x, y])
        # print(self.available)

    def drawBoard(self):
        for row in self.board:

            print("|", end="")
            for i in row:
                print(i, end="|")
            print()
        print(self.boardSize, self.target)

    def setBoard(self, board, target=-1):
        self.board = board.split('\n')[:-1]
        self.available = []

        # Make the new board according to string
        for i in range(len(self.board)):
            self.board[i] = [*self.board[i]]
            # Make sure available has the new available spots
            for j in range(len(self.board)):
                if self.board[i][j] == '-':
                    self.available.append([i, j])
        print(self.available)

        print(self.board)
        self.boardSize = len(self.board)
        if target == -1:
            self.target = int(self.boardSize / 2)
        else:
            self.target = target

    def heu(self):
        return 1

    def next(self, current):
        return 0

    def win(self):
        winner = ''
        adjacent = [self.board[0][0], 0]

        # First check row
        for row in self.board:
            adjacent = [row[0], 0]
            for item in row:
                # if match
                if item == adjacent[0] and item != '-':
                    adjacent[1] += 1
                    print(adjacent)
                    if adjacent[1] == self.target:
                        return item
                else:
                    adjacent = [item, 1]

        # Check column
        for j in range(self.boardSize):
            adjacent = [self.board[0][j], 0]
            for i in range(self.boardSize):
                if self.board[i][j] == adjacent[0] and self.board[i][j] != '-':
                    adjacent[1] += 1
                    if adjacent[1] == self.target:
                        return self.board[i][j]
                else:
                    adjacent = [self.board[i][j], 1]

        # Check diagonal
        for i in range(self.boardSize):
            for j in range(self.boardSize + 1 - self.target):
                if (i + self.target) <= self.boardSize:
                    print("Down right diagonal")
                    value = [[self.board[i + k][j + k]]
                             for k in range(self.target)]
                    print(value)
                    if all(elem == value[0] for elem in value) and value[0] != '-':
                        return value[0]
                elif(i - self.target + 1) >= 0:
                    print("Down left diagonal", i, j)
                    value = [[self.board[i - k][j + k]]
                             for k in range(self.target)]
                    print(value)
                    if all(elem == value[0] for elem in value) and value[0] != '-':
                        return value[0]

        # Check tie
        if len(self.available) == 0:
            return True


def main():
    game = TTT(6, 4)

    game.setBoard("--O\n-OX\nOOX\n", 3)
    # game.setBoard("O-----------\nOO----------\n---O--------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n")
    game.drawBoard()
    print("Winner is:", game.win())


if __name__ == '__main__':
    main()
