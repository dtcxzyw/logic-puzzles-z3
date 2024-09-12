# https://mp.weixin.qq.com/s/9CPicquytAEdfT_1IS3tGg
from z3 import *
import util

a1, b1 = Bools('a1 b1')
a2, b2 = Bools('a2 b2')

s = Solver()
s.add(util.count_eq([a1, b1], 1))
s.add(Not(And(a2, b2)))
s.add(a2 == a1)
s.add(b2 == Not(b1))

assert util.solve_all(s, {'a1': a1, 'b1': b1})
