# https://mp.weixin.qq.com/s/MB9k_boV3xrso1wCcH7TMQ
from z3 import *
import util

a, b, c, d = Ints('a b c d')
e = Bool('e')
s = Solver()
for i in [a, b, c, d]:
    s.add(i >= 1, i <= 4)
s.add(Distinct(a, b, c, d))

def query(i, expr):
    return If(i == 1, expr, If(i == 4, If(e, expr, Not(expr)), Not(expr)))

s.add(query(a, a == 3))
s.add(query(b, Implies(a == 3, c == 4)))
s.add(query(c, If(c == 4, e, c == 1)))
s.add(query(d, d != 1))

assert util.solve_all(s, {'a': a, 'b': b, 'c': c, 'd': d, 'e': e})
