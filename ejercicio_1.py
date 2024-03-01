#1.	Elaborar un programa que pida un número y si es par lo eleve al cubo, y si impar lo eleve al cuadrado.

numero = int(input("digite un numero:"))
if numero % 2 == 0:
    conclusion = numero ** 3
else:
    conclusion = numero ** 2
print("es: ", conclusion)