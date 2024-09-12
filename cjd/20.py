# https://mp.weixin.qq.com/s/CTSB8Rnl2B1_bwT7O8dONQ
from z3 import *
import util

a, b, c, d, e = Bools('a b c d e')

s = Solver()
s.add(b == Not(c))
s.add(c == Not(d))
s.add(d == Not(e))
s.add(e == Not(a))

s.push()
s.add(a == b)
assert util.solve_all(s, {'a': a, 'b': b, 'c': c, 'd': d, 'e': e})
s.pop()
s.push()
s.add(a == Not(b))
assert s.check() == unsat
s.pop()
