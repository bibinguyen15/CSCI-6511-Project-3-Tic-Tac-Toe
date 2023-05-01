import time
from API import *

from minimax import nextMove
from tictactoe import Board


def loadGame(gameId, teamId2, opponentFirst=False):
    # Flag is true while game is still going on
    flag = True

    print("Starting game...\nGameId:", gameId)

    if opponentFirst:
        user, opponent = 1, 0
    else:
        user, opponent = 0, 1

    # Create new game?
    if gameId == 0:
        gameId = createAGame(teamId2, constants.boardSize, constants.target)
        print(gameId)
        if gameId == 'FAIL':
            print("Failed to create game!")
            return False
        else:
            newGame = True
    else:
        newGame = False

    boardStr, target = getBoardString(gameId)
    # Just putting stock values for size and target because it will be override by setBoard anyways
    board = Board(constants.boardSize, constants.target, user)
    board.setBoard(boardStr, target)
    board.drawBoard()

    # if we did not create the game
    if not newGame and opponentFirst:
        print("Wait for first move...")
        while getMoves(gameId) == 'FAIL':
            time.sleep(2)

        time.sleep(1)
        lastMove = getMoves(gameId)
        x, y = lastMove['x'], lastMove['y']

        board.add([x, y], opponent)
        board.drawBoard()

    while flag:
        #board.print()

        time.sleep(1)
        bestMove = setMove(gameId, board)

        moveStatus = makeMove(moveToStr(bestMove), gameId)
        #board.print()
        while moveStatus['code'] == 'FAIL':
            time.sleep(2)
            if 'Game is no longer open' in moveStatus['message']:
                print("Game ended.")
                flag = False
                return
            elif 'It is not the turn of team' in moveStatus['message']:
                lastMove = getMoves(gameId)
                print("Waiting for move...")
                while lastMove['teamId'] != teamId2:
                    time.sleep(3)
                    lastMove = getMoves(gameId)
                x, y = lastMove['x'], lastMove['y']

                board.add([x, y], opponent)
                board.drawBoard()
                bestMove = setMove(gameId, board)

            #board.print()
            moveStatus = makeMove(moveToStr(bestMove), gameId)

        board.add(bestMove, user)
        print("Player move:")
        board.drawBoard()

        #board.print()


        if board.win or board.isFull():
            print("Game ended.\nWinner:", board.winner)
            #return

        lastMove = getMoves(gameId)
        print("Waiting for move...")
        while lastMove['teamId'] != teamId2:
            time.sleep(3)
            lastMove = getMoves(gameId)

        x, y = lastMove['x'], lastMove['y']
        board.add([x, y], opponent)

        #board.print()

        print("Opponent move:")

        board.drawBoard()


def setMove(gameId, board):
    available = len(board.available())

    #print("Game ID is:", gameId)

    if available > 30:
        constants.maxDepth = 2
    elif available > 25:
        constants.maxDepth = 3
    elif available > 20:
        constants.maxDepth = 4
    elif available > 10:
        constants.maxDepth = 5
    else:
        constants.maxDepth = 10

    bestMove = nextMove(board, board.user)
    #board.print()
    #print("Best move is:", bestMove)

    return bestMove


def moveToStr(move):
    return str(move[0]) + ',' + str(move[1])
