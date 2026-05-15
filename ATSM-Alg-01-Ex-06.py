#vraagzes_06

suquinho = 2.98

pratao = 15.98

sobramesa = 5.99

tot = 0


print("Valor das opções:")
print(f"Suco: R$ {suquinho:.2f}")
print(f"Prato principal: R$ {pratao:.2f}")
print(f"Sobremesa: R$ {sobramesa:.2f}")


print("Voce vai querer suco?(S/N)")
s1 = input()

print("Voce vai querer prato principal?(S/N)")
s2 = input()

print("Voce vai querer sobremesa?(S/N)")
s3 = input()


if s1 == "S":
    tot = tot + suquinho 
else :
    tot =+ 0

if s2 == "S" : 
    tot = tot + pratao
else : 
    tot =+ 0

if s3 == "S" :
    tot = tot + sobramesa
else :
    tot =+ 0

tot = tot + tot*0.1

print(f"Sua conta do almoço deu R$ {tot:.2f}")
