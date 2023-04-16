from tictactoe import Board
import constants

#maxDepth = constants.maxDepth
maxDepth = 3
MIN = float('-inf')
MAX = float('inf')


def heuristic(board):
    score = 0

    # evaluate row
    for row in board.getBoard():
        score += perLine(row)

    # evaluate column
    return 0


def perLine(line):
    return 1


def minimax(board, depth, isMax, alpha=MIN, beta=MAX):

    if board.gameOver():

        winner = board.getWinner()
        board.continueGame()
        return (1000 * winner - depth if winner == 1 else 1000 * winner + depth)

    elif board.isFull():
        return 0

    elif depth == maxDepth:
        return heuristic(board)

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

    # else:
    # bestVal = MIN
    # bestMove = (-1, -1)


