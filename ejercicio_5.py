#5.	Diseñar un algoritmo que permita emitir la factura correspondiente a una compra de un artículo del cual se adquiere una o varias unidades y se conoce su precio antes de IVA (iva igual al 16%), y si el precio bruto (precio de venta más IVA) es mayor de $500.000.oo se debe realizar un descuento del 15%

def emitir_factura(valor_articulo, cantidad):
    iva = 0.16
    precio_bruto = valor_articulo * cantidad * (1+iva)
    if precio_bruto > 500000:
        descuento = 0.15
        precio_bruto -= precio_bruto * descuento 
    return precio_bruto

valor_articulo = float(input("Ingrese el precio del articulo:"))
cantidad = int(input("ingrese la cantidad:"))
total = emitir_factura(valor_articulo, cantidad)

print("el total es:", total)