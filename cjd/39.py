# https://mp.weixin.qq.com/s/j2l9xVvYWjSIJryB-rG_pw
from z3 import *
import util

color1, (A1, B1, C1, D1) = EnumSort("color1", ["A", "B", "C", "D"])
color2, (A2, B2, C2, D2) = EnumSort("color2", ["A", "B", "C", "D"])

a1 = Const("a1", color1)
a2 = Const("a2", color2)
b1 = Const("b1", color1)
b2 = Const("b2", color2)
c1 = Const("c1", color1)
c2 = Const("c2", color2)
d1 = Const("d1", color1)
d2 = Const("d2", color2)

def query1(color):
    res = A2
    for i, j in [(a1, A2), (b1, B2), (c1, C2), (d1, D2)]:
        res = If(i == color, j, res)
    return res

def query2(color):
    res = A2
    for i, j in [(a2, A2), (b2, B2), (c2, C2), (d2, D2)]:
        res = If(i == color, j, res)
    return res

s = Solver()
s.add(Distinct(a1, b1, c1, d1))
s.add(Distinct(a2, b2, c2, d2))
s.add(Or(a1 == A1, b1 == B1, c1 == C1, d1 == D1))
s.add(Or(a2 == A2, b2 == B2, c2 == C2, d2 == D2))
s.add(c2 == query1(A1))
s.add(a2 == query1(B1))
s.add(b2 == query2(D2))

assert util.solve_all(s, {"a1": a1, "b1": b1, "c1": c1, "d1": d1, "a2": a2, "b2": b2, "c2": c2, "d2": d2})
