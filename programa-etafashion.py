

import time

precioCompra = float(input("Ingrese el precio final de la compra: "))
cantidad = int(input("Ingrese la cantidad de prendas adquiridas: "))


print("Procesando los datos")
print("Por favor espere....")
time.sleep(3)

if cantidad > 21:
    descuento = 0.5 * precioCompra
    precioFinal = precioCompra - descuento
    print(f"La cantidad de prendas fueron: {cantidad}")
    print(f"El precio final a pagar es: {precioFinal}")
elif cantidad >= 10 and cantidad <= 20:
    descuento = 0.5 * precioCompra
    precioFinal = precioCompra - descuento
    print(f"La cantidad de prendas fueron: {cantidad}")
    print(f"El precio final a pagar es: {precioFinal}")
else:
    print(f"La cantidad de prendas fueron: {cantidad}")
    print(f"El precio final a pagar es: {precioCompra}")

