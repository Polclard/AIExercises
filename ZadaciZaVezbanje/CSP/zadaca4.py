from constraint import *

if __name__ == '__main__':
    problem = None
    a = input()
    if a == "BacktrackingSolver":
        problem = Problem(BacktrackingSolver())
    elif a == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    elif a == "MinConflictsSolver":
        problem = Problem(MinConflictsSolver())

    variables = range(0, 81)
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(1, 10))))

    # Ограничување 1: Секоја редица мора да содржи броеви од 1 до 9, каде што ниту еден број не смее да се повторува.
    for i in range(9):
        row = range(i * 9, i * 9 + 9)
        problem.addConstraint(AllDifferentConstraint(), row)

    # Ограничување 2: Секоја колона мора да содржи броеви од 1 до 9, каде што ниту еден број не смее да се повторува.
    for j in range(9):
        column = range(j, 80, 9)
        problem.addConstraint(AllDifferentConstraint(), column)

    # Ограничување 3: Секој блок мора да содржи броеви од 1 до 9, каде што ниту еден број не смее да се повторува.
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [i * 9 + j + k * 9 + l for k in range(3) for l in range(3)]
            problem.addConstraint(AllDifferentConstraint(), block)

    solutions = problem.getSolution()

    print(solutions)
