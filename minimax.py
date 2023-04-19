from tictactoe import Board
import constants
from constants import *
import numpy as np


def minimax(board, depth, isMax, alpha=constants.MIN, beta=MAX):
    # board.print()

    if board.gameOver():
        winner = board.getWinner()
        return (1000 * winner - depth if winner == 1 else 1000 * winner + depth)

    elif board.isFull():
        return 0

    elif depth == constants.maxDepth:
        score = heuristic(board)
        print(board.board, score)
        if isMax:
            return score - depth
        else:
            return score + depth

    # if not, is it the maximizing player's turn?
    if isMax:
        best = MIN

        for cell in board.available():
            # make the move
            board.add(cell, board.getUser())

            # self.drawBoard()

            # Call minimax recursively and choose the maximum value
            score = minimax(board,
                            depth + 1, False, alpha, beta)
            print("Score for", cell, board.getUser(), "=", score)

            best = max(best, score)

            alpha = max(alpha, best)

            # undo move
            board.remove(cell)

            if beta <= alpha:
                break

        return best

    # minimizer's move
    else:
        best = MAX

        for cell in board.available():
            # make the move
            board.add(cell, board.getOther())

            # self.drawBoard()

            # Call minimax recursively and choose the maximum value
            score = minimax(board,
                            depth + 1, True, alpha, beta)

            # print("Score for", cell, board.getOther(), "=", score)

            best = min(best, score)
            beta = min(beta, best)

            # undo move
            board.remove(cell)

            if beta <= alpha:
                break

        return best


def nextMove(board, player):

    if board.isEmpty():
        bestMove = [board.getSize() // 2, board.getSize() // 2]
    else:
        bestVal = MIN
        bestMove = (-1, -1)
        moveScore = {}

        board.switchUser(player)

        for cell in board.available():

            # Make the move
            board.add(cell, player)

            # Call minimax
            move = minimax(board, 0, False, MIN, MAX)

            moveScore[(cell[0], cell[1])] = move

            # Undo move
            board.remove(cell)

            if move > bestVal:
                bestMove, bestVal = cell, move

    return bestMove


def heuristic(board):
    score = 0
    target = board.getTarget()

    currentBoard = board.getBoard()
    size = board.getSize()

    # evaluate row
    for i in range(size):
        for j in range(size):
            score += eachPoint(board, [i, j], target, size)

    return score


def eachPoint(board, point, target, size):
    x, y = point
    score = 0

    # print("____Calculating heuristics____\nPoint: ", point
    # )

    row = board.board[x, y:y + target if y + target < size else size]
    if len(row) == target and not (1 in row and -1 in row):
        points = perLine(row, target)
        if abs(points) >= 200:
            return points
        score += points

    col = board.board[x:x + target if x + target < size else size, y]
    if len(col) == target and not (1 in col and -1 in col):
        points = perLine(col, target)
        if abs(points) >= 200:
            return points
        score += points

    k = min(x, y)
    left = np.diagonal(
        board.board, y - x)[k:k + target if k + target < size else size]

    if len(left) == target and not (1 in left and -1 in left):
        points = perLine(left, target)
        if abs(points) >= 200:

            return points
        score += points

    k = min(x, size - 1 - y)
    right = np.fliplr(board.board).diagonal(
        size - 1 - y - x)[k:k + target if k + target < size else size]

    if len(right) == target and not (1 in right and -1 in right):
        points = perLine(right, target)
        if abs(points) >= 200:

            return points
        score += points

    return score


def perLine(line, target):
    if 1 in line:
        turn = 1
    else:
        turn = -1

    #print("Turn:", turn)

    nonZeros = np.count_nonzero(line)

    if nonZeros == target:
        return 1000 * turn

    if nonZeros == target - 1:
        return 500 * turn
    if nonZeros == target - 2:
        return 200 * turn

    return (nonZeros * 5 + target - nonZeros) * turn


'''
game = Board()
# game.setBoard(
# "XXX----\n-------\nOOO----\n-------\n-------\nXOX--OX\nXXOOX--\n", 4)

game.setBoard("X-XO\nX-OX\nOO-X\nOOXX\n", 4)
game.print()

game.printBoard()

print(heuristic(game))

game.printBoard()
'''
