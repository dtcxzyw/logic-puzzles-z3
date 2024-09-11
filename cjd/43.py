# https://mp.weixin.qq.com/s/NqJhjaWiG0gi4ALJUrH-1Q
from z3 import *
import util

color, (red, pink, white, black, purple) = EnumSort('color', ['red', 'pink', 'white', 'black', 'purple'])
a = Const('a', color)
b = Const('b', color)
c = Const('c', color)
d = Const('d', color)
e = Const('e', color)

is_true = {a: False, b: False, c: True, d: True, e: True}

s = Solver()
s.add(Distinct(a, b, c, d, e))

def query(color, expr):
    res = False
    for i in [a, b, c, d, e]:
        ans = expr
        if not is_true[i]:
            ans = Not(ans)
        res = If(color == i, ans, res)
    return res

s.add(query(red, query(pink, e == white)))
s.add(Not(query(pink, query(white, b == black))))
s.add(Not(query(white, query(black, d == red))))
s.add(query(black, query(red, And(a != pink, b != pink))))

assert util.solve_all(s, {'a': a, 'b': b, 'c': c, 'd': d, 'e': e})
