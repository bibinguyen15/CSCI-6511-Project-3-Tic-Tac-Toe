import unittest
import math
from Project_3_Cat import *


class Test(unittest.TestCase):
    # Checking the win() function
    # if board is empty
    def testWin0(self):
        game = TTT(3, 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, None, "Expected: None")

    # win with vertical X
    def testWin1(self):
        game = TTT(3, 3)
        game.setBoard("X--\nX--\nX--\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    # win with vertical O
    def testWin2(self):
        game = TTT(3, 3)
        game.setBoard("O--\nO--\nO--\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    # win with vertical X column 2

    def testWin3(self):
        game = TTT(3, 3)
        game.setBoard("-X-\n-X-\n-X-\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    # win with vertical O column 2
    def testWin4(self):
        game = TTT(3, 3)
        game.setBoard("-O-\n-O-\n-O-\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    # win with vertical X column 3
    def testWin5(self):
        game = TTT(3, 3)
        game.setBoard("--X\n--X\n--X\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    # win with vertical O column 3
    def testWin6(self):
        game = TTT(3, 3)
        game.setBoard("--O\n--O\n--O\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    # Horizontal X tests
    def testWin7(self):
        game = TTT()
        game.setBoard("XXX\n---\n---\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    def testWin8(self):
        game = TTT()
        game.setBoard("---\nXXX\n---\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    def testWin9(self):
        game = TTT()
        game.setBoard("---\n---\nXXX\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    # Horizontal O tests
    def testWin10(self):
        game = TTT()
        game.setBoard("OOO\n---\n---\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    def testWin11(self):
        game = TTT()
        game.setBoard("---\nOOO\n---\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    def testWin12(self):
        game = TTT()
        game.setBoard("---\n---\nOOO\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    # Diagonal X tests:
    def testWin13(self):
        game = TTT()
        game.setBoard("X--\n-X-\n--X\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    def testWin14(self):
        game = TTT()
        game.setBoard("--X\n-X-\nX--\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'X', "Expected: X")

    # Diagonal O tests
    def testWin15(self):
        game = TTT()
        game.setBoard("--O\n-O-\nO--\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'O', "Expected: O")

    def testWin16(self):
        game = TTT()
        game.setBoard("O--\n-O-\n--O\n", 3)
        result = game.win(game.available)
        print(result)
        self.assertEqual(result, 'O', "Expected: O")


def unitTest():
    unitTest = unittest.TestSuite()

    # TestSuite represents an aggregation of individual test cases
    for i in range(17):
        name = 'testWin' + str(i)

        unitTest.addTest(Test(name))

    return unitTest


'''
def main():
    game = TTT(6, 4)

    game.setBoard("X--\nX--\nX--\n", 3)
    # game.setBoard("O-----------\nOO----------\n---O--------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n")
    game.drawBoard()
    print(game.win(game.available))

    print("Winner is:", game.win(game.available))
'''

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(unitTest())
    # main()
