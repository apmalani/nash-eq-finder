import numpy as np
import unittest
import src.equilibria

class TestSolving(unittest.TestCase):
    def test_indifference(self):
        matrix = np.array([
            [1, -1],
            [-1, 1]
        ])

        rows = [0, 1]
        cols = [0, 1]

        self.assertTrue(all(np.isclose(src.equilibria.indifference(matrix, rows, cols), np.array([0.5, 0.5]))))