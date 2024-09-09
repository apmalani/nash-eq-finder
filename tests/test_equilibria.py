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
        
    def test_support_pairs(self):
        row_matrix = np.array([
            [1, -1],
            [-1, 1]
        ])
        col_matrix = np.array([
            [-1, 1],
            [1, -1]
        ])

        expected = [((0,), (0,)), ((0,), (1,)), ((0,), (0, 1)), ((1,), (0,)), ((1,), (1,)), ((1,), (0, 1)), ((0, 1), (0,)), ((0, 1), (1,)), ((0, 1), (0, 1))]

        self.assertEqual(list(src.equilibria.support_pairs(row_matrix, col_matrix)), expected)