from tictactoe import Board
import time
from minimax import *
from APIFunctions import *
from constants import teamId2


boardSize = 3
target = 3
user = 0


def main():

    # localPlay()
    teamId2 = '1349'
    gameId = 0
    opponentStarts = False

    loadGame(gameId, teamId2, opponentStarts)


def localPlay():

    game = Board(boardSize, target, user)

    print("Starting game.\nboardSize=", boardSize,
          "| target=", target)

    game.drawBoard()
    turn = user

    while(True):
        #player = int(input("Player's turn: "))
        player = turn % 2

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

        turn += 1

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
