from tictactoe import Board
import constants
from constants import *
import numpy as np


def heuristic(board):
    score = 0
    target = board.getTarget()

    currentBoard = board.getBoard()
    size = board.getSize()

    # evaluate row
    for row in currentBoard:
        score += perLine(row, target)

    # evaluate column
    for j in range(size):
        score += perLine(currentBoard[:, j], target)

    for i in range(1 - size, size):
        score += perLine(np.diagonal(currentBoard, i), target)
        score += perLine(np.fliplr(currentBoard).diagonal(i), target)

    # evaluate diagonal
    return score


def perLine(line, target):
    if len(line) >= target:
        print("Line being evaluated:", line)
        score, count, last, neutral = 0, 0, 0, 0
        interrupted = False

        for x in line:
            if x == 0:
                neutral += 1
                if count != 0:
                    interrupted = True
            elif x == last:
                count += 1
                if count == target and not interrupted:
                    return 1000 * x
            elif x != last and last != 0:
                if neutral + count >= target:
                    score += (count * 2 + neutral) * last
                count = 1
                last = x
                neutral = 0

            else:
                last = x
                count = 1

        return score
    return 0


def minimax(board, depth, isMax, alpha=constants.MIN, beta=MAX):

    if board.gameOver():

        winner = board.getWinner()
        board.continueGame()
        return (1000 * winner - depth if winner == 1 else 1000 * winner + depth)

    elif board.isFull():
        return 0

    elif depth == constants.maxDepth:

        return 1
        # return heuristic(board)

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


