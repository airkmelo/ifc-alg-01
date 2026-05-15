#vraagzes_06

suq = 2.98

prat = 15.98

sobr = 5.99


print("Valor das opções:")
print(f"Suco: R$ {suq:.2f}")
print(f"Prato principal: R$ {prat:.2f}")
print(f"Sobremesa: R$ {sobr:.2f}")


print("Voce vai querer suco?(1 para Sim ou 0 para Nao)")
s1 = int(input())

print("Voce vai querer prato principal?(1 para Sim ou 0 para Nao)")
s2 = int(input())

print("Voce vai querer sobremesa?(1 para Sim ou 0 para Nao)")
s3 = int(input())


tot = (suq*s1 + prat*s2 + sobr*s3) * 1.1

print(f"Sua conta do almoço deu R$ {tot:.2f}")