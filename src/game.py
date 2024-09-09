import numpy as np
import src.equilibria

class Game:
    def __init__(self, row, col = None):
        if col:
            if row.shape == col.shape:
                self.matrices = (row, col)
            else:
                raise ValueError()
        else:
            self.matrices = (row, -row)

    def payoffs(self, row_strat, col_strat):
        row_payoff = np.dot(row_strat, np.dot(self.matrices[0], col_strat))
        col_payoff = np.dot(row_strat, np.dot(self.matrices[1], col_strat))

        payoffs = [row_payoff, col_payoff]

        return np.array(payoffs)
    
    def solve(self):
        return src.equilibria.solve_nash_equilibrium(*self.matrices)