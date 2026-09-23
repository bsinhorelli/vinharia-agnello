import os
os.system("cls")

nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média das notas é: {media}")

if media >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")