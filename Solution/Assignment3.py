from cspProblem import Variable, Constraint, CSP
from searchGeneric import Searcher1
from cspSearch import Search_from_CSP
from cspConsistency import Con_solver, Search_with_AC_from_CSP
from operator import ne, gt, ge

A = Variable('A', {1,2,3,4}, position=(0.2,0.9))
B = Variable('B', {1,2,3,4}, position=(0.8,0.9))
C = Variable('C', {1,2,3,4}, position=(1,0.4))
D = Variable('D', {1,2,3,4}, position=(0,0.4))
E = Variable('E', {1,2,3,4}, position=(0.5,0))

scheduling = CSP("scheduling", {A,B,C,D,E},
                 [Constraint([A,D], gt, "A > D"),
                  Constraint([D,E], gt, "D > E"),
                  Constraint([C,A], ne, "C != A"),
                  Constraint([C,E], gt, "C > E"),
                  Constraint([C,D], ne, "C != D", position=(0.5, 0.3)),
                  Constraint([B,A], ge, "B >= A"),
                  Constraint([B,C], ne, "B != C"),
                  Constraint([C,D], lambda c,d : c != d + 1, "C != D+1", position=(0.5, 0.5))
                 ])

scheduling.show() #Constraint Graph

searcher = Searcher1(Search_from_CSP(scheduling))
print(searcher.search())    #search three

print("\n\n\n")

s1 = Search_with_AC_from_CSP(scheduling) #Arc Consistency
   
print("\n\n\n")

Con_solver.max_display_level = 4
Con_solver(scheduling).solve_one(s1.domains)  #Arc Consistency and splitting domain

