#Name: quizGameUnitTest.py
#Purpose: tests to help document code
#Author: Joshua Djakaria
import quizGame
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_points(self):
        testGame = quizGame()
        #tests the amount of points when right
        self.assertEqual(0, testGame.get_points())

    def test_right_wrong(self):
        testGame = quizGame()
        #tests point values when right and wrong
        testGame.setThreshold(5)
        self.assertEqual(0, testGame.get_points())
        testGame.get_right()
        self.assertEqual(1, testGame.get_points())
        testGame.get_wrong()
        self.assertEqual(0, testGame.get_points())
        testGame.get_right()
        self.assertEqual(1, testGame.get_points())
        for i in range (4):
            testGame.get_right()
            self.assertEqual(i+2, testGame.get_points())
        testGame.get_wrong()
        self.assertEqual(5, testGame.get_points())

if __name__ == '__main__':
    unittest.main()