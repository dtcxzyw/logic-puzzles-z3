from z3 import *

def solve_unique(s: Solver, vars: dict):
    if s.check() != sat:
        return False
    
    assign = {}
    for k, v in vars.items():
        res = s.model().eval(v)
        print(k, res)
        assign[k] = res
    
    cons = False
    for k, v in assign.items():
        cons = Or(cons, vars[k] != v)
    s.add(cons)
    if s.check() == unsat:
        return True
    print('Multiple solutions found:')
    for k, v in vars.items():
        res = s.model().eval(v)
        print(k, res)
    return False
