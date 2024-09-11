# https://mp.weixin.qq.com/s/Y2FGPXzQyP1Df4R0XnR7VA
from z3 import *
import util

color1, (grey, green, blue, red) = EnumSort('color1', ['grey', 'green', 'blue', 'red'])
color2, (black, white, purple, tea) = EnumSort('color2', ['black', 'white', 'purple', 'tea'])

a1 = Const('a1', color1)
a2 = Const('a2', color2)
a3 = Int('a3')
b1 = Const('b1', color1)
b2 = Const('b2', color2)
b3 = Int('b3')
c1 = Const('c1', color1)
c2 = Const('c2', color2)
c3 = Int('c3')
d1 = Const('d1', color1)
d2 = Const('d2', color2)
d3 = Int('d3')

s = Solver()
for n in [a3, b3, c3, d3]:
    s.add(n >= 1, n <= 4)
s.add(Distinct(a1, b1, c1, d1))
s.add(Distinct(a2, b2, c2, d2))
s.add(Distinct(a3, b3, c3, d3))

def query1(color1):
    return If(a1 == color1, a3,
            If(b1 == color1, b3,
            If(c1 == color1, c3,
            d3)))

def query2(color2):
    return If(a2 == color2, a3,
            If(b2 == color2, b3,
            If(c2 == color2, c3,
            d3)))

def add(a, b, c, d):
    s.add(Distinct(a, b, c))
    s.add(a + b + c == d)

add(query1(grey), query2(black), b3, 8)
add(query1(green), query2(white), c3, 9)
add(query1(red), query2(tea), d3, 7)

for v1, v2 in [(a1, a2), (b1, b2), (c1, c2), (d1, d2)]:
    s.add(Implies(v2 == purple, v1 != grey))

s.add(c1 != blue)
s.add(b1 == red)

assert util.solve_unique(s, {'a1': a1, 'a2': a2, 'a3': a3, 'b1': b1, 'b2': b2, 'b3': b3, 'c1': c1, 'c2': c2, 'c3': c3, 'd1': d1, 'd2': d2, 'd3': d3})
