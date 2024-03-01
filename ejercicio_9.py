#9.	La pizzería Pequeña Italia ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación. Ingredientes vegetarianos: Pimiento y tofu. Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


bienvenido = input("elija pizza vegentariana o no vegentariana:")

if bienvenido == "pizza vegetariana": 
    print("Ingredientes vegetarianos: Pimiento, tofu mas mozzarella y tomate")
    while True:
        ingredientes = input("elige entre tofu o pimiento: ")
        
        if ingredientes == "tofu":
            print("Tu pizza es de tofu con tomate y mozzarella")
        
        else:
            print("tu pizza es de pimiento con tomate y mozzarella")
        
else:
    print("Ingredientes no vegetarianos: Peperoni, jamon o salmon mas mozzarella y tomate")
    
ingredientes1 = input("elige entre peperoni, jamon o salmon: ")
        
if ingredientes1 == "peperoni":
            print("Tu pizza es de peperoni con tomate y mozzarella")
        
if ingredientes1 == "jamon":
            print("Tu pizza es de jamon con tomate y mozzarella")
            
if ingredientes1 == "salmon":
            print("Tu pizza es de salmon con tomate y mozzarella")
            
    