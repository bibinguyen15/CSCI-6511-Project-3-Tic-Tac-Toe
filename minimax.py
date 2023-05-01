from tictactoe import Board
import constants
from constants import *
import numpy as np
import math
from cache import Cache


def minimax(board, depth, isMax, alpha=constants.MIN, beta=constants.MAX):
    #board.print()

    if board.win:
        winner = board.winner
        board.continueGame()
        if winner == 1:
            score = 100000 * winner - depth
        else:
            score = 100000 * winner + depth
        return score

    elif board.isFull():
        return 0

    elif depth == constants.maxDepth:
        #inCache = cache.getScore(board.board)
        #if not inCache:
        #score = heuristic(board)
        #cache.append(board.board, score)
        #else:
        #score = inCache

        score = heuristic(board)
        if isMax:
            return score + depth
        else:
            return score - depth

    possibleMoves = checkOccupied(board)
    # if not, is it the maximizing player's turn?
    if isMax:
        best = MIN

        score = []
        for move in possibleMoves:
            score.append((move, moveHeu(move, board, 1)))
        score.sort(key=lambda a: a[1], reverse=True)

        available = [move for (move, i) in score]

        for cell in available:
            # make the move
            board.add(cell, board.user)

            # Call minimax recursively and choose the maximum value
            score = minimax(board,
                            depth + 1, False, alpha, beta)

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

        score = []
        for move in possibleMoves:
            score.append((move, moveHeu(move, board, -1)))
        score.sort(key=lambda a: a[1], reverse=False)

        available = [move for (move, i) in score]

        for cell in available:
            # make the move
            board.add(cell, board.other)
            #print("Adding move:", cell)
            #board.drawBoard()

            # Call minimax recursively and choose the maximum value
            score = minimax(board,
                            depth + 1, True, alpha, beta)

            best = min(best, score)
            beta = min(beta, best)

            # undo move
            board.remove(cell)
            if beta <= alpha:
                break

        return best


def nextMove(board, player):
    if board.isEmpty():
        bestMove = [board.size // 2, board.size // 2]
    elif board.board[board.size // 2][board.size // 2] == 0:
        bestMove = [board.size // 2, board.size // 2]
    else:
        bestVal = constants.MIN
        bestMove = (-1, -1)
        moveScore = {}

        board.switchUser(player)

        possibleMoves = checkOccupied(board)

        score = []
        for move in possibleMoves:
            score.append((move, moveHeu(move, board, 1)))
        score.sort(key=lambda a: a[1], reverse=True)

        available = [move for (move, i) in score]

        for cell in available:
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


def moveHeu(move, board, turn):
    score = 0

    board.add(move, board.user if turn == 1 else board.other)

    if board.win:
        board.remove(move)
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
    while jx < board.size and jy < board.size and board.board[jx][jy] == turn:
        jx += 1
        jy += 1
    continuous = jx - ix - 1
    left = ix
    right = jx
    while ix > -1 and iy > -1 and board.board[ix][iy] != opponent:
        ix -= 1
        iy -= 1
    while jx < board.size and jy < board.size and board.board[jx][jy] == turn:
        jx += 1
        jy += 1
    if jx - right + continuous >= board.target and left - ix + continuous >= board.target:
        return (5 * continuous + jx - right + left - ix)

    elif jx - ix - 1 < board.target:
        return 0
    else:
        return 5 * continuous


def checkDiagonalLeft(move, board, turn):
    x, y = move
    ix = jx = x
    iy = jy = y
    opponent = 1 if turn == -1 else -1

    while ix > -1 and iy < board.size and board.board[ix][iy] == turn:
        ix -= 1
        iy += 1
    while jx < board.size and jy > -1 and board.board[jx][jy] == turn:
        jx += 1
        jy -= 1
    continuous = jx - ix - 1
    left = ix
    right = jx
    while ix > -1 and iy < board.size and board.board[ix][iy] != opponent:
        ix -= 1
        iy += 1
    while jx < board.size and jy > -1 and board.board[jx][jy] != opponent:
        jx += 1
        jy -= 1
    if jx - right + continuous >= board.target and left - ix + continuous >= board.target:
        return (5 * continuous + jx - right + left - ix)

    elif jx - ix - 1 < board.target:
        return 0
    else:
        return 5 * continuous


def checkRow(move, board, turn):
    x, y = move
    i = j = x
    opponent = 1 if turn == -1 else -1

    while i > -1 and board.board[i][y] == turn:
        i -= 1
    while j < board.size and board.board[j][y] == turn:
        j += 1
    continuous = j - i - 1
    left = i
    right = j
    while i > -1 and board.board[i][y] != opponent:
        i -= 1
    while j < board.size and board.board[j][y] != opponent:
        j += 1

    if j - right + continuous >= board.target and left - i + continuous >= board.target:
        return (5 * continuous + j - right + left - i)

    elif j - i - 1 < board.target:
        return 0
    else:
        return 5 * continuous


def checkCol(move, board, turn):
    x, y = move
    i = j = y
    opponent = 1 if turn == -1 else -1

    while i > -1 and board.board[x][i] == turn:
        i -= 1
    while j < board.size and board.board[x][j] == turn:
        j += 1
    continuous = j - i - 1
    left = i
    right = j

    while i > -1 and board.board[x][i] != opponent:
        i -= 1
    while j < board.size and board.board[x][j] != opponent:
        j += 1

    if j - right + continuous >= board.target and left - i + continuous >= board.target:
        return (5 * continuous + j - right + left - i)
    elif j - i - 1 < board.target:
        return 0
    else:
        return 5 * continuous


def heuristic(board):
    score = 0
    target = board.target

    size = board.size

    # evaluate row
    for i in range(size):
        for j in range(size):
            score += eachPoint(board, [i, j], target, size)

    return score


def eachPoint(board, point, target, size):
    x, y = point
    score = 0

    row = board.board[x, y:y + target if y + target < size else size]
    if len(row) == target and not (1 in row and -1 in row):
        points = perLine(row, target)
        if abs(points) >= 100000:
            return points
        score += points

    col = board.board[x:x + target if x + target < size else size, y]
    if len(col) == target and not (1 in col and -1 in col):
        points = perLine(col, target)

        if abs(points) == 100000:
            return points
        score += points

    k = min(x, y)
    left = np.diagonal(
        board.board, y - x)[k:k + target if k + target < size else size]

    if len(left) == target and not (1 in left and -1 in left):

        points = perLine(left, target)

        if abs(points) == 100000:
            return points
        score += points

    k = min(x, size - 1 - y)
    right = np.fliplr(board.board).diagonal(
        size - 1 - y - x)[k:k + target if k + target < size else size]

    if len(right) == target and not (1 in right and -1 in right):
        points = perLine(right, target)

        if abs(points) == 100000:
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
        return 100000 * turn

    if nonZeros == target - 1:
        return 500 * turn
    if nonZeros == target - 2:
        return 200 * turn

    return (nonZeros * 5 + target - nonZeros) * turn


def checkOccupied(board):
    possibleMoves = board.available()
    if board.totalMoves - len(possibleMoves) <= board.size - board.target + 2:

        moves = []
        for move in possibleMoves:
            width = board.getSize() - 1
            x, y = move

            keep = False
            count = 0

            reach = board.target // 2 + 1

            left = x - reach if x - reach >= 0 else 0
            right = x + reach if x + reach <= width else width
            top = y - reach if y - reach >= 0 else 0
            bottom = y + reach if y + reach <= width else width

            for i in range(left, right + 1):
                for j in range(top, bottom + 1):
                    if board.board[i][j] != 0:
                        keep = True
                        break
                if keep:
                    break

            if keep:
                moves.append(move)
        return moves
    return possibleMoves



