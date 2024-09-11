# https://mp.weixin.qq.com/s/rbuAcFiwI4MtrFFhLCVZww
from z3 import *
import util

a, b, c = Ints('a b c')
s = Solver()
for i in [a, b, c]:
    s.add(i >= 1, i <= 5)
s.add(Distinct(a, b, c))

def win(i):
    val = []
    for j in [a, b, c]:
        if eq(i, j):
            continue
        val.append(j)
    return And(val[0] <= 2, val[1] <= 2)

def lose(i):
    val = []
    for j in [a, b, c]:
        if eq(i, j):
            continue
        val.append(j)
    return Or(val[0] == 5, val[1] == 5)

s.add(Not(win(a)), Not(lose(a)))
s.add(Not(win(b)), Not(lose(b)))
s.add(lose(c))

assert s.check() == unsat
