import math
import random

class Mulky:
    def __init__(self, breed):
        self.breed = breed

class Bulky(Mulky):
    def __init__(self, name, surname, age, breed):
        super(Bulky, self).__init__(breed)
        self.name = name
        self.surname = surname
        self.age = age
        
    def tellNameSurname(self):
        print(f"Hello my name is {self.name} and my surname is {self.surname}")

    def __str__(self):
        print(f"{self.name} {self.surname} {self.age} {self.breed}")
    

if __name__  == "__main__":
    torka = (1,2,4,5,6,78,9)
    recnik = {"Golema":"big", "Mala":"small", "Teska":"Heavy", "Silna":"Strong"}  
    listaOdTorki = [("Golema","big"), ("Mala","small"), ("Teska","Heavy"), ("Silna","Strong")]
    
    torka2 = (2,5,4,12,42,5,1231,25,2,5)
    
    # novaLista = [(element*2) for element in 
    #                 [element2-3 for element2 in torka if(element2 % 2 == 0)]]
    # print(math.sin(90))
    
    df = dict()
    
    df[tuple([1])] = [2]
    
    print(df)
    
    