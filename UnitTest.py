import unittest
import math
from Project_3_Cat import *


class Test(unittest.TestCase):
    # if board is empty
    def testWin0(self):
        game = TTT(3, 3)
        result = game.win()
        print(result)
        self.assertEqual(result, None, "Expected: None")

    # win with vertical X column 1
    def testWin1(self):
        game = TTT(3, 3)
        game.setBoard("X--\nX--\nX--\n", 3)
        result = game.win()
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    # win with vertical O
    def testWin2(self):
        game = TTT(3, 3)
        game.setBoard("O--\nO--\nO--\n", 3)
        result = game.win()
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    # win with vertical X column 2

    def testWin3(self):
        game = TTT(3, 3)
        game.setBoard("-X-\n-X-\n-X-\n", 3)
        result = game.win()
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    # win with vertical O column 2
    def testWin4(self):
        game = TTT(3, 3)
        game.setBoard("-O-\n-O-\n-O-\n", 3)
        result = game.win()
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    # win with vertical X column 3
    def testWin5(self):
        game = TTT(3, 3)
        game.setBoard("--X\n--X\n--X\n", 3)
        result = game.win()
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    # win with vertical O column 3
    def testWin6(self):
        game = TTT(3, 3)
        game.setBoard("--O\n--O\n--O\n", 3)
        result = game.win()
        print(result)
        self.assertEqual(result, 'O', "Expected: O")


def unitTest():
    unitTest = unittest.TestSuite()

    # TestSuite represents an aggregation of individual test cases
    for i in range(6):
        name = 'testWin' + str(i)

        unitTest.addTest(Test(name))

    return unitTest


def main():
    game = TTT(6, 4)

    game.setBoard("X--\nX--\nX--\n", 3)
    # game.setBoard("O-----------\nOO----------\n---O--------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n")
    game.drawBoard()
    print(game.win())

    print("Winner is:", game.win())


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(unitTest())
    main()
