from tictactoe import Board
import time
from minimax import *
from APIFunctions import *


boardSize = 6
target = 4
user = 0


def main():
    # localPlay()

    teamId2 = '1376'
    gameId = 0
    loadGame(gameId, teamId2)


def localPlay():
    game = Board(boardSize, target, user)
    game.drawBoard()

    while(True):
        player = int(input("Player's turn: "))
        if game.getUser() != player:
            game.switchUser(player)

        if not (input("Do you want to make a move (leave empty if not)? ")):

            start = time.time()

            best = nextMove(game, player)

            end = time.time()

            print("The best calculated move is:", best)
            print("Time taken", end - start, "s")

            add = int(input("Want to make this move (1 for yes, 0 for no)? "))

            if add == 1:
                game.add(best, player)

            else:
                game.add(userMove(), player)
        else:
            game.add(userMove(), player)

        game.drawBoard()

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


def userMove():
    print("Type the move you want to make")
    x = int(input("x: "))
    y = int(input("y: "))
    return [x, y]


if __name__ == '__main__':
    main()
