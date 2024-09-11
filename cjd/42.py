# https://mp.weixin.qq.com/s/d_GBZLzXfuLA9KxQ14LGaw
from z3 import *
import util

a1, a2, a3, a4 = Ints('a1 a2 a3 a4')
b1, b2, b3, b4 = Ints('b1 b2 b3 b4')

s = Solver()
s.add(Distinct(a1, a2, a3, a4))
s.add(Distinct(b1, b2, b3, b4))
for i in [a1, a2, a3, a4]:
    s.add(And(i >= 1, i <= 4))
for i in [b1, b2, b3, b4]:
    s.add(And(i >= 1, i <= 5))

sum1 = a1 + b1
sum2 = a2 + b2
sum3 = a3 + b3
sum4 = a4 + b4

s.add(sum2 == sum1 + 1)
s.add(sum3 == sum2 + 1)
s.add(sum4 == sum3 + 1)
s.add(b2 >= 2)

assert util.solve_unique(s, {'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4, 'b1': b1, 'b2': b2, 'b3': b3, 'b4': b4})
