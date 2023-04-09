from constraint import *


def check_diagonal(x, y, n1):
    forbiddenPosition = []

    c1 = y - x
    c2 = y + x

    for i in range(1, n1 + 1):
        for j in range(1, n1 + 1):
            if j - i == c1 or j + i == c2:
                forbiddenPosition.append((i, j))
    return tuple(forbiddenPosition)


def func(*args):
    print(args)

    counter = 0
    for main in args:
        counter = 0
        for other in args:
            if other != main:
                x_main = main[0]
                y_main = main[1]

                x_other = other[0]
                y_other = other[1]
                if x_main == x_other or y_main == y_other and other in check_diagonal(x_main, y_main, N_GLOBAL):
                    counter += 1

        if counter >= len(args) * len(args) - 2:
            return False
        else:
            return True


N_GLOBAL = 0

if __name__ == '__main__':
    n = int(input())
    N_GLOBAL = n
    problem = Problem(BacktrackingSolver())

    problem.addVariables(range(1, n + 1), [(x, y) for x in range(1, n) for y in range(1, n)])

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(), )
    problem.addConstraint(func, )

    # ----------------------------------------------------
    if n <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())
