from constraint import *

'''
Потребно е да составите тим кој се состои од 1 тим лидер и 5 членови. 
Членовите се избираат од множество на N1 можни членови. Тим лидерот се
избира од множество на N2 можни тим лидери. Притоа, секој член и тим 
лидер има одредена тежина (реална вредност помеѓу 0 и 100). 
Ваша задача е да креирате оптимален тим. Оптимален тим е тимот 
чија сума на тежини е највисока. Дополнително, сумата не требада 
биде поголема од 100. Не е можно еден тим лидер или еден член дасе избере повеќе од еднаш.

Од стандарден влез се чита бројот на можни членови, а потоа се
читаат информации за секој член во следниот формат „тежина име“.
Потоа, се чита бројот на можни тим лидери и информациите за 
секој тим лидер во следниот формат „тежина име“.

На стандарден излез да се испечати вкупната сума за формираниот тим.
Потоа да се испечатат тим лидерот и членовите на тимот.
'''
'''
10
31.3 A
28.4 B
26.1 C
24.2 D
21.8 E
20.3 F
15.5 G
14.1 H
12.5 I
11.5 J
5
32.2 K
27.4 L
24.6 M
14.9 N
13.2 O
'''


class List:
    def __init__(self):
        self.list = list()
        self.maximumValue = 0

    def __setList__(self, new_list):
        self.list = new_list

    def __setMaximumValue__(self, new_maximum_value):
        self.maximumValue = maxSum

maxSum = 0
total = 0
naj = []
def someFunc(*args):
    global total
    total = 0
    list_same = []

    for i in range(0, len(args)):
        for j in range(0, len(args)):
            if i != j:
                if args[i].split(" ")[1] == args[j].split(" ")[1]:
                    list_same.append(args[i].split(" ")[1])
                    return False

    for item in args:
        total += float(item.split(" ")[0])


    #returning False if the sum is greater than 100
    if total > 100:
        return False

    #returning the maximum value 100 or less than 100
    global maxSum
    global naj
    if total == 100:
        return True
    else:
        if maxSum < total:
            maxSum = total
            naj = ([item for item in args])
        else:
            return False

    return naj



if __name__ == '__main__':
    # N1 = int(input())
    # N2 = int(input())
    problem = Problem(BacktrackingSolver())

    lista_timlideri = []
    lista_rabotnici = []

    for x in range(int(input())):
        lista_rabotnici.append(input())

    for y in range(int(input())):
        lista_timlideri.append(input())

    for z in range(0, 5):
        problem.addVariable("Participant " + str(z + 1) + ":", lista_rabotnici)

    problem.addVariable("Team leader:", lista_timlideri)


    # problem.addConstraint(AllDifferentConstraint(),)
    problem.addConstraint(someFunc, )

    solution = problem.getSolution()

    if solution == None:
        solution = naj
        total = maxSum
        print(solution)
    else:
        print("Total score: " + str(total))
        for key, value in solution.items():
            print(f"{key} {value.split(' ')[1]}")
