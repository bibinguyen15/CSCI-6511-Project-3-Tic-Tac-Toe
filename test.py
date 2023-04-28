import numpy as np
import time

test = np.array([[0, 1, 1, -1], [1, -1, 1, 0],
                [1, 1, 1, 1], [-1, -1, -1, -1]])


begin1 = time.time_ns()
for k in range(1000):
    newTest = []
    for i in range(4):
        newTest.append(test[1][i])
end1 = time.time_ns()

print(newTest, end1 - begin1)

begin2 = time.time_ns()
for k in range(1000):
    newTest = []
    newTest = test[1, :]
end2 = time.time_ns()
print(newTest, end2 - begin2)
