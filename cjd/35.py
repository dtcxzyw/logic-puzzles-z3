# https://mp.weixin.qq.com/s/E3rppRc8XpaOuGFIMHtuIA
from z3 import *
import util

a, b, c, d, e = Bools('a b c d e')
s = Solver()
s.add(Implies(a, Not(b)))
s.add(Implies(Or(a, c), e))
s.add(Implies(b, Xor(d, e)))
s.add(util.count_eq([a, b, c, d, e], 3))

for i in [a, b, c, d, e]:
    s.push()
    s.add(Not(i))
    if s.check() == unsat:
        print(i)
    s.pop()
