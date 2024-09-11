# https://mp.weixin.qq.com/s/0ejszItibziJdDN6COYNNg
from z3 import *
import util

a1, b1, c1 = Ints('a1 b1 c1')
a2, b2, c2 = Ints('a2 b2 c2') # +: faster, -: slower

s = Solver()
s.add(b1 - a1 == 1)
s.add(c1 - b1 == 2)

s.add(a1 + a2 == 0)
s.add(b1 + b2 == 10)
s.add(c1 + c2 == -3)

s.add(Or(a2 == -8, b2 == -8, c2 == -8))
s.add(Or(a2 == -2, b2 == -2, c2 == -2))
s.add(Or(a2 == 7, b2 == 7, c2 == 7))
s.add(Distinct(a2, b2, c2))

assert util.solve_all(s, {"a1": a1, "b1": b1, "c1": c1, "a2": a2, "b2": b2, "c2": c2})
