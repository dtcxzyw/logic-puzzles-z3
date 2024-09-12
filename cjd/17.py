# https://mp.weixin.qq.com/s/stkyCFZV9vQsq_DpotrLZQ
from z3 import *
import util

job, (designer, mystery, writer, dancer) = EnumSort('job', ['designer', 'mystery', 'writer', 'dancer'])
m, r, t, u = Consts('m r t u', job)

s = Solver()
s.add(Distinct(m, r, t, u))
s.add(Implies(m == designer, r == mystery))
s.add(Implies(t == writer, r == dancer))
s.add(Implies(u == dancer, m == designer))
s.add(Implies(r != mystery, m != dancer))
s.add(Implies(u != mystery, r == writer))
s.add(m != writer)

assert util.solve_all(s, {'m': m, 'r': r, 't': t, 'u': u})
