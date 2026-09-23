import os
os.system("cls")

salario = float(input("digite seu salario: "))
anos = int(input("quantos anos de empresa: "))
#and é no mesmo sentido que no exercicio 5 porem aqui ficaria maior ainda
if salario <= 3000 and anos > 5:
    bonus = salario * 0.1
elif salario > 3000 and anos > 5:
    bonus = salario * 0.07
elif salario <= 3000 and anos <= 5:
    bonus = salario * 0.03

else:
    bonus = 0

print(f"bonus: {bonus:.2f}")
print(f"novo salario: {salario + bonus:.2f}")