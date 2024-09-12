# https://mp.weixin.qq.com/s/JCEMvh5OYj2abknPp_ERUg
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

s.add(Or(a2 == -6, b2 == -6, c2 == -6))
s.add(Or(a2 == -2, b2 == -2, c2 == -2))
s.add(Or(a2 == 5, b2 == 5, c2 == 5))
s.add(Distinct(a2, b2, c2))

assert s.check() == unsat
