# https://mp.weixin.qq.com/s/4nLtLpXPahJzQJxHQsEerg
from z3 import *
import util

a, b, c, d, e, f = Bools('a b c d e f')
s = Solver()
s.add(util.count_eq([a, b, c, d, e, f], 3))
s.add(a == Not(b))
s.add(b == Not(Or(a, c)))
s.add(c == Not(Or(d, e)))
s.add(d == Not(Or(c, f)))
s.add(e == Not(Or(d, f)))
s.add(f == Not(e))
s.add(a == Not(d))
s.add(b == Not(f))

assert util.solve_all(s, {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f})
