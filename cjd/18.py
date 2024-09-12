# https://mp.weixin.qq.com/s/LIRa91r_p8eDWOyT1lvggg
from z3 import *
import util

a1, b1 = Bools('a1 b1')
a2, b2 = Bools('a2 b2')

s = Solver()
s.add(util.count_eq([a1, b1], 1))
s.add(util.count_eq([a2, b2], 1))
s.add(a2 == a1)

assert util.solve_all(s, {'a1': a1, 'b1': b1, 'a2': a2, 'b2': b2})
