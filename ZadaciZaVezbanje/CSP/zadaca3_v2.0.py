from constraint import *


def someFunc(var1, var2, var3, var4, var5, var6, var7):

    lista = [var1, var2, var3, var4, var5, var6, var7]

    if var2.split('_')[1] == var6.split('_')[1]:
        return False


    theMainList = []
    for first in lista:
        for second in lista:
            if first != second:
                if first.split('_')[0] == second.split('_')[0]:
                    theMainList.append(first)

    if len(theMainList) == 0:
        return True

    for g in range(len(lista)):
        for j in range(g+1, len(lista)):
            if g != j:
                if lista[g].split('_')[0] == lista[j].split('_')[0]:
                    if abs(int(lista[g].split("_")[1]) - int(lista[j].split("_")[1])) < 2:
                        return False

    return True



if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    # ML_predavanja_domain = ["ml predavanja"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    # ML_vezbi_domain = ["ml vezbi"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    list_ai = ["AI_cas_" + str(i + 1) for i in range(int(casovi_AI))]
    list_ml = ["ML_cas_" + str(i + 1) for i in range(int(casovi_ML))]
    list_r = ["R_cas_" + str(i + 1) for i in range(int(casovi_R))]
    list_bi = ["BI_cas_" + str(i + 1) for i in range(int(casovi_BI))]

    problem.addVariables(list_ai, AI_predavanja_domain)
    problem.addVariables(list_ml, ML_predavanja_domain)
    problem.addVariables(list_r, R_predavanja_domain)
    problem.addVariables(list_bi, BI_predavanja_domain)

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # ----------------------------------------------------

    # print(list_ml)
    # problem.addVariable("ML_cas_1", ML_predavanja_domain)
    # problem.addConstraint(masinsko, ("ML_vezbi", "ML_cas_1"))
    # problem.addConstraint(AllDifferentConstraint(),)
    problem.addConstraint(nova, )


    solution = problem.getSolution()

    print(solution)

    nov = dict ()

    # for x in solution: