from constraint import *

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
    
    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(("AI","ML","NLP"), domain)
    
    # Tuka dodadete gi ogranichuvanjata
    if(aiNum <= 4 and mlNum <= 4 and nlpNum <= 4):
        problem.addConstraint(AllDifferentConstraint(), ("AI","ML","NLP"))

        
    result = problem.getSolution()

    for key,value in papers.items():
        print(f"{key} ({value}): {result[value]}")


