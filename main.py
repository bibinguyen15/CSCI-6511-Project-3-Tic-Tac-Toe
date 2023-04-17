from API import makeMove
from APIFunctions import intialLoadGame
from tictactoe import Board
import time
from minimax import *
from constants import teamId2


def main():
    #game = Board(boardSize, target, user)

    # game.drawBoard()

    # game.printBoard()

    # game.switchUser(1)

    # game.printBoard()

    # game.drawBoard()

    #print(nextMove(game, 1))
    # localPlay(gameId)
    # team2id = 1362
    gameId = 0
    intialLoadGame(gameId, teamId2)


if __name__ == '__main__':
    main()
