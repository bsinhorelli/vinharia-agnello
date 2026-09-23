import os
os.system("cls")

idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
if idade >= 12:
    if altura >= 1.40:
        print("entrada permitida")
    else:
        print("entrada não permitida")
else:
    print("entrada não permitida")