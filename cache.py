import numpy as np
import time


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

            return self.scores[index]
        except:
            return False
