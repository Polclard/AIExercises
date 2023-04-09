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

    listOfGood= []

    for i in range(1, len(args)):
        for j in range(i+1, len(args)):
            if i != j:
                if (args[i] == args[j]) or (args[i][0] == args[j][0]) or (args[i][1] == args[j][1]) or (args[j] in check_diagonal(args[i][0], args[i][1], N_GLOBAL)):
                    return False
        listOfGood.append(tuple(args))
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
