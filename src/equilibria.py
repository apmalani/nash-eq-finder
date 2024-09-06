import numpy as np
import itertools

def powerset(n):
    s = range(n)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(n + 1))

def indifference(matrix, row_indices, column_indices):
    constraint = (matrix[np.array(row_indices)] - np.roll(matrix[np.array(row_indices)], 1, axis=0))[:-1]
    avoid = set(range(matrix.shape[1])) - set(column_indices)

    if avoid:
        avoid_constraints = np.eye(matrix.shape[1])[list(avoid)]
        constraint = np.vstack([constraint, avoid_constraints])

    constraint = np.vstack([constraint, np.ones((1, constraint.shape[1]))])
    target = np.zeros(len(constraint))
    target[-1] = 1

    try:
        probability = np.linalg.lstsq(constraint, target, rcond = None)[0]
        if np.all(probability >= 0):
            return probability
        return False
    except np.linalg.LinAlgError as e:
        return False
    
def solve_nash_equilibrium(row, col):
    pass