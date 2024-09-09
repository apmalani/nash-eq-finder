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
        matrix = np.array([
            [1, -1],
            [-1, 1]
        ])

        expected = [((0,), (0,)), ((0,), (1,)), ((0,), (0, 1)), ((1,), (0,)), ((1,), (1,)), ((1,), (0, 1)), ((0, 1), (0,)), ((0, 1), (1,)), ((0, 1), (0, 1))]

        self.assertEqual(list(src.equilibria.support_pairs(matrix)), expected)

    def test_support_obedience(self):
        self.assertTrue(src.equilibria.support_obedience(np.array([1, -1]), np.array([0, 1])))
        self.assertFalse(src.equilibria.support_obedience(False, np.array([0, 1])))
        self.assertFalse(src.equilibria.support_obedience(np.array([0, 100]), np.array([0, 1])))

    def test_equilibria_generation(self):
        row = np.array([
            [1, -1],
            [-1, 1]
        ])
        col = np.array([
            [-1, 1],
            [1, -1]
        ])

        print(list(src.equilibria.generate_equilibrium(row, col)))