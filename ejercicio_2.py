#2.	Elaborar un programa que pida a dos usuarios el nombre y la edad e imprima el nombre del menor

nombre_1 = input("digite nombre:")
edad_1 = int(input("digite edad:"))

nombre_2 = input("digite nombre:")
edad_2 = int(input("digite edad:"))

if edad_1 > edad_2:
   menor = nombre_2
else:
   menor = nombre_1 

print("el nombre del menor es:", menor)  
