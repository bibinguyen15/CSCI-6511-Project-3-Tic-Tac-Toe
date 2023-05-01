import numpy as np
import time
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

board = Board()

s1 = time.time()
for i in range(100000):
    size = board.getSize()

e1 = time.time()
print(e1 - s1)

s2 = time.time()
for i in range(100000):
    size = board.size

e2 = time.time()

print(e2 - s2)
