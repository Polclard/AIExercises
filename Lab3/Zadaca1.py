from constraint import *

if __name__ == '__main__':
    problem = Problem()
    
    # ---------------------------------------------------
    problem.addVariable("Simona_prisustvo", [0,1])
    problem.addVariable("Marija_prisustvo", [0,1])
    problem.addVariable("Petar_prisustvo", [0,1])
    problem.addVariable("vreme_sostanok", range(12, 20))
    # ----------------Add constrains here-----------------
    
    problem.addConstraint(InSetConstraint([1]), ("Simona_prisustvo",))
    problem.addConstraint(SomeInSetConstraint([1]), ("Marija_prisustvo","Petar_prisustvo"))
    # problem.addConstraint(InSetConstraint([13,14,16,19]), ("vreme_sostanok",))

    problem.addConstraint(lambda m,p,v: (p == 0 and m == 1 and v in [14]) or (m == 0 and p == 1 and v in [13,16,19]), ( "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok")) 
    
    prb = problem.getSolutions()
    
    nov = dict()
    
    for solution in prb:
        nov["Simona_prisustvo"] = solution["Simona_prisustvo"]
        nov["Marija_prisustvo"] = solution["Marija_prisustvo"]
        nov["Petar_prisustvo"] = solution["Petar_prisustvo"]
        nov["vreme_sostanok"] = solution["vreme_sostanok"]
        print(nov) 

    
    
    # [print(solution) for solution in problem.getSolutions()]
