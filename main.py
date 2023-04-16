from tictactoe import Board
import time
from minimax import *

boardSize = 10
target = 5
user = 0


def main():
    #game = Board(boardSize, target, user)

    # game.drawBoard()

    # game.printBoard()

    # game.switchUser(1)

    # game.printBoard()

    # game.drawBoard()

    #print(nextMove(game, 1))
    localPlay()


def localPlay():
    game = Board(boardSize, target, user)
    game.drawBoard()

    while(True):
        player = int(input("Player's turn: "))
        if game.getUser() != player:
            game.switchUser(player)

        start = time.time()

        game.add(nextMove(game, player), player)

        end = time.time()

        game.drawBoard()
        print("Time taken", end - start, "s")
        print("__________________________________________________________________")

        if game.isFull():
            print("It's a draw.")
            break
        elif game.gameOver():
            print("Winner:", end=" ")
            if game.getWinner() == 1:
                print(game.getPlayer(player))
            else:
                print(game.getPlayer(player - 1))
            break


if __name__ == '__main__':
    main()
