# https://mp.weixin.qq.com/s/Nb4OSS8wmMXl0cAMBd_lWg
from z3 import *
import util

a1, b1, c1, d1, e1 = Bools('a1 b1 c1 d1 e1') # white: T, black: F
a2, b2, c2, d2, e2 = Bools('a2 b2 c2 d2 e2')
m = Bool('m')

s = Solver()
for k, v in zip([a1, b1, c1, d1, e1], [a2, b2, c2, d2, e2]):
    s.add(Xor(k, v) == m)

s.add(a2 == util.count_eq([b1, c1, d1, e1], 3))
s.add(b2 == util.count_eq([a1, c1, d1, e1], 1))
s.add(c2 == util.count_eq([a1, b1, d1, e1], 4))
s.add(d2 == util.count_eq([a1, b1, c1, e1], 0))
s.add(e2 == Not(m))

# s.add(Not(util.count_le([a2, b2, c2, d2, e2], 2)))
# assert s.check() == unsat
assert util.solve_all(s, {'a2': a2, 'b2': b2, 'c2': c2, 'd2': d2, 'e2': e2})
