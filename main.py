from tictactoe import Board
from time import *
from minimax import *

boardSize = 4
target = 4
user = 0


def main():
    game = Board(boardSize, target, user)

    game.setBoard("OOX-\nOXO-\nO--X\n----\n", 4)

    game.drawBoard()

    game.printBoard()

    game.switchUser(1)

    game.printBoard()

    game.drawBoard()

    print(nextMove(game, 0))


def localPlay():
    game = Board(boardSize, target, user)
    game.drawBoard()

    while(True):
        player = int(input("Player's turn: "))

        start = time.time()

        game.add(nextMove(game, player))

        end = time.time()
        print("Time taken", end - start, "s")
        print("__________________________________________________________________")

        gameEnd = game.win(game.available)
        if gameEnd != None:
            if gameEnd == True:
                print("It's a draw.")
            else:
                print("Winner:", gameEnd)
            print("Game ended.")
            break


if __name__ == '__main__':
    main()
