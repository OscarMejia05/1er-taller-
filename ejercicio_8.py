#8.	Un almacén de la ciudad tiene un plan de tarifas y descuentos sobre el valor del envío de mercancía a sus clientes: Descuentos: - Si el valor de la mercancía es >= a 300.000 y <= a 600.000 se hace un descuento del 20% sobre el valor del envío - Si el valor de la mercancía es > a 600.000 y <= a 1.000.000 se hace un descuento del 35% sobre el valor del envío - Si el valor de la mercancía es > a 1.000.000 se hace un descuento del 50% sobre el valor del envío. Promociones: - Si el pago se hace con tarjeta propia del almacén, no se cobra la tarifa de envío - Si paga en efectivo y el valor de la mercancía es superior a 500.000 no se cobra el envío. - Si paga en efectivo y el valor de la mercancía está entre 300.000 y 500.000 se hace un 50% de descuento sobre la tarifa de envío. Desarrolle un programa que calcule e imprima el valor total del envío.

def descuentos_de_un_almacen():
    peso = float(input("Ingrese el peso de la mercancia: "))
    valor = float(input("Ingrese el valor de la mercancia: "))
    pago = input("Ingrese la forma de pago: ")

    if peso <= 500:
        tarifa = 40000
    elif 500 < peso <= 750:
        tarifa = 80000
    elif 750 < peso <= 1000:
        tarifa = 100000
    elif peso > 1000:
        tarifa = 500 * (peso // 10)

    if 300000 <= valor <= 600000:
        descuento = tarifa * 0.20
    elif 600000 < valor <= 1000000:
        descuento = tarifa * 0.35
    elif valor > 1000000:
        descuento = tarifa * 0.50

    if pago == "tarjeta":
        tarifa = 0
    elif pago == "efectivo" and valor > 500000:
        tarifa = 0
    elif 300000 < valor < 500000:
        descuento = tarifa * 0.50

    print("El valor es: ", tarifa - descuento)
descuentos_de_un_almacen()