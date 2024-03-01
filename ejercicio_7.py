#Realizar un programa que le presente un menú al usuario con las siguientes opciones:1.Leer dos números enteros positivos únicamente 2.Sumar los dos números leídos 3.Restarle al primer número el segundo (siempre y cuando el primero sea mayor que él segundo, en caso contrario indicar con un mensaje que la operación no es posible realizarla y volver al menú principal, 4.Multiplicar los dos números (siempre y cuando ninguno de los números sea igual a cero, en caso contrario indicar con un mensaje que la operación no es posible realizarla y volver al menú principal 5.Dividir el primer número dado por el segundo

def leer_dos_numeros():
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    return num1, num2

def sumar_numeros():
    num1, num2 = leer_dos_numeros()
    suma = num1 + num2
    print("La suma es:", suma)

def restar_numeros():
    num1, num2 = leer_dos_numeros()
    if num1 >= num2:
        resta = num1 - num2
        print("La resta es:", resta)
    else:
        print("No es posible realizar la opercación.")

def multiplicar_numeros():
    num1, num2 = leer_dos_numeros()
    if num1 != 0 and num2 != 0:
        multiplicacion = num1 * num2
        print("La multiplicación es:", multiplicacion)
    else:
        print("No es posible realizar la operación.")

def dividir_numeros():
    num1, num2 = leer_dos_numeros()
    if num2 != 0:
        division = num1 / num2
        print("La división es:", division)
    else:
        print("No es posible realizar la operación.")

def mostrar_menu():
    print("Menú:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

mostrar_menu()
opcion = int(input("Seleccione: "))

while opcion != 5:
    if opcion == 1:
        sumar_numeros()
    elif opcion == 2:
        restar_numeros()
    elif opcion == 3:
        multiplicar_numeros()
    elif opcion == 4:
        dividir_numeros()
    else:
        print("Intenta de nuevo")

    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

print("Fin.")