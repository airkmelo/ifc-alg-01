#fragefunf_05

print("Quantos vasilhames de até 1 litro voce quer reciclar?")
igual1l = int(input())

print("E quantos vasilhames com mais de 1 litro queres recilar?")

more1l = int(input())

y = igual1l * 0.10
c = more1l * 0.25

tot = y + c

print(" Seus créditos são de R$", round(tot,2), "reais")