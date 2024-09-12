# https://mp.weixin.qq.com/s/PCBv6AI-kcPW8XPDxyqHRQ
from z3 import *
import util

a, b, c, d = Ints('a b c d')
s = Solver()
for i in [a, b, c, d]:
    s.add(And(1 <= i, i <= 4))
s.add(Distinct(a, b, c, d))
def query(n, x, y, z, w):
    xv, yv, zv, wv = Bools(f'xv{n} yv{n} zv{n} wv{n}')
    return And(xv == x, yv == y, zv == z, wv == w, util.count_eq([xv, yv, zv, wv], 2))
s.add(query(1, a == 1, b == 3, c == 2, d != 2))
s.add(query(2, a == 3, b != 3, c != 2, d == 2))
s.add(query(3, a == 4, b != 3, c == 2, d == 1))

assert util.solve_all(s, {'a': a, 'b': b, 'c': c, 'd': d})
