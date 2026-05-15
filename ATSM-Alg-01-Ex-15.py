#Fragefünfzehn_15

import math as m

oc = float(input("Insira o comprimento de um lado do seu polígono: "))

al = float(input("Insira a quantidade de lados do seu polígonos: "))

area = al *  oc**2 / (4 * m.tan(m.pi/al))

print(f"A area do poligono é: {area:.2f}")

