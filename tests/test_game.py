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
        row = np.array([
            [1, -1],
            [-1, 1]
        ])

        game = src.game.Game(row)

        row_strat = np.array([0, 1])
        col_strat = np.array([1, 0])

        self.assertTrue(np.array_equal(game.payoffs(row_strat, col_strat), np.array([-1, 1])))

if __name__ == '__main__':
    unittest.main()