import os
os.system("cls")

temperatura = float(input("temperatura: "))
#and é para veficar as duas condições, dá pra fazer sem ele porem o codigo fica maior
if temperatura < 10:
    print("classificação: FRIO")
elif temperatura >= 10 and temperatura <= 24:
    print("classificação: AMENO")
elif temperatura >= 25 and temperatura <= 34:
    print("classificação: QUENTE")
else:
    print("classificação: MUITO QUENTE")