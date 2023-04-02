from constraint import *



if __name__ == '__main__':

    variables = ('A', 'B', 'C', 'D')
    domain = (1, 2, 3, 4, 5)

    problem = Problem(BacktrackingSolver())

    problem.addVariables(variables, domain)

    problem.addConstraint(lambda b1, b2, b3, b4: b1 < b2 < b3 < b4, variables)
    problem.addConstraint(lambda d: d % 2 != 0, ('D',))

    solutions = problem.getSolutions();

    new_dict = dict()

    for solution in solutions:
        new_dict["A"] = solution["A"]
        new_dict["B"] = solution["B"]
        new_dict["C"] = solution["C"]
        new_dict["D"] = solution["D"]
        print(f"{new_dict.values()}")
