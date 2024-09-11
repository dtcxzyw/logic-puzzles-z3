# https://mp.weixin.qq.com/s/3yFu_1cuKiJWi8qq7CS9NA
from z3 import *
import util

a = Int('a')
b = Int('b')
c = Int('c')
d = Int('d')

s = Solver()
for i in [a, b, c, d]:
    s.add(i >= 5, i <= 8)
s.add(Distinct(a, b, c, d))

s.add(a == 7)
final = {'a' : a, 'b' : b, 'c' : c, 'd' : d}
given = {'a' : False, 'b' : False, 'c' : False, 'd' : False}
num = {1: False, 2: False, 3: False, 4: False}

for i in [a, b, c, d]:
    giveCount = 0
    for j in [a, b, c, d]:
        if id(i) != id(j):
            give = Int(f'give{i}2{j}')
            s.add(give >= 0, give <= i)
            for n in num:
                num[n] = Or(num[n], give == n)
            
            final[str(i)] -= give
            final[str(j)] += give
            given[str(j)] = Or(given[str(j)], give > 0)
            giveCount = giveCount + If(give > 0, 1, 0)
            if str(i) == 'a' and str(j) == 'b':
                s.add(give > 0)
            if str(i) == 'b':
                s.add(Implies(give > 0, give == 3))
            if str(j) == 'c':
                s.add(Implies(give > 0, give == 1))
    s.add(giveCount == 1)

s.add(Distinct(final['a'], final['b'], final['c'], final['d']))
for key in final:
    s.add(final[key] >= 5, final[key] <= 8)
s.add(given['a'], given['b'], given['c'], given['d'])
s.add(num[1], num[2], num[3], num[4])

assert util.solve_unique(s, {'a': a, 'b': b, 'c': c, 'd': d, 'fa': final['a'], 'fb': final['b'], 'fc': final['c'], 'fd': final['d']})
