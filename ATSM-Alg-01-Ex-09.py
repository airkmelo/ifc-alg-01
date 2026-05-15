#kysymys_yhdeksän_09

x = 1

print("Qual o valor inicial na sua conta de investimento?")
m=float(input())

while x<=3:

    jc = m*(1+0.12)**x

    print("O valor no ano", x, "é:", round(jc,2))

    x= x+1
