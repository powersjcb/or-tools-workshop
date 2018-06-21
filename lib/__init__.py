import itertools
from ortools.constraint_solver import pywrapcp
import numpy as np


def print_matrix(matrix):
    for row in matrix:
        print(''.join([str(v.Value()) for v in row]))


def chunks(matrix):
    m = np.array(matrix)
    result = []
    for i in range(3):
        for j in range(3):
            result.append(m[i * 3:i * 3 + 3, j * 3: j * 3 + 3])
    return result


def main():
    solver = pywrapcp.Solver('Sudoku')
    matrix = [[solver.IntVar(1, 9, 'Cell') for _ in range(9)] for _ in range(9)]
    for submatrix in chunks(matrix):
        submatrix_nodes = [v for v in itertools.chain(*submatrix)]
        solver.Add(solver.AllDifferent(submatrix_nodes))

    for row in matrix:
        solver.Add(solver.AllDifferent(row))

    for column in zip(*matrix[::-1]):
        solver.Add(solver.AllDifferent(column))


    decision_builder = solver.Phase(
        [v for v in itertools.chain(*matrix)],
        solver.CHOOSE_FIRST_UNBOUND,
        solver.ASSIGN_MIN_VALUE,
    )  # args: list of vars, strategy, how do we assign new values

    solver.Solve(decision_builder)
    solver.NextSolution()

    print_matrix(matrix)


if __name__ == '__main__':
    main()
