import time
from API import API
import json


class TTT:
    def __init__(self, boardSize=3, target=3):
        self.boardSize = boardSize
        self.target = target
        self.players = ['O', 'X']
        self.board = []
        #self.board = [['-'] * boardSize] * boardSize
        self.available = []
        for x in range(boardSize):
            row = []
            for y in range(boardSize):
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

        # print("Game details:", self.boardSize, "-", self.target)

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
        self.boardSize = len(self.board)
        if target == -1:
            self.target = int(self.boardSize / 2)
        else:
            self.target = target

    def makeMove(self, move, player):
        self.available.remove(list(move))

        self.board[move[0]][move[1]] = self.players[player]
        self.drawBoard()

    def heu(self):
        return 1

    def next(self, player):
        bestVal = float('-inf')
        bestMove = (-1, -1)

        # Trying to find the best move for "player"
        for cell in self.available:
            # Make the move
            self.board[cell[0]][cell[1]] = self.players[player]
            self.drawBoard()
            self.available.remove(cell)

            # computer minimax of this move
            move = self.minimax(0, False, player)

            # Undo the move
            self.board[cell[0]][cell[1]] = '-'
            self.available.append(cell)

            # If the current move is better, then update

            if move > bestVal:
                bestMove, bestVal = tuple(cell), move
        print(bestMove)
        return bestMove
#

    def minimax(self, depth, isMax, player):
        end = self.win()
        print("End", end)

        # if the game has ended
        if (end != None):
            if end == self.players[player]:
                print("Returning 10")
                return 10
            elif end == self.players[player - 1]:
                print("Returning -10")
                return -10
            else:
                print("Returning 0")
                return 0

        self.drawBoard()
        # if not, is it the maximizing player's turn?
        if isMax:
            best = float('-inf')
            # print("The move for maximizing player", player,
            # "at depth:", depth, "Scores:")
            for cell in self.available:
                # make the move
                self.board[cell[0]][cell[1]] = self.players[player]
                self.available.remove(cell)

                print("Depth:", depth, "\nPlayer's turn:", self.players[player],
                      "is maximzing?", isMax)
                self.drawBoard()

                score = self.minimax(depth + 1, False, player)
                best = max(best, score)
                print(score, end=", ")

                # Call minimax recursively and choose the maximum value
                # best=max(best, self.minimax(depth + 1, False, player))
                print("Score:", score)

                # undo move
                self.board[cell[0]][cell[1]] = '-'
                self.available.append(cell)
            print("Chosen", best, "for maximizing")
            return best

        # minimizer's move
        else:
            best = float('inf')

            for cell in self.available:
                # make the move
                self.board[cell[0]][cell[1]] = self.players[player - 1]
                self.available.remove(cell)

                print("Depth:", depth, "\nPlayer's turn:", self.players[player - 1],
                      "is maximzing?", isMax)
                self.drawBoard()

                score = self.minimax(depth + 1, True, player)
                best = min(best, score)
                print(score, end=", ")

                # call minimax and choose minimum value
                # best = min(best, self.minimax(depth + 1, True, player))
                print("Score:", score)

                # undo move
                self.board[cell[0]][cell[1]] = '-'
                self.available.append(cell)

            print("Chosen", best, "for minimizing")
            return best

    #

    def win(self):
        # because there's no way the game can complete
        # without at least reaching target *2 - 1 moves
        if(True):
            # sif (len(self.available) + self.target) >= (self.boardSize**2):
            # if len(self.available) + 2 * self.target - 1 >= self.boardSize ** 2:
            winner = ''
            adjacent = [self.board[0][0], 0]

            # First check row
            for row in self.board:
                adjacent = [row[0], 0]
                for item in row:
                    # if match
                    if item == adjacent[0] and item != '-':
                        adjacent[1] += 1
                        # print(adjacent)
                        if adjacent[1] == self.target:
                            return item
                    else:
                        adjacent = [item, 1]

            # Check column
            for j in range(self.boardSize):
                adjacent = [self.board[0][j], 0]
                for i in range(self.boardSize):
                    if self.board[i][j] == adjacent[0] and self.board[i][j] != '-':
                        adjacent[1] += 1
                        if adjacent[1] == self.target:
                            return self.board[i][j]
                    else:
                        adjacent = [self.board[i][j], 1]

            # Check diagonal
            for i in range(self.boardSize):
                for j in range(self.boardSize + 1 - self.target):
                    if (i + self.target) <= self.boardSize:
                        value = [self.board[i + k][j + k]
                                 for k in range(self.target)]

                        if all(elem == value[0] for elem in value) and value[0] != '-':
                            return value[0]
                    elif(i - self.target + 1) >= 0:

                        value = [self.board[i - k][j + k]
                                 for k in range(self.target)]

                        if all(elem == value[0] for elem in value) and value[0] != '-':
                            return value[0]

            # Check tie
            if len(self.available) == 0:
                return True


def processString(gameId):
    strMap = json.loads(API.getBoardString(gameId))
    print(strMap)
    board, target = strMap['output'], strMap['target']

    return board, target


def sendToAPI(game):
    board, target = processString('3887')

    game.setBoard(board, target)

    move = game.next(0)
    print(move)
    move = str(move[0]) + ',' + str(move[1])

    API.makeMove(move)


def main():
    game = TTT()

    sendToAPI(game)
    #game.setBoard("X--\n-O-\nX--\n", 3)

    #game.setBoard("X--\nOO-\nX--\n", 3)

    #game.setBoard("X--\nOOX\nX--\n", 3)

    #game.setBoard("XO-\nOOX\nX--\n", 3)

    #game.setBoard("XO-\nOOX\nXX-\n", 3)
    # game.setBoard("O-----------\nOO----------\n---O--------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n")
    game.drawBoard()

    '''
    print("Winner is:", game.win())

    while(True):
        player = int(input("Player: "))
        start = time.time_ns()
        game.makeMove(game.next(player), player)
        end = time.time_ns()
        print("Time taken", end - start, "ns")
        print("__________________________________________________________________")
        if game.win() != None:
            print(game.win())
            print(game.available)

            print("Game ended.")
            break
            '''


if __name__ == '__main__':
    main()
