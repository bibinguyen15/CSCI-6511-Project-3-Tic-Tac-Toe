from tictactoe import Board
import constants

maxDepth = constants.maxDepth
MIN = float('-inf')
MAX = float('inf')


def minimax(board, depth, isMax, player, alpha=MIN, beta=MAX):

    if depth == maxDepth or board.gameOver():
        print("Game ended")
        return 10

    return 1


def nextMove(board, player):
    bestVal = MIN
    bestMove = (-1, -1)
    moveScore = {}

    board.switchUser(player)

    available = board.emptySpots()

    print("Available moves:\n", available)

    for cell in board.emptySpots():
        print("Chosen move:", cell, "x=", cell[0], "y=", cell[1])

        # Make the move
        board.add(cell, player)
        board.drawBoard()

        # Call minimax
        move = minimax(board, 0, False, MIN, MAX)

        moveScore[(cell[0], cell[1])] = move

        # Undo move
        board.remove(cell)

        if move > bestVal:
            bestMove, bestVal = cell, move

    print(moveScore)
    return bestMove

    # else:
    # bestVal = MIN
    # bestMove = (-1, -1)


