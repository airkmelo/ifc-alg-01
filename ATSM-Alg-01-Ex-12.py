#Fragezwölf_12

import math as math

print("Qual o seu valor de raio?")

ro = float(input())


circ = math.pi * ro**2

esf = math.pi * 4/3 * ro**3

print(f"Área do círculo é {circ:.2f} ")

print("Volume da esfera é", round(esf, 2))