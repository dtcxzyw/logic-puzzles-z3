# https://mp.weixin.qq.com/s/8IeHImuQpZBZpzxyC7vSqg
from z3 import *
import util

end = 50
a, b, c, d, e = Ints('a b c d e')
s = Solver()
for i in [a, b, c, d, e]:
    s.add(i >= 0, i < end)
s.add(Distinct(a, b, c, d, e))
s.add(b < d)

def meet(i, j):
    return 2 * end - i - j

def meet_k(i, j):
    mij = meet(i, j)
    cnt = 0
    for k in [a, b, c, d, e]:
        if not eq(k, i):
            cnt += If(meet(i, k) <= mij, 1, 0)
    return cnt

s.add(meet_k(a, c) == 3)
s.add(meet_k(c, d) == 2)

def order(i):
    res = 0
    for j in [a, b, c, d, e]:
        res += If(j >= i, 1, 0)
    return res

assert util.solve_all(s, {'a': order(a), 'b': order(b), 'c': order(c), 'd': order(d), 'e': order(e)})
