# https://mp.weixin.qq.com/s/LIRa91r_p8eDWOyT1lvggg
from z3 import *
import util

a, b, c, d = Bools('a b c d')

s = Solver()
s.add(If(a, d, Not(a == d)))
s.add(b == Not(d))
s.add(c == d)

assert util.solve_all(s, {'a': a, 'b': b, 'c': c, 'd': d})
