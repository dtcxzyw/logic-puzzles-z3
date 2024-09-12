# https://mp.weixin.qq.com/s/VKfl3joAOG_un9Wu2yD3Ow
from z3 import *
import util

a1, b1, c1 = Bools('a1 b1 c1')
a2, b2, c2 = Bools('a2 b2 c2')
s = Solver()
s.add(util.count_eq([a1, b1, c1], 1))
s.add(a2 == Not(b1))
s.add(b2 == a2)
s.add(c2 == And(Not(a1), Not(c1)))
s.add(Not(And(a2, b2, c2)))
s.add(Implies(a1, a2), Implies(b1, b2), Implies(c1, c2))

assert util.solve_all(s, {'a1': a1, 'b1': b1, 'c1': c1})
