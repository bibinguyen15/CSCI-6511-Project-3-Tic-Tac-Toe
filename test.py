import numpy as np
import time
from minimax import *
from tictactoe import Board
'''
class Cache():
    def __init__(self):
        self.states = []
        self.scores = []
        self.index = 0
        self.maxSize = 10000

    def append(self, state, score):
        if len(self.states) == 10000:
            self.states[self.index] = state
            self.scores[self.index] = score
        else:
            self.states.append(state)
            self.scores.append(score)
        if self.index >= self.maxSize - 1:
            self.index = 0
        else:
            self.index += 1

    def getScore(self, board):
        try:
            index = [np.array_equal(board, x)
                     for x in self.states].index(True)

            print(self.states[index], self.scores[index])
            return self.scores[index]
        except:
            return False


test = np.ones((10, 10))

cache = Cache()

find = np.zeros((10, 10))

#begin1 = time.time()
turn = 1
for k in range(2):
    cache.append((turn, test), k)
    turn *= -1

cache.append((1, find), 2000000)

print(cache.states)
begin1 = time.time()

try:
    index = [np.array_equal(test, x[1])
             for x in cache.states].index(True)
    print(index)
    print(cache.states[0])
    print(cache.states[1])
except:

    print("Not in list")


print("Scores for find list:", cache.getScore(test))

end1 = time.time()

cache2 = Cache()

flag = True
while flag:
    print(end1 - begin1, "s")
    if not input("Continue? Type yes"):
        flag = False
'''


def getScore(board, x, y, step):
    dimensions = board.getSize()
    count_player = 0
    count_opponent = 0
    score = 0
    rowArray = board.board[x:x + 1,
                           y:(y + step) if y + step < dimensions else dimensions]
    # colArray = board.board[x:(x + step) if x + step < dimensions else dimensions, y:y + 1]
    colArray = []
    i = 0
    while x + i < dimensions and len(colArray) < step:
        colArray.append(board.board[x + i][y])
        i += 1
    negativeDiagonal = []
    ndx, ndy = x, y
    count = 0
    while ndx < dimensions and ndy < dimensions and count < step:
        negativeDiagonal.append(board.board[ndx][ndy])
        ndx += 1
        ndy += 1
        count += 1
    positiveDiagonal = []
    pdx, pdy = x, y
    count = 0
    while pdx > -1 and pdy < dimensions and count < step:
        positiveDiagonal.append(board.board[pdx][pdy])
        pdx -= 1
        pdy += 1
        count += 1

    # Calculate row scores
    rowCount = 0
    rowArray = rowArray[0]
    if 1 in rowArray and -1 in rowArray:
        score += 0
    elif len(rowArray) >= step:
        for x in rowArray:
            if x == 1:
                count_player += 1
                rowCount += 1
            elif x == -1:
                rowCount -= 1
                count_opponent += 1
    # Calculate column scores
    colCount = 0
    if 1 in colArray and -1 in colArray:
        score += 0
    elif len(colArray) >= step:
        for x in colArray:
            if x == 1:
                count_player += 1
                colCount += 1
            elif x == -1:
                count_opponent += 1
                colCount -= 1
    # Calculate negative diagonal scores
    ndCount = 0
    if 1 in negativeDiagonal and -1 in negativeDiagonal:
        score += 0
    elif len(negativeDiagonal) >= step:
        for x in negativeDiagonal:
            if x == 1:
                count_player += 1
                ndCount += 1
            elif x == -1:
                count_opponent += 1
                ndCount -= 1
    # Calculate positive diagonal scores
    pdCount = 0
    if 1 in positiveDiagonal and -1 in positiveDiagonal:
        score += 0
    elif len(positiveDiagonal) >= step:
        for x in positiveDiagonal:
            if x == 1:
                count_player += 1
                pdCount += 1
            elif x == -1:
                count_opponent += 1
                pdCount -= 1
    if step > 4:
        checkStep = step - 1
    else:
        checkStep = step

    if colCount == step or rowCount == step or ndCount == step or pdCount == step:
        return 100000
    elif colCount == -step or rowCount == -step or ndCount == -step or pdCount == -step:
        return -100000
    elif colCount == checkStep or rowCount == checkStep or ndCount == checkStep or pdCount == checkStep:
        return 5000
    elif colCount == -checkStep or rowCount == -checkStep or ndCount == -checkStep or pdCount == -checkStep:
        return -5000
    else:
        # return count_player - count_opponent
        return colCount * abs(colCount) + rowCount * abs(rowCount) + ndCount * abs(ndCount) + pdCount * abs(pdCount)


def finalHeuristic(board):
    score = 0
    target = board.target

    size = board.size

    # evaluate row
    for i in range(size):
        for j in range(size):
            score += getScore(board, i, j, target)

    return score


#Aditya's
board = Board()
board.setBoard("XX--O\nOX-X-\n--O--\n--O--\n-----\n", 5)

a1 = time.time()
score = 0
for i in range(100000):
    score += finalHeuristic(board) - 3

a2 = time.time()

print(score, a2 - a1)


c1 = time.time()
score = 0
for i in range(100000):
    score += heuristic(board) - 3

c2 = time.time()

print(score, c2 - c1)
