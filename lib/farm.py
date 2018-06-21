from ortools.constraint_solver import pywrapcp


def main():
    solver = pywrapcp.Solver('Farm')
    cows = solver.IntVar(0, 20, 'Cows')
    chickens = solver.IntVar(0, 20, 'Chickens')

    solver.Add((cows * 4) + (chickens * 2) == 56)
    solver.Add(cows + chickens == 20)

    decision_builder = solver.Phase(
        [cows, chickens],
        solver.CHOOSE_FIRST_UNBOUND,
        solver.ASSIGN_MIN_VALUE,
    )  # args: list of vars, strategy, how do we assign new values
    solver.Solve(decision_builder)
    solver.NextSolution()
    print(f'cows: {cows.Value()} chickens: {chickens.Value()}')


if __name__ == '__main__':
    main()
