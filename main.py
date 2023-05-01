from tictactoe import Board
import time
from minimax import *
from APIFunctions import *
from constants import teamId2


boardSize = 10
target = 5
user = 0


def main():
    #localPlayAI()
    personStarts = False
    localPlayPerson(boardSize, target, personStarts)

    # localPlayAI()
    teamId2 = '1358'
    gameId = 0
    opponentStarts = False

    #loadGame(gameId, teamId2, opponentStarts)


def localPlayPerson(size, target, playerStart=False):

    print("Starting game...")

    if playerStart:
        user, opponent = 1, 0
    else:
        user, opponent = 0, 1

    # Just putting stock values for size and target because it will be override by setBoard anyways
    board = Board(size, target, user)

    board.drawBoard()
    cache = Cache()
    #board.setBoard("XX--O\nOX-X-\n--O--\n--O--\n-----\n", 5)
    #board.drawBoard()

    # if player start first
    if playerStart:
        x, y = int(input("x=")), int(input("y="))

        board.add([x, y], opponent)
        print("Your move:")
        board.drawBoard()

    while True:
        # board.print()

        start = time.time()

        bestMove = setMove(board, cache)

        end = time.time()

        print("Time taken", end - start, "s")

        board.add(bestMove, user)
        # board.print()

        print("AI move:")
        board.drawBoard()

        # board.print()

        if board.win or board.isFull():
            print("Game ended.\nWinner:", board.winner)
            return

        x, y = int(input("x=")), int(input("y="))

        while board.board[x][y] != 0:
            x, y = int(input("x=")), int(input("y="))

        board.add([x, y], opponent)
        print("Your move:")

        board.drawBoard()

        if board.win or board.isFull():
            print("Game ended.")
            if board.winner:
                print("Winner:", board.winner)

            return

        # board.print()


def setMove(board, cache):
    available = len(board.available())
    if available > board.totalMoves - board.target - 1:
        #if available > 80:
        constants.maxDepth = 1
    elif available > 30:
        constants.maxDepth = 2
    elif available > 20:
        constants.maxDepth = 3
    elif available > 10:
        constants.maxDepth = 4
    else:
        constants.maxDepth = 10

    bestMove = nextMove(board, board.user, cache)
    # board.print()
    # print("Best move is:", bestMove)

    return bestMove


def localPlayAI():

    game = Board(boardSize, target, user)

    print("Starting game.\nboardSize=", boardSize,
          "| target=", target)

    game.drawBoard()
    turn = user

    while(True):
        #player = int(input("Player's turn: "))
        player = turn % 2

        print("Player's turn:", player)

        if game.user != player:
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
        elif game.win:
            print("Winner:", end=" ")
            if game.winner == 1:
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
