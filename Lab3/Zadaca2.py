from constraint import *

list_ai = []
list_ml = []
list_nlp = []


counter_termin1 = 0
counter_termin2 = 0
def func(*args):

    print(args)

    list_ai.append(args[0])
    list_ml.append(args[1])
    list_nlp.append(args[2])

    # print(f"AI: {len(list_ai}\nML: {list_ml} \nNLP: {list_nlp}\n")
    problem.addConstraint(AllEqualConstraint(),  ("AI",))
    problem.addConstraint(AllEqualConstraint(),  ("ML",))
    problem.addConstraint(AllEqualConstraint(),  ("NLP",))
    return True


    # return len(list_ai) <= 4 and len(list_ml) <= 4 and len(list_nlp) <= 4

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    aiNum = 0
    mlNum = 0
    nlpNum = 0

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        if(topic == "AI"):
            aiNum+=1
        elif(topic == "ML"):
            mlNum+=1
        else:
            nlpNum+=1
        papers[title] = topic
        paper_info = input()

    #---------------print------------------------
    # print(f"{aiNum} - {mlNum} - {nlpNum}")
    #--------------------------------------------

    # Tuka definirajte gi promenlivite

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())
    print(papers)
    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(("AI","ML","NLP"), domain)

    # Tuka dodadete gi ogranichuvanjata
    if(aiNum <= 4 or mlNum <= 4 or nlpNum <= 4):
        problem.addConstraint(AllDifferentConstraint(), ("AI", "ML", "NLP"))
    else:
        problem.addConstraint(func, ())

    result = problem.getSolution()

    print(result)

    for key,value in papers.items():
        print(f"{key} ({value}): {result[value]}")