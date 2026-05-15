#questaootto_11

import math as v

x1 = float(input("qual seu ponto t1:"))

x2 = float(input("Qual seu ponto g1"))

x3 = float(input("Qual seu ponto t2:"))
x4 = float(input("Qual seu ponto g2:"))

r1 = v.radians(x1)
r2 = v.radians(x2)

t1 = v.radians(x3)
t2 = v.radians(x4)

d = 6371.01 * v.acos(v.sin(r1) * v.sin(t1) + v.cos(r1)*v.cos(t1)*v.cos(r2 - t2))


print(d)