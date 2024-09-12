# https://mp.weixin.qq.com/s/8zRm9XYpCmuiYo7MIIeojQ
from z3 import *
import util

a1, b1, c1, d1, e1 = Ints('a1 b1 c1 d1 e1')
a2, b2, c2, d2, e2 = Bools('a2 b2 c2 d2 e2')
s = Solver()
for k, v in zip([a1, b1, c1, d1, e1], [a2, b2, c2, d2, e2]):
    s.add(k >= 0)
    #s.add(Implies(v, k == 7))
    s.add(Implies(v, (k % 2) == 1))

s.add(c1 - e1 == 2)
# s.add(a1 + d1 == 24)
s.add((a1 + d1) % 2 == 0)
s.add(b1 * 2 == d1)
s.add(a1 + c1 == e1 * 2)
s.add(Or(a2, b2, c2, d2, e2))

assert util.solve_all(s, {'a2': a2, 'b2': b2, 'c2': c2, 'd2': d2, 'e2': e2})
