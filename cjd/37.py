# https://mp.weixin.qq.com/s/v9qW8S3HWFyR1dqCUmVGtw
from z3 import *
import util

a1, b1, c1, d1, e1, f1, g1, h1, i1 = Bools('a1 b1 c1 d1 e1 f1 g1 h1 i1')
a2, b2, c2, d2, e2, f2, g2, h2, i2 = Bools('a2 b2 c2 d2 e2 f2 g2 h2 i2')

s = Solver()
s.add(util.count_eq([a1, b1, c1, d1, e1, f1, g1, h1, i1], 1))
s.add(util.count_eq([a2, b2, c2, d2, e2, f2, g2, h2, i2], 3))

s.add(a2 == And(Not(a1), Not(e1)))
s.add(b2 == Not(a2))
s.add(c2 == b1)
s.add(d2 == c2)
s.add(e2 == Or(e1, a1))
s.add(f2 == Not(b1))
s.add(g2 == Or(b1, h1))
s.add(h2 == And(Not(h1), Not(b1)))
s.add(i2 == h2)

assert util.solve_all(s, {'a1': a1, 'b1': b1, 'c1': c1, 'd1': d1, 'e1': e1, 'f1': f1, 'g1': g1, 'h1': h1, 'i1': i1,
                          'a2': a2, 'b2': b2, 'c2': c2, 'd2': d2, 'e2': e2, 'f2': f2, 'g2': g2, 'h2': h2, 'i2': i2})
