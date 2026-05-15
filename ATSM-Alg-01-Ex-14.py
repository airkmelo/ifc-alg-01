#Fragevierzehn14

import math as m

l0 = float(input("O valor do primeiro lado do seu triangulo: "))

l1 = float(input("o valor do segundo lado do seu triangulo: "))


l2 = float(input("O valor do terceiro lado do seu triangulo: "))


l = (l0 + l1 + l2)/2

ara = (l * (l - l0) * (l - l1) * (l - l2))**(1/2)

print(f"A area dp triangulo é {ara:.2f}")


#a² = b² + c²
#a2 = 9/3 + 16/4
