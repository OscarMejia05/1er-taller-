#6.	Desarrollar un algoritmo de “Adivina un Número”, con las siguientes características: a) El número debe estar en el rango de 1 a 200. b) Debe tener dos niveles nivel básico y nivel experto, el nivel básico no tendrá restricciones en número de oportunidades. El Nivel experto solo tendrá 5 oportunidades. Al finalizar debe informar el número de intentos realizados antes de encontrar la respuesta correcta

import random 
def adivina_un_numero(nivel):
    
    numero_aleatorio = random.randint(1, 200)
    intentos = 0
    
    if nivel == "basico":
        print("juegas en nivel basico")
        while True:
            intento = int(input("Adivina el numero: "))
            intentos += 1
            
            if intento == numero_aleatorio:
                print("Adivinaste el numero en", intentos, "intentos:")
                break
            if intento < numero_aleatorio:
                print("el numero es mayor: ")
            else:
                print("el numero es menor: ")
    
    elif nivel == "nivel esperto":
        print("juegas en nivel experto")
        for _ in range(5):
            intento = int(input("Adivina el numero en cinco intentos: "))
            intentos += 1
            
            if intento == numero_aleatorio:
                print("Adivinaste el numero en", intentos, "intentos:")
                break
            if intento < numero_aleatorio:
                print("el numero es mayor: ")
            else:
                print("el numero es menor: ")
                
        print("perdiste en las cinco oportunidades, el numero aleatorio era: ", numero_aleatorio)
    
    else:
        print("Error, por favor elige entre basico  experto: ")
        
nivel_juego = input("Elige un nivel (basico o experto): ")
adivina_un_numero(nivel_juego)