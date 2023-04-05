class TTT:
    def __init__(self, boardSize, target):
        self.boardSize = boardSize
        self.target = target
        self.players = ['O', 'X']
        self.board = [['-'] * boardSize] * boardSize

    def drawBoard(self):
        for row in self.board:

            print("|", end="")
            for i in row:
                print(i, end="|")
            print()
        print(self.boardSize, self.target)

    def setBoard(self, board):
        self.board = board.split('\n')[:-1]
        self.boardSize = len(self.board)
        self.target = int(self.boardSize / 2)


def main():
    game = TTT(3, 3)

    game.setBoard("O-----------\nOO----------\n---O--------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n")
    game.drawBoard()


if __name__ == '__main__':
    main()
