# https://mp.weixin.qq.com/s/hcZ7NSWvd3AqiBMx0TtJPw
from z3 import *

a, b, c = Bools('a b c')
s = Solver()
s.add(a == Not(And(a, b, c)))

print(s.check())
