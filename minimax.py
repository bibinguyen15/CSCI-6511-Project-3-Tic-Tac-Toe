from tictactoe import Board
import constants
from constants import *
import numpy as np
import math


def sortMoves(available, board, turn):
    score = []
    for move in available:
        score.append((move, moveHeu(move, board, turn)))
    score.sort(key=lambda a: abs(a[1]), reverse=True)
    print(score)
    return [move for (move, i) in score]


def moveHeu(move, board, turn):
    score = 0

    board.add(move, board.user if turn == 1 else board.other)

    if board.gameOver():
        return 10000 * turn

    score += checkCol(move, board, turn) + checkRow(move, board, turn) + \
        checkDiagonalLeft(move, board, turn) + \
        checkDiagonalRight(move, board, turn)

    board.remove(move)

    return score * turn


def checkDiagonalRight(move, board, turn):
    x, y = move
    ix = jx = x
    iy = jy = y
    opponent = 1 if turn == -1 else -1

    while ix > -1 and iy > -1 and board.board[ix][iy] == turn:
        ix -= 1
        iy -= 1
    while jx < board.getSize() and jy < board.getSize() and board.board[jx][jy] == turn:
        jx += 1
        jy += 1
    continuous = jx - ix - 1
    left1 = ix
    right1 = jx
    while ix > -1 and iy > -1 and board.board[ix][iy] != opponent:
        ix -= 1
        iy -= 1
    while jx < board.getSize() and jy < board.getSize() and board.board[jx][jy] == turn:
        jx += 1
        jy += 1
    if jx - right1 + continuous >= board.getTarget() and left1 - ix + continuous >= board.getTarget():
        return 4 ** continuous
    elif jx - ix - 1 < board.getTarget():
        return 0
    else:
        return math.pow(4, (continuous - 1))


def checkDiagonalLeft(move, board, turn):
    x, y = move
    ix = jx = x
    iy = jy = y
    opponent = 1 if turn == -1 else -1

    while ix > -1 and iy < board.getSize() and board.board[ix][iy] == turn:
        ix -= 1
        iy += 1
    while jx < board.getSize() and jy > -1 and board.board[jx][jy] == turn:
        jx += 1
        jy -= 1
    continuous = jx - ix - 1
    left1 = ix
    right1 = jx
    while ix > -1 and iy < board.getSize() and board.board[ix][iy] != opponent:
        ix -= 1
        iy += 1
    while jx < board.getSize() and jy > -1 and board.board[jx][jy] != opponent:
        jx += 1
        jy -= 1
    if jx - right1 + continuous >= board.getTarget() and left1 - ix + continuous >= board.getTarget():
        return 4 ** continuous
    elif jx - ix - 1 < board.getTarget():
        return 0
    else:
        return math.pow(4, (continuous - 1))


def checkRow(move, board, turn):
    x, y = move
    i = j = x
    opponent = 1 if turn == -1 else -1

    while i > -1 and board.board[i][y] == turn:
        i -= 1
    while j < board.getSize() and board.board[j][y] == turn:
        j += 1
    continuous = j - i - 1
    left = i
    right = j
    while i > -1 and board.board[i][y] != opponent:
        i -= 1
    while j < board.getSize() and board.board[j][y] != opponent:
        j += 1

    if j - right + continuous >= board.getTarget() and left - i + continuous >= board.getTarget():
        return 4**continuous
    elif j - i - 1 < board.getTarget():
        return 0
    else:
        return math.pow(4, (continuous - 1))


def checkCol(move, board, turn):
    x, y = move
    i = j = y
    opponent = 1 if turn == -1 else -1

    while i > -1 and board.board[x][i] == turn:
        i -= 1
    while j < board.getSize() and board.board[x][j] == turn:
        j += 1
    continuous = j - i - 1
    left1 = i
    right1 = j

    while i > -1 and board.board[x][i] != opponent:
        i -= 1
    while j < board.getSize() and board.board[x][j] != opponent:
        j += 1

    if j - right1 + continuous >= board.getTarget() and left1 - i + continuous >= board.getTarget():
        return 4**continuous
    elif j - i - 1 < board.getTarget():
        return 0
    else:
        return math.pow(4, (continuous - 1))


def minimax(board, depth, isMax, alpha=constants.MIN, beta=constants.MAX):
    board.print()

    if board.gameOver():
        winner = board.getWinner()
        return (10000 * winner - depth if winner == 1 else 10000 * winner + depth)

    elif board.isFull():
        return 0

    elif depth == constants.maxDepth:
        # elif depth == 100:
        print(depth)
        score = heuristic(board)
        print(board.board, score)
        if isMax:
            return score + depth
        else:

            return score - depth

    # if not, is it the maximizing player's turn?
    if isMax:
        best = MIN

        available = sortMoves(board.available(), board, 1)

        for cell in available:
            # make the move
            board.add(cell, board.getUser())

            board.drawBoard()

            # Call minimax recursively and choose the maximum value
            score = minimax(board,
                            depth + 1, False, alpha, beta)

            board.drawBoard()
            #print("Score for", cell, "[", board.getUser(), "] =", score)

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

        available = sortMoves(board.available(), board, -1)

        for cell in available:
            # make the move
            board.add(cell, board.getOther())

            board.drawBoard()

            # Call minimax recursively and choose the maximum value
            score = minimax(board,
                            depth + 1, True, alpha, beta)

            board.drawBoard()
            #print("Score for", cell, "[", board.getOther(), "] =", score)

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
        bestVal = constants.MIN
        bestMove = (-1, -1)
        moveScore = {}

        board.switchUser(player)

        for cell in board.available():
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n",
                  "Evaluating the move:", cell)

            # Make the move
            board.add(cell, player)

            # Call minimax
            move = minimax(board, 0, False, MIN, MAX)

            moveScore[(cell[0], cell[1])] = move

            # Undo move
            board.remove(cell)
            print("Move value:", move,
                  "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------\n")

            if move > bestVal:
                bestMove, bestVal = cell, move

        print("\nAll moves:", moveScore)

        #print("Best move for us:", bestMove, "with value:", bestVal)

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

    #print("__Calculating heuristics__\nPoint: ", point)

    row = board.board[x, y:y + target if y + target < size else size]
    if len(row) == target and not (1 in row and -1 in row):
        points = perLine(row, target)
        #print("Row:", row, "=", points)
        if abs(points) >= 10000:
            return points
        score += points

    col = board.board[x:x + target if x + target < size else size, y]
    if len(col) == target and not (1 in col and -1 in col):
        points = perLine(col, target)
        #print("Col:", col, "=", points)
        if abs(points) == 10000:
            return points
        score += points

    k = min(x, y)
    left = np.diagonal(
        board.board, y - x)[k:k + target if k + target < size else size]

    if len(left) == target and not (1 in left and -1 in left):

        points = perLine(left, target)
        #print("Left diag:", left, "=", points)
        if abs(points) == 10000:
            return points
        score += points

    k = min(x, size - 1 - y)
    right = np.fliplr(board.board).diagonal(
        size - 1 - y - x)[k:k + target if k + target < size else size]

    if len(right) == target and not (1 in right and -1 in right):
        points = perLine(right, target)
        print("Right:", right, "=", points)
        if abs(points) == 10000:
            return points
        score += points

    return score


def perLine(line, target):
    if 1 in line:
        turn = 1
    else:
        turn = -1

    nonZeros = np.count_nonzero(line)

    if nonZeros == target:
        return 10000 * turn

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
