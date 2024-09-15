from z3 import *

def solve_all(s: Solver, vars: dict):
    if s.check() != sat:
        return False
    print(s.to_smt2())

    cnt = 0
    while True:
        cnt += 1
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
        if cnt >= 8:
            print("Too many solutions")
            return False
        print(f'Another solution {cnt}:')

def count_eq(s, n):
    return PbEq([(i, 1) for i in s], n)

def count_le(s, n):
    return PbLe([(i, 1) for i in s], n)
