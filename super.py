import random


def compra_random(productos, precios, stock_supermercado):

    # Número de productos distintos que comprará el cliente
    cantidad_productos = random.randint(1, 5)

    coste_total = 0

    print("\nNUEVO CLIENTE")
    print("----------------------------")

    for i in range(cantidad_productos):

        # Elegimos un producto aleatoriamente
        posicion = random.randint(0, len(productos) - 1)

        # Cantidad que quiere comprar el cliente
        cantidad = random.randint(1, 3)

        # Comprobamos que haya suficiente stock
        if stock_supermercado[posicion] >= cantidad:

            stock_supermercado[posicion] = (
                stock_supermercado[posicion] - cantidad
            )

            coste = precios[posicion] * cantidad
            coste_total = coste_total + coste

            print(
                productos[posicion],
                "-",
                cantidad,
                "unidades -",
                round(coste, 2),
                "€"
            )

    print("----------------------------")
    print("Total:", round(coste_total, 2), "€")

    return coste_total