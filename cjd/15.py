# https://mp.weixin.qq.com/s/5BBFR_jaAG0na6RzmY69CA
from z3 import *

sort = DeclareSort('sort')
f1 = Function('f1', sort, BoolSort())
f2 = Function('f2', sort, BoolSort())
f3 = Function('f3', sort, BoolSort())
f4 = Function('f4', sort, BoolSort())
f5 = Function('f5', sort, BoolSort())

s = Solver()
x = Const('x', sort)
s.add(ForAll([x], Implies(f1(x), Not(f2(x)))))
s.add(ForAll([x], Implies(f3(x), f4(x))))
s.add(ForAll([x], Implies(f2(x), f5(x))))
s.add(ForAll([x], Implies(f4(x), Not(f5(x)))))

exprs = [
    Implies(Not(f4(x)), f2(x)),
    Implies(f3(x), Not(f2(x))),
    Implies(f4(x), f3(x)),
    Implies(f1(x), f5(x)),
]

for expr in exprs:
    s.push()
    s.add(Not(ForAll([x], expr)))
    if s.check() == unsat:
        print(expr)
    s.pop()
