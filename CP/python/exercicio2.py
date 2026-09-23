import os
os.system("cls")

valor = float(input("digite o valor da compra: "))
if valor < 100:
    desconto = valor * 0
    print(f"o valor da compra é: {valor}")
    print(f"desconto: {desconto}")
    print(f"valor final: R${valor - desconto}")
else:
    if valor >= 100 and valor < 500:
        desconto = valor * 0.05
        print(f"o valor da compra: {valor}")
        print(f"desconto: {desconto}")
        print(f"valor final: R${valor - desconto}")
    else:
        if valor >= 500:
            desconto = valor * 0.1
            print(f"o valor da compra: {valor}")
            print(f"desconto: {desconto}")
            print(f"valor final: R${valor - desconto}")