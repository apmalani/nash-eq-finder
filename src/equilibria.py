import numpy as np
import itertools

def custom_powerset(n):
    s = range(n)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1, n + 1))

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
        probability = np.linalg.solve(constraint, target)
        if np.all(probability >= 0):
            return probability
        return False
    except np.linalg.LinAlgError as e:
        return False
    
def support_pairs(matrix):
    row_strat, col_strat = matrix.shape

    for i in custom_powerset(row_strat):
        for j in custom_powerset(col_strat):
                yield i, j

def support_obedience(strat, sup):
    if strat is False: return False
    return all(strat[i] != 0 for i in sup) and all(strat[i] == 0 for i in range(len(strat)) if i not in sup)

def generate_equilibrium(row, col):
    col_t = col.T

    for row_sup, col_sup in support_pairs(row):
        row_strats = indifference(col_t, col_sup, row_sup)
        col_strats = indifference(row, row_sup, col_sup)

        if support_obedience(row_strats, row_sup) and support_obedience(col_strats, col_sup):
                yield row_strats, col_strats, row_sup, col_sup

def solve_nash_equilibrium(row, col):
    pass
