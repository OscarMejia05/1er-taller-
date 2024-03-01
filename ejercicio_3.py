#3.	Desarrollar un algoritmo para leer la temperatura en grados centígrados y muestre su resultado en Fahrenheit y kelvin

centigrados = float(input("digite temperatura en grados centigrados:"))

fahrenheit = (centigrados * 9/5) + 32
kelvin = centigrados + 273.15 

print("la temperatura en fahrenheit es:", fahrenheit)
print("la temperatura en kelvin es:", kelvin)