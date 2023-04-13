from tictactoe import Board
import constants

#maxDepth = constants.maxDepth
maxDepth = 10
MIN = float('-inf')
MAX = float('inf')


def heuristic(board):
    score = 0

    # evaluate row
    for row in board.getBoard():
        score += self.perLine(row)

    # evaluate column
    return 0


def minimax(board, depth, isMax, player, alpha=MIN, beta=MAX):
    board.printBoard()
    if board.gameOver():
        print("winner is", board.getWinner())

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
        # print("The move for maximizing player", player,
        # "at depth:", depth, "Scores:")
        for cell in board.available():
            # make the move
            board.add(cell, player)

            # self.drawBoard()

            # Call minimax recursively and choose the maximum value
            score = minimax(board,
                            depth + 1, False, player, alpha, beta)

            best = max(best, score)

            alpha = max(alpha, best)

            # undo move
            board.remove(cell)

            if beta <= alpha:
                break

        print("Chosen", best, "for maximizing")
        return best

    # minimizer's move
    else:
        best = MAX

        for cell in board.available():
            other = 0 if player == 1 else 1
            print(other)
            # make the move
            board.add(cell, other)

            # self.drawBoard()

            # Call minimax recursively and choose the maximum value
            score = minimax(board,
                            depth + 1, True, player, alpha, beta)

            best = min(best, score)
            beta = min(beta, best)

            # undo move
            board.remove(cell)

            if beta <= alpha:
                break

        print("Chosen", best, "for minimizing")
        return best


def nextMove(board, player):
    bestVal = MIN
    bestMove = (-1, -1)
    moveScore = {}

    board.switchUser(player)

    for cell in board.available():
        print("Chosen move:", cell, "x=", cell[0], "y=", cell[1])

        # Make the move
        board.add(cell, player)

        board.drawBoard()
        board.printBoard()

        # Call minimax
        move = minimax(board, player, False, MIN, MAX)

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


