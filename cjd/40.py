# https://mp.weixin.qq.com/s/nBjVpryPM6uvO5NqDV06qg
from z3 import *
import util

color, (white, black, blue) = EnumSort('color', ['white', 'black', 'blue'])

a = Const('a', color) # angel
b = Const('b', color) # commoner
c = Const('c', color) # evil

def query(color, notx):
    res = False
    for i in [a, b, c]:
        if id(i) == id(notx):
            ans = False
        else:
            ans = True
        if id(i) == id(b):
            ans = True
        elif id(i) == id(c):
            ans = not ans
        res = If(i == color, ans, res)
    return res

s = Solver()
s.add(Distinct(a, b, c))
s.add(query(white, a))
s.add(query(blue, b))
s.add(query(black, c))

assert util.solve_unique(s, {'a': a, 'b': b, 'c': c})
