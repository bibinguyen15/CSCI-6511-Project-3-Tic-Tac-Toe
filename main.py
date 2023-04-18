from tictactoe import Board
import time
from minimax import *
from APIFunctions import *
from constants import teamId2


boardSize = 5
target = 4
user = 1


def main():

    # localPlay()

    game = Board(boardSize, target, user)
    print(user, game.getUser())

    game.setBoard("XXX--\n-----\nOOO--\n-----\n-----\n", 4)

    game.drawBoard()
    game.add([2, 3], 0)
    game.printBoard()
    print(game.gameOver(), game.getWinner())
    #gameId = 4155
    #loadGame(gameId, teamId2)
    #loadGame(gameId, teamId2, True)


def localPlay():
    game = Board(boardSize, target, user)

    print("Starting game.\nboardSize=", boardSize,
          "| target=", target)

    game.drawBoard()

    while(True):
        #player = int(input("Player's turn: "))
        player = user % 2

        print("Player's turn:", player)

        if game.getUser() != player:
            game.switchUser(player)

        if not (input("Do you want to make a move (leave empty if not)? ")):

            start = time.time()

            best = nextMove(game, player)

            end = time.time()

            print("The best calculated move is:", best)
            print("Time taken", end - start, "s")

            if not input("Want to make this move (leave empty for yes)? "):
                game.add(best, player)

            else:
                game.add(userMove(), player)
        else:
            game.add(userMove(), player)

        game.drawBoard()

        print("__________________________________________________________________")

        user += 1

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
