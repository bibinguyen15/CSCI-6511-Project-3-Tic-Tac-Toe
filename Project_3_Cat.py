import time
from API import API
import json
import copy


MIN = float('-inf')
MAX = float('inf')


class TTT:
    def __init__(self, size=3, target=3):
        self.size = size
        self.target = target
        self.players = ['O', 'X']
        self.board = []
        # self.board = [['-'] * size] * size
        self.available = []
        for x in range(size):
            row = []
            for y in range(size):
                row.append('-')
                self.available.append([x, y])
            self.board.append(row)
        # print(self.available)

    def drawBoard(self):
        for row in self.board:

            print("|", end="")
            for i in row:
                print(i, end="|")
            print()

        # print("Game details:", self.size, "-", self.target)

    def setBoard(self, board, target=-1):
        self.board = board.split('\n')[:-1]
        self.available = []

        # Make the new board according to string
        for i in range(len(self.board)):
            self.board[i] = [*self.board[i]]
            # Make sure available has the new available spots
            for j in range(len(self.board)):
                if self.board[i][j] == '-':
                    self.available.append([i, j])
        # print(self.available)

        print(self.board)
        self.size = len(self.board)
        if target == -1:
            self.target = int(self.size / 2)
        else:
            self.target = target

    def makeMove(self, move, player):
        self.available.remove(list(move))

        self.board[move[0]][move[1]] = self.players[player]
        self.drawBoard()

    def heu(self, player):
        score = 0

        # evaluate row:
        for row in self.board:
            score += self.perLine(row, player)

        # evaluate column
        for j in range(self.size):
            score += self.perLine([self.board[i][j]
                                  for i in range(self.size)], player)

        # evaluate diagonal
        dStart = -(self.size - self.target)
        dEnd = -dStart

        for i in range(dStart, dEnd + 1):

            score += self.perLine([self.board[k][i + k] for k in range(
                max(-i, 0), min(self.size, self.size - i))], player)

            score += self.perLine([self.board[j][self.size - j - i - 1]
                                  for j in range(max(-i, 0), min(self.size, self.size - i))], player)

        return score

    def perLine(self, line, player):
        points = {self.players[player]: 1, self.players[player - 1]: -1}

        score, count, last, neutral = 0, 0, 0, 0
        interrupted = False

        for x in line:

            if x == '-':
                neutral += 1
                if count != 0:
                    interrupted = True
            elif x == last:
                count += 1
                if count == self.target and not interrupted:
                    return 100 * points[x]
            elif (x == 'O' or x == 'X') and last != 0:
                if neutral + count >= self.target:
                    score += count * points[last]
                count = 1
                last = x
                neutral = 0
            else:
                last = x
                count = 1

        if neutral + count >= self.target and last != 0:
            score += count * points[last]

        return score
#
#

    def next(self, player):
        if len(self.available) == self.size ** 2:
            bestMove = (0, 0)
        elif [1, 1] in self.available:
            bestMove = (1, 1)
        else:
            bestVal = MIN
            bestMove = (-1, -1)
            moveScore = {}

            # Trying to find the best move for "player"
            for cell in self.available:
                print("Available moves:", self.available, "chosen move:", cell)

                # Make the move
                self.board[cell[0]][cell[1]] = self.players[player]
                self.drawBoard()

                currentAvai = self.available.copy()
                currentAvai.remove(cell)

                # compute minimax of this move
                move = self.minimax(0, False, player, currentAvai, MIN, MAX)

                moveScore[tuple(cell)] = move
                # Undo the move
                self.board[cell[0]][cell[1]] = '-'

                # If the current move is better, then update

                if move > bestVal:
                    bestMove, bestVal = tuple(cell), move

            print(bestMove, "Move scores:", moveScore)
        return bestMove
#

    def minimax(self, depth, isMax, player, available, alpha, beta):
        end = self.win(available)
        print("End", end)

        # if the game has ended
        if (end != None):
            if end == self.players[player]:
                return 100 - depth
            elif end == self.players[player - 1]:
                return -100 + depth
            else:
                return 0

        if depth == 7:
            heu = self.heu(player)
            if heu >= 0:
                return heu - depth
            else:
                return heu + depth

        print("Depth:", depth, "- Player priority:", self.players[player],
              "- Is maximzing?", isMax)

        # if not, is it the maximizing player's turn?
        if isMax:
            best = MIN
            # print("The move for maximizing player", player,
            # "at depth:", depth, "Scores:")
            for cell in available:
                # make the move
                self.board[cell[0]][cell[1]] = self.players[player]

                currentAvai = available.copy()
                currentAvai.remove(cell)

                # self.drawBoard()

                # Call minimax recursively and choose the maximum value
                score = self.minimax(
                    depth + 1, False, player, currentAvai, alpha, beta)
                best = max(best, score)

                alpha = max(alpha, best)

                print("Score:", score)

                # undo move
                self.board[cell[0]][cell[1]] = '-'

                if beta <= alpha:
                    break

            print("Chosen", best, "for maximizing")
            return best

        # minimizer's move
        else:
            best = MAX

            for cell in available:
                # make the move
                self.board[cell[0]][cell[1]] = self.players[player - 1]

                currentAvai = available.copy()
                currentAvai.remove(cell)

                # self.drawBoard()

                # call minimax and choose minimum value
                score = self.minimax(
                    depth + 1, True, player, currentAvai, alpha, beta)
                best = min(best, score)
                beta = min(beta, best)

                print("Score:", score)

                # undo move
                self.board[cell[0]][cell[1]] = '-'

                if beta <= alpha:
                    break

            print("Chosen", best, "for minimizing")
            return best

    #
    def win(self, available):

        winner = ''
        adjacent = [self.board[0][0], 0]

        # First check row
        for row in self.board:
            adjacent = [row[0], 0]
            empty = 0
            for item in row:
                if item != '-':
                    # if match
                    if item == adjacent[0]:
                        adjacent[1] += 1
                        # print(adjacent)
                        if adjacent[1] == self.target:
                            return item
                    else:
                        adjacent = [item, 1]

        # Check column
        for j in range(self.size):
            adjacent = [self.board[0][j], 0]
            for i in range(self.size):
                if self.board[i][j] != '-':
                    if self.board[i][j] == adjacent[0]:
                        adjacent[1] += 1
                        if adjacent[1] == self.target:
                            return self.board[i][j]
                    else:
                        adjacent = [self.board[i][j], 1]

        # Check diagonal
        for i in range(self.size):
            for j in range(self.size + 1 - self.target):
                if self.board[i][j] != '-':
                    if (i + self.target) <= self.size:
                        value = [self.board[i + k][j + k]
                                 for k in range(self.target)]

                        if all(elem == value[0] for elem in value):
                            return value[0]
                    elif(i - self.target + 1) >= 0:

                        value = [self.board[i - k][j + k]
                                 for k in range(self.target)]

                        if all(elem == value[0] for elem in value):
                            return value[0]

        # Check tie
        if len(available) == 0:
            return True


def processString(gameId):
    strMap = json.loads(API.getBoardString(gameId))
    print(strMap)
    board, target = strMap['output'], strMap['target']

    return board, target


def sendToAPI(game):
    board, target = processString('3975')

    game.setBoard(board, target)
    game.drawBoard()

    move = game.next(0)
    print(move)
    move = str(move[0]) + ',' + str(move[1])

    API.makeMove(move)


def main():
    game = TTT()

    sendToAPI(game)

    # game.setBoard("X--\n-O-\nX--\n", 3)

    # game.setBoard("X--\nOO-\nX--\n", 3)

    # game.setBoard("X--\nOOX\nX--\n", 3)

    # game.setBoard("XO-\nOOX\nX--\n", 3)

    # game.setBoard("----\n-O--\n----\n----\n", 3)

    # game.setBoard("OOX-\nXXO-\nO--X\n----\n", 3)

    # game.drawBoard()


'''
    #print(game.perLine(['O', 'O', 'O', '-'], 0))

    print("Winner is:", game.win(game.available))

    while(True):
        player = int(input("Player: "))
        start = time.time()
        game.makeMove(game.next(player), player)
        end = time.time()
        print("Time taken", end - start, "s")
        print("__________________________________________________________________")

        gameEnd = game.win(game.available)
        if gameEnd != None:
            if gameEnd == True:
                print("It's a draw.")
            else:
                print("Winner:", gameEnd)
            print("Game ended.")
            break

'''

if __name__ == '__main__':
    main()
