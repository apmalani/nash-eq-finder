import unittest
import src.game
import numpy as np

class TestGame(unittest.TestCase):
    def test_matrices(self):
        row = np.array([
            [1, -1],
            [-1, 1]
        ])
        col = np.array([
            [-1, 1]
        ])

        with self.assertRaises(ValueError):
            src.game.Game(row, col)

        new_game = src.game.Game(row, None)

        for result, expected in zip(new_game.matrices, (row, -row)):
            self.assertTrue(np.array_equal(result, expected))

    def test_payoffs(self):
        pass

if __name__ == '__main__':
    unittest.main()