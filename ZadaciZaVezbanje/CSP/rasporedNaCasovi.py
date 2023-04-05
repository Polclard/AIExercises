from constraint import *

lista_zafateni = []


def someFunc(var1, var2, var3, var4, var5, var6, var7):
    lista = [var1, var2, var3, var4, var5, var6, var7]
    # print([item for item in lista])
    if var1.split("_")[0] != var2.split("_")[0] != var3.split("_")[0] != var4.split("_")[0] != var5.split("_")[0] != \
            var6.split("_")[0] != var7.split("_")[0]:
        return True

    counterTrue = 0
    counterFalse = 0

    for i in range(0, len(lista)):
        for j in range(i + 1, len(lista)):
            # print(f'{int(lista[i].split("_")[1])}')
            if (lista[i] not in lista_zafateni or lista[j] not in lista_zafateni) and lista[i].split("_")[0] == \
                    lista[j].split("_")[0] and abs(int(lista[i].split("_")[1]) - int(lista[j].split("_")[1])) >= 2:
                lista_zafateni.append(lista[j])
                return True
            else:
                pass

    # print(lista_zafateni)
    #
    # for var in lista:
    #     if var not in lista_zafateni:
    #         ...
    #     else:
    #         return False

    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    lista_predavanja_ai = []
    lista_predavanja_ml = []
    lista_predavanja_r = []
    lista_predavanja_bi = []

    for i in range(int(casovi_AI)):
        lista_predavanja_ai.append("AI_cas_" + str(i + 1))

    for i in range(int(casovi_ML)):
        lista_predavanja_ml.append("ML_cas_" + str(i + 1))

    for i in range(int(casovi_R)):
        lista_predavanja_r.append("R_cas_" + str(i + 1))

    for i in range(int(casovi_BI)):
        lista_predavanja_bi.append("BI_cas_" + str(i + 1))

    # print(lista_predavanja_ai)

    problem.addVariables(lista_predavanja_ai, AI_vezbi_domain)
    problem.addVariables(lista_predavanja_ml, ML_predavanja_domain)
    problem.addVariables(lista_predavanja_r, R_predavanja_domain)
    problem.addVariables(lista_predavanja_bi, BI_vezbi_domain)

    problem.addVariable(("AI_vezbi"), AI_vezbi_domain)
    problem.addVariable(("ML_vezbi"), ML_vezbi_domain)
    problem.addVariable(("BI_vezbi"), BI_vezbi_domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(someFunc, )

    # problem.addConstraint()

    # ----------------------------------------------------

    solution = problem.getSolution()

    print(solution)
