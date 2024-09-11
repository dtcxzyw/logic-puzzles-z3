# https://mp.weixin.qq.com/s/hIS2YrYp69XHIS_ddm03cQ
from z3 import *

a = Bool('a')
b = Bool('b')
c = Bool('c')

s = Solver()
s.add(Or(a, b, c))
s.add(Implies(Or(a, b), And(b, c)))
for i in [a, b, c]:
    s.push()
    s.add(Not(i))
    if s.check() == unsat:
        print(i)
    s.pop()
