from constraint import *


def func(S, E, N, D, M, O, R, Y):
    SEND = D + 10 * N + 100 * E + 1000 * S
    MORE = E + 10 * R + 100 * O + 1000 * M

    MONEY = Y + 10 * E + 100 * N + 1000 * O + 10000 * M
    if SEND + MORE == MONEY:
        return True
    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint())

    problem.addConstraint(func, ())

    # ----------------------------------------------------

    print(problem.getSolution())
