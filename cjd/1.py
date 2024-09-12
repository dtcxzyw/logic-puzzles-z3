# https://mp.weixin.qq.com/s/LrKd_9aupc0ffdn7TeG5MQ
from z3 import *
import util

a1, b1, c1 = Bools('a1 b1 c1') # black
a2, b2, c2 = Bools('a2 b2 c2') # white

s = Solver()
s.add(util.count_eq([a1, b1, c1], 2))
s.add(util.count_eq([a2, b2, c2], 2))
for v1, v2 in zip([a1, b1, c1], [a2, b2, c2]):
    s.add(Or(v1, v2))

s.add(Implies(a1, Not(b2)))
s.add(Implies(b1, Not(c2)))

assert util.solve_all(s, {'a1': a1, 'b1': b1, 'c1': c1, 'a2': a2, 'b2': b2, 'c2': c2})
