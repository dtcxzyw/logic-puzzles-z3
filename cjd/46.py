# https://mp.weixin.qq.com/s/bALOToRTnUadGlfI5T7pPQ
from z3 import *
import util

a, b, c = Bools('a b c')
s = Solver()
s.add(util.count_eq([a, b, c], 1))
s.add(a == Not(b))
s.add(b == Not(c))
s.add(c == c)
util.solve_all(s, {"a": a, "b": b, "c": c})
