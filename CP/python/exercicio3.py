import os
os.system("cls")

numeroX = int(input("DIgite um numero: "))
numeroY = int(input("digite um numero: "))
numeroZ = int(input("digite um numero: "))

if numeroX >= numeroY and numeroX >= numeroZ:
    print(f"o maior numero é {numeroX}")
elif numeroY >= numeroX and numeroY >= numeroZ:
    print(f"o maior numero é {numeroY}")
else:
    print(f"o maior numero é {numeroZ}")