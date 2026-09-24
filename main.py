import productos
import super
from productos import stock_minimo_almacen

# Numero de clientes que entraran al supermercado
numero_clientes = 100

# Dinero total generado durante la simulacion
ingresos_totales = 0

# Contadores para ver cuantas reposiciones se realizan
reposiciones_supermercado = 0
pedidos_fabrica = 0


# Guardamos el stock inicial para saber hasta cuanto hay que reponer
stock_objetivo_supermercado = productos.stock_supermercado.copy()
stock_objetivo_almacen = productos.stock_almacen.copy()


print("========================================")
print("        SIMULACION SUPERMERCADO")
print("========================================")


# SIMULACION DE CLIENTES
for cliente in range(numero_clientes):

    print("\n========================================")
    print("CLIENTE", cliente + 1)
    print("========================================")

    # El cliente realiza una compra aleatoria
    coste_compra = super.compra_random(
        productos.productos,
        productos.precios,
        productos.stock_supermercado
    )

    ingresos_totales = ingresos_totales + coste_compra


    # COMPROBAR STOCK DEL SUPERMERCADO
    for i in range(len(productos.productos)):

        if productos.stock_supermercado[i] <= productos.stock_minimo_supermercado[i]:

            print(
                "\nSTOCK BAJO EN SUPERMERCADO:",
                productos.productos[i]
            )

            # Calculamos cuantas unidades hacen falta para
            # volver al stock inicial
            cantidad_necesaria = (
                stock_objetivo_supermercado[i]
                - productos.stock_supermercado[i]
            )


            # COMPROBAR SI EL ALMACEN TIENE SUFICIENTE STOCK
            if productos.stock_almacen[i] < cantidad_necesaria:

                print(
                    "El almacen no tiene suficiente stock de",
                    productos.productos[i]
                )

                print("Solicitando productos a la fabrica...")


                # La fabrica tiene stock infinito
                cantidad_fabrica = (
                    stock_objetivo_almacen[i]
                    - productos.stock_almacen[i]
                )

                productos.stock_almacen[i] = (
                    productos.stock_almacen[i]
                    + cantidad_fabrica
                )

                pedidos_fabrica = pedidos_fabrica + 1


                print(
                    "FABRICA -> ALMACEN:",
                    cantidad_fabrica,
                    "unidades de",
                    productos.productos[i]
                )


            # REPONER EL SUPERMERCADO DESDE EL ALMACEN

            productos.stock_almacen[i] = (
                productos.stock_almacen[i]
                - cantidad_necesaria
            )

            productos.stock_supermercado[i] = (
                productos.stock_supermercado[i]
                + cantidad_necesaria
            )

            reposiciones_supermercado = (
                reposiciones_supermercado + 1
            )


            print(
                "ALMACEN -> SUPERMERCADO:",
                cantidad_necesaria,
                "unidades de",
                productos.productos[i]
            )

            print(
                "Nuevo stock supermercado:",
                productos.stock_supermercado[i]
            )

            print(
                "Nuevo stock almacen:",
                productos.stock_almacen[i]
            )


            # COMPROBAR STOCK DEL ALMACEN

            if productos.stock_almacen[i] <= productos.stock_minimo_almacen[i]:

                print(
                    "Stock bajo en almacen de",
                    productos.productos[i]
                )

                print("Solicitando productos a la fabrica...")


                # Cantidad necesaria para devolver el almacen
                # a su stock inicial
                cantidad_fabrica = (
                    stock_objetivo_almacen[i]
                    - productos.stock_almacen[i]
                )

                productos.stock_almacen[i] = (
                    productos.stock_almacen[i]
                    + cantidad_fabrica
                )

                pedidos_fabrica = pedidos_fabrica + 1


                print(
                    "FABRICA -> ALMACEN:",
                    cantidad_fabrica,
                    "unidades de",
                    productos.productos[i]
                )

                print(
                    "Nuevo stock almacen:",
                    productos.stock_almacen[i]
                )


# FIN DE LA SIMULACION

print("\n\n========================================")
print("          FIN DE LA SIMULACION")
print("========================================")

print("Clientes atendidos:", numero_clientes)

print(
    "Ingresos totales:",
    round(ingresos_totales, 2),
    "€"
)

print(
    "Reposiciones del supermercado:",
    reposiciones_supermercado
)

print(
    "Pedidos realizados a la fabrica:",
    pedidos_fabrica
)


# STOCK FINAL DEL SUPERMERCADO

print("\n========================================")
print("      STOCK FINAL SUPERMERCADO")
print("========================================")

for i in range(len(productos.productos)):

    print(
        productos.productos[i],
        "-",
        productos.stock_supermercado[i],
        "unidades"
    )


# STOCK FINAL DEL ALMACEN

print("\n========================================")
print("         STOCK FINAL ALMACEN")
print("========================================")

for i in range(len(productos.productos)):

    print(
        productos.productos[i],
        "-",
        productos.stock_almacen[i],
        "unidades"
    )

def calcular_cantidad_reposicion(stock_minimo_almacen):
    
    cantidad_reposicion = []

    for stock_minimo in stock_minimo_almacen:
        cantidad_reposicion.append(stock_minimo * 2)

    return cantidad_reposicion

cantidad_reposicion = calcular_cantidad_reposicion(stock_minimo_almacen)

print(cantidad_reposicion)


def reponer_stock(stock_almacen):
    
    if stock_almacen <= stock_minimo_almacen:
        stock_almacen = stock_almacen + cantidad_reposicion
    
    return stock_almacen