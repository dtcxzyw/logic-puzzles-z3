# https://mp.weixin.qq.com/s/dzu_RCj7zscT5gcnr0WDtQ
from z3 import *

sort = DeclareSort('sort')
p = Function('p', sort, BoolSort())
q = Function('q', sort, BoolSort())
r = Function('r', sort, BoolSort())
t = Function('t', sort, BoolSort())
s = Function('s', sort, BoolSort())

solver = Solver()
c = Const('c', sort)
solver.add(ForAll([c], Implies(p(c), And(q(c), r(c)))))
solver.add(Exists([c], And(s(c), Not(q(c)))))
solver.add(ForAll([c], Implies(t(c), Not(r(c)))))
solver.add(Exists([c], And(t(c), q(c))))

exprs = [
    Exists([c], And(s(c), t(c))),
    ForAll([c], Implies(s(c), Not(r(c)))),
    Exists([c], And(q(c), s(c))),
    ForAll([c], Implies(p(c), Not(t(c)))),
]

for expr in exprs:
    solver.push()
    solver.add(Not(expr))
    if solver.check() == unsat:
        print(expr)
    solver.pop()
