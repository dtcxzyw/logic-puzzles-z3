# https://mp.weixin.qq.com/s/YMhd09dTnNShg1G_8wSVMg
from z3 import *
import util

w1 = Int('w1')
w2 = Int('w2')
a, b, c, d, e, f, g, h = Bools('a b c d e f g h')

def query(s):
    sum = 0
    for i in s:
        sum = sum + If(i, w1, w2)
    return sum

s = Solver()
s.add(w1 >= 1, w1 <= 2)
s.add(w2 >= 1, w2 <= 2)
s.add(w1 != w2)
s.add(query([a,b,c]) == query([d,e,f]))
s.add(query([a,b,g]) > query([c,d,e]))
s.add(query([a,h]) == query([d,f]))
s.add(query([a,b,c,d,e,f,g,h]) == 6 * w1 + 2 * w2)

for cond in [w1 < w2, w1 > w2]:
    s.push()
    print("When",cond)
    s.add(cond)
    assert util.solve_all(s, {'w1': w1, 'w2': w2, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h})
    s.pop()
